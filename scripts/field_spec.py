from event_contents import event_code, event_parameters

l2cap_data = {
    'Length': 16,
    'Channel_ID': 16,
    'Choose': 'Channel_ID',
    0x0001: {
        'Code': 8,
        'Identifier': 8,
        'Length': 16,
        'Choose': 'Code',
        2: {
            'PSM': 16,
            'Src_CID': 16
        },
        3: {
            'Dst_CID': 16, # This two CIDs must be linked to their upper layer protocol by PSM of Code 0x02 
            'Src_CID': 16,  # This two CIDs must be linked to their upper layer protocol by PSM of Code 0x02
            'Result': 16,
            'Status': 16
        },
        4: {
            'Dst_CID': 16, 
            'Flags': 16,
            'Config_Opt': 32
        },
        5: {
            'Src_CID': 16,
            'Flags': 16,
            'Result': 16,
            'Config': 16,
        },
        6: {
            'Dst_CID': 16,
            'Src_CID': 16
        },
        7: {
            'Dst_CID': 16,
            'Src_CID': 16
        },
        10: {
            'InfoType': 16
        },
        11: {
            'InfoType': 16,
            'Result': 16,
            'Data': -1
        },
        'Name': {
            2: 'Con_req',
            3: 'Con_res',
            4: 'Config_req',
            5: 'Config_res',
            6: 'Discon_req',
            7: 'Discon_res',
            10: 'Info_req',
            11: 'Info_res'
        }
    },
    0x0002: {
        '2': '2',
    },
    -1: {
        'Data': -10, # This part of data will be parsed later (after getting the upper protocol)
        # -10 means reserved to parse later
    },
    'Name': {
        0x0001: 'Signaling Channel',
        0x0002: '0x0002',
        -1    : 'Dynamic allocated' # TODO: change this to correct name later
    }
}

hci_command = {
    'OCF': 10,
    'OGF': 6,
    'Length': 8
}

hci_acl_data = {
    'Handle': 12,
    'PB_Flag': 2,
    'BC_Flag': 2,
    'Length': 16,
    'acl_data': l2cap_data
}

hci_sync_data = {
    'Handle': 12,
    'Packet_Status': 2,
    'RFU': 2,
    'Length': 8
}

hci_event = {
    'Event': 8,
    'Length': 8,
    'Parameter': event_parameters  # all event_parameter are in event_contents.py
}

header_field = {
    'ts_sec': 32,
    'ts_usec': 32,
    'incl_len': 32,
    'orig_len': 32,
    None: 32,
    'packet_type': 8
}

data_field = {
    1: hci_command,
    2: hci_acl_data,
    3: hci_sync_data,
    4: hci_event,
}

sdp_field = {
    'PDU': 8,
    'Transaction_ID': 16,
    'Length': 16,
    'Parameters': -1
}

avdtp_field = { 
    'Msg_type': 2,
    'Packet_type': 2,
    'Transaction': 4,
    'Choose': 'Packet_type',
    0: {
        'Signal_ID': 6,
        'RFA': 2,
        'Choose': 'Signal_ID',
        3: {
            'ACP_RFA': 2,
            'ACP_SEID': 6,
            'INT_RFA': 2,
            'INT_SEID': 6,
            'Capabilities': {
                'Service_Category': 8,
                'LOSC': 8,
                'Service': {
                    'Category': 8,
                    'LOSC': 8,
                    'RFA': 4,
                    'Media_Type': 4,
                    'Codec_Type': 8,
                    'Data': -1
                }
            }
        },
        7: {
            'Signal_Start': -1
        },
        9: {
            'Signal_Suspend': -1
        },
        -1: {
            'Data': -1
        },
        'Name': {
            3: 'SetConfiguration',
            7: 'Signal Start',
            9: 'Signal Suspend',
            -1: 'Undefined'
        }
    },
    1: {
        'NOSP': 8,
        'Signal_ID': 6,
        'RFA': 2,
    },
    2: {
    },
    3: {
    },
    'Name': {
        0: 'Single_Packet',
        1: 'Start_Packet',
        2: 'Continue_Packet',
        3: 'End_Packet'
    }
}

avctp_field = {
    'IPID': 1,
    'C/R': 1,
    'Packet_type': 2,
    'Transaction': 4,
    'Profile_ID': 16,
    'Other_Data': -1
}

psm_field = {
    1: sdp_field,
    23: avctp_field,
    25: avdtp_field,
}

a2dp_field = {
    0: {
        'SID_count': 4,
        'Extension': 1,
        'Padding': 1,
        'Version': 2,
        'Payload_Type': 8,
        'Seq': 16,
        'Timestamp': 32,
        'Sync SID': 32,
        'SBC_Codec': {
            'Frame_numbers': 4,
            'RFA': 1,
            'Last_Packet': 1,
            'Starting_Packet': 1,
            'Fragmented': 1,
            'Frames': -1
        }
    }
}

dynamic_CID_table = dict()
dynamic_CID_table_name = {
    1: 'SDP',
    23: 'AVCTP',
    25: 'AVDTP',
    4105: 'no!'
}

data_start_status = False
data_service_type = None
def parse_field(field, data, cur_channel_id=None):
    global data_start_status
    global data_service_type
    hci_type = check_push_value_count = 0
    ret = dict()
    end = 0
    for key, value in field.items():
        if key is None:
            pass
        elif key == 'Signal_Start':
            data_start_status = True
            break
        elif key == 'Signal_Suspend':
            data_start_status = False
            break
        elif key == 'Choose':
            choose = ret[value]
            if choose not in field: choose = -1

            end8 = int(end/8)
            if 'Length' not in ret:
                inner, _ = parse_field(field[choose], data[end8:], cur_channel_id)
            else:
                inner, _ = parse_field(field[choose], data[end8: end8+ret['Length']], cur_channel_id)
            ret.update(inner)

            ####### specific update for dynamic CID table #######
            if value == 'Code': # 2-side channel
                if choose == 2:
                    if inner['Src_CID'] in dynamic_CID_table and dynamic_CID_table[inner['Src_CID']] != inner['PSM']:
                        pass
                    else:
                        dynamic_CID_table[inner['Src_CID']] = inner['PSM']
                elif choose == 3:
                    dynamic_CID_table[inner['Dst_CID']] = dynamic_CID_table[inner['Src_CID']]
            #####################################################

            break
        
        elif type(value) is int:

            if value == -10: # multiplexing
                end8 = int(end/8)
                op_name = dynamic_CID_table[cur_channel_id]

                if data_start_status == True and len(data[end8:]) > 10: # parse A2DP data
                    inner, _ = parse_field(a2dp_field[data_service_type], data[end8:], cur_channel_id)
                else: # parse PSM field data
                    inner, _ = parse_field(psm_field[op_name], data[end8:], cur_channel_id)
                ret.update({dynamic_CID_table_name[op_name]:inner})
            elif value < 0:
                end8 = int(end/8)
                ret.update({
                    key: data[end8:] if value > -2 else int.from_bytes(data[end8:], 'little')
                })
            else:  # normal usage
                tmp_hci_type = hci_type
                hci_type, typeValue = typeCode_to_typeValue(key, int_from_bits(data, end, end + value))
                hci_type = hci_type if tmp_hci_type == 0 else tmp_hci_type  # if hci_type is changed, then restoring hci_type by tmp_value
                check_push_value_count += 1
                ret.update({
                    key: typeValue
                })

                if key == 'Channel_ID': cur_channel_id = ret['Channel_ID']
                if key == 'Codec_Type': data_service_type = ret['Codec_Type']
        elif type(value) is dict:  
            end8 = int(end/8)
            value = value[ret['Event']] if 'Event' in ret else value
            if 'Length' not in ret:
                inner, _ = parse_field(value, data[end8:], cur_channel_id)
            else: inner, _ = parse_field(value, data[end8: end8+ret['Length']], cur_channel_id)
            ret.update({key: inner})
            continue

        if check_push_value_count == 1: update_right_value_in_dict(field)

        end += value

    data = data[int(end/8):]

    return ret, data

def int_from_bits(data, start, end):
   num = int.from_bytes(data, 'little') 
   return (num>>start) & ((1<<(end-start))-1)

# on Case 4(event), Event code converts to Event name by its code.
# e.g, Event code : 14H (20d) > Event name: Mode Change
# You can modify name and code content,
# but it must contain event_code[pure_int] ... to get event name
# return hci_type by data_field and name
def typeCode_to_typeValue(key, pure_int):
    if key in header_field:
        return -1, pure_int
    elif key in data_field[1]:
        return 1, pure_int
    elif key in data_field[2]:
        return 2, pure_int
    elif key in data_field[3]:
        return 3, pure_int
    elif key in data_field[4]:
        return 4, event_code[pure_int]
    else:
        return 0, pure_int


def update_right_value_in_dict(data_dict):
    # get first key and value to update last parameter
    first_parmtr = [list(data_dict.keys())[0], list(data_dict.values())[0]]

    for key, value in data_dict.items():
        # -1 and -2 belong to special case, -3 and -4 belong to reserved field
        if type(value) is int and value < -4:
            value = value * -1 * first_parmtr[1]  # index 1 is first value in dict