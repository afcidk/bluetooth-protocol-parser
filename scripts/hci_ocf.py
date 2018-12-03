def cmd_code(ogf):
    if(ogf == 1):
        return hci_link_ctrl_ocf_code
    elif(ogf == 2):
        return hci_link_policy_ocf_code
    elif(ogf == 3):
        return hci_ctrller_baseband_ocf_code
    elif(ogf == 4):
        return hci_info_ocf_code
    elif(ogf == 5):
        return hci_status_ocf_code
    elif(ogf == 6):
        return hci_test_ocf_code

def cmd_parameters(ogf):
    if(ogf == 1):
        return hci_link_ctrl_ocf_parameters
    elif(ogf == 2):
        return hci_link_policy_ocf_parameters
    elif(ogf == 3):
        return hci_ctrller_baseband_ocf_parameters
    elif(ogf == 4):
        return hci_info_ocf_parameters
    elif(ogf == 5):
        return hci_status_ocf_parameters
    elif(ogf == 6):
        return hci_test_ocf_parameters

# when OGF = 1
hci_link_ctrl_ocf_code = {
    1: 'HCI_Inquiry',
    2: 'HCI_Inquiry_Cancel',
    3: 'HCI_Periodic_Inquiry_Mode',
    4: 'HCI_Exit_Periodic_Inquiry_Mode',
    5: 'HCI_Create_Connection',
    6: 'HCI_Disconnect',
    8: 'HCI_Create_Connection_Cancel',
    9: 'HCI_Accept_Connection_Request',
    10: 'HCI_Reject_Connection_Request',
    11: 'HCI_Link_Key_Request_Reply',
    12: 'HCI_Link_Key_Request_Negative_Reply',
    13: 'HCI_PIN_Code_Request_Reply',
    14: 'HCI_PIN_Code_Request_Negative_Reply',
    15: 'HCI_Change_Connection_Packet_Type',
    17: 'HCI_Authentication_Requested',
    19: 'HCI_Set_Connection_Encryption',
    21: 'HCI_Change_Connection_Link_Key',
    23: 'HCI_Master_Link_Key',
    25: 'HCI_Remote_Name_Request',
    26: 'HCI_Remote_Name_Request_Cancel',
    27: 'HCI_Read_Remote_Supported_Features',
    28: 'HCI_Read_Remote_Extended_Features',
    29: 'HCI_Read_Remote_Version_Information',
    31: 'HCI_Read_Clock_Offset',
    32: 'HCI_Read_LMP_Handle',
    40: 'HCI_Setup_Synchronous_Connection',
    41: 'HCI_Accept_Synchronous_Connection_Request',
    42: 'HCI_Reject_Synchronous_Connection_Request',
    43: 'HCI_IO_Capability_Request_Reply',
    44: 'HCI_User_Confirmation_Request_Reply',
    45: 'HCI_User_Confirmation_Request_Negative_Reply',
    46: 'HCI_User_Passkey_Request_Reply',
    47: 'HCI_User_Passkey_Request_Negative_Reply',
    48: 'HCI_Remote_OOB_Data_Request_Reply',
    51: 'HCI_Remote_OOB_Data_Request_Negative_Reply',
    52: 'HCI_IO_Capability_Request_Negative_Reply',
    53: 'HCI_Create_Physical_Link',
    54: 'HCI_Accept_Physical_Link',
    55: 'HCI_Disconnect_Physical_Link',
    56: 'HCI_Create_Logical_Link',
    57: 'HCI_Accept_Logical_Link',
    58: 'HCI_Disconnect_Logical_Link',
    59: 'HCI_Logical_Link_Cancel',
    60: 'HCI_Flow_Spec_Modify',
    61: 'HCI_Enhanced_Setup_Synchronous_Connection',
    62: 'HCI_Enhanced_Accept_Synchronous_Connection_Request',
    63: 'HCI_Truncated_Page',
    64: 'HCI_Truncated_Page_Cancel',
    65: 'HCI_Set_Connectionless_Slave_Broadcast',
    66: 'HCI_Set_Connectionless_Slave_Broadcast_Receive',
    #67: HCI_Start_Synchronization_Train,
    68: 'HCI_Receive_Synchronization_Train',
    69: 'HCI_Remote_OOB_Extended_Data_Request_Reply'
}

hci_link_ctrl_ocf_parameters = {
    'HCI_Inquiry': {
        'LAP' : 3,
        'Inquiry_Length': 1,
        'Num_Responses': 1
    },
    'HCI_Inquiry_Cancel': {
        #'Status': 1
    },
    'HCI_Periodic_Inquiry_Mode': {
        'Max_Period_Length': 2,
        'Min_Period_Length': 2,
        'LAP': 3,
        'Inquiry_Length': 1,
        'Num_Responses': 1,
        #'Status': 1
    },
    'HCI_Exit_Periodic_Inquiry_Mode': {
        #'Status': 1
    },
    'HCI_Create_Connection': {
        'BD_ADDR': 6,
        'Packet_Type': 2,
        'Page_Scan_Repetition_Mode': 1,
        'Reserved': 1,
        'Clock_Offset': 2,
        'Allow_Role_Switch': 1
    },
    'HCI_Disconnect': {
        'Connection_Handle': 2,
        'Reason': 1
    },
    'HCI_Create_Connection_Cancel': {
        'BD_ADDR': 6
        #'Status': 1
    },
    'HCI_Accept_Connection_Request': {
        'BD_ADDR': 6,
        'Role': 1
    },
    'HCI_Reject_Connection_Request': {
        'BD_ADDR': 6,
        'Reason': 1
    },
    'HCI_Link_Key_Request_Reply': {
         'BD_ADDR': 6,
         'Link_Key': 16,
         #'Status': 1
    },
    'HCI_Link_Key_Request_Negative_Reply': {
        'BD_ADDR': 6,
        #'Status': 1
    },
    'HCI_PIN_Code_Request_Reply': {
        'BD_ADDR': 6,
        'PIN_Code_Length': 1,
        'PIN_Code': 16,
        #'Status': 1
    },
    'HCI_PIN_Code_Request_Negative_Reply': {
        'BD_ADDR': 3,
        #'Status': 1
    },
    'HCI_Change_Connection_Packet_Type': {
        'Connection_Handle': 2,
        'Packet_Type': 2
    },
    'HCI_Authentication_Requested': {
        'Connection_Handle': 2
    },
    'HCI_Set_Connection_Encryption': {
        'Connection_Handle': 2,
        'Encryption_Enable': 1
    },
    'HCI_Change_Connection_Link_Key': {
        'Connection_Handle': 2
    },
    'HCI_Master_Link_Key': {
        'Key_Flag': 1
    },
    'HCI_Remote_Name_Request': {
        'BD_ADDR': 6,
        'Page_Scan_Repetition_Mode': 1,
        'Reserved': 1,
        'Clock_Offset': 2
    },
    'HCI_Remote_Name_Request_Cancel': {
        'BD_ADDR': 6,
        #'Status': 1
    },
    'HCI_Read_Remote_Supported_Features': {
        'Connection_Handle': 2
    },
    'HCI_Read_Remote_Extended_Features': {
        'Connection_Handle': 2,
        'Page Number': 1
    },
    'HCI_Read_Remote_Version_Information': {
        'Connection_Handle': 2
    },
    'HCI_Read_Clock_Offset': {
        'Connection_Handle': 2
    },
    'HCI_Read_LMP_Handle': {
        'Connection_Handle': 2,
        #'Status': 1,
        #'LMP_Handle': 1,
        #'Reserved': 4
    },
    'HCI_Setup_Synchronous_Connection': {
        'Connection_Handle': 2,
        'Transmit_Bandwidth': 4,
        'Receive_Bandwidth': 4,
        'Max_Latency': 2,
        'Voice_Setting': 2,
        'Retransmission_Effort': 1,
        'Packet Type': 2
    },
    'HCI_Accept_Synchronous_Connection_Request': {
        'BD_ADDR': 6,
        'Transmit_Bandwidth': 4,
        'Receive_Bandwidth': 4,
        'Max_Latency': 2,
        'Voice_Setting': 2,
        'Retransmission_Effort': 1,
        'Packet_Type': 2
    },
    'HCI_Reject_Synchronous_Connection_Request': {
        'BD_ADDR': 6,
        'Reason': 1
    },
    'HCI_IO_Capability_Request_Reply': {
        'BD_ADDR': 6,
        'IO_Capability': 1,
        'OOB_Data_Present': 1,
        'Authentication_Requirements': 1,
        #'Status': 1
    },
    'HCI_User_Confirmation_Request_Reply': {
        'BD_ADDR': 6,
        #'Status': 1
    },
    'HCI_User_Confirmation_Request_Negative_Reply': {
        'BD_ADDR': 6,
        #'Status': 1
    },
    'HCI_User_Passkey_Request_Reply': {
        'BD_ADDR': 6,
        'Numeric_Value': 4,
        #'Status': 1
    },
    'HCI_User_Passkey_Request_Negative_Reply': {
        'BD_ADDR': 6,
        #'Status': 1
    },
    'HCI_Remote_OOB_Data_Request_Reply': {
        'BD_ADDR': 6,
        'C': 16,
        'R': 16,
        #'Status': 1
    },
    'HCI_Remote_OOB_Data_Request_Negative_Reply': {
        'BD_ADDR': 6,
        #'Status': 1
    },
    'HCI_IO_Capability_Request_Negative_Reply': {
        'BD_ADDR': 6,
        'Reason': 1,
        #'Status': 1
    },
    'HCI_Create_Physical_Link': {
        'Physical_Link_Handle': 1,
        'Dedicated_AMP_Key_Length': 1,
        'Dedicated_AMP_Key_Type': 1,
        #'Dedicated_AMP_Key': AMP_Key_Length Octets
    },
    'HCI_Accept_Physical_Link': {
        'Physical_Link_Handle': 1,
        'Dedicated_AMP_Key_Length': 1,
        'Dedicated_AMP_Key_Type': 1,
        #'Dedicated_AMP_Key':  Dedicated_AMP_Key_Length Octets
    },
    'HCI_Disconnect_Physical_Link': {
        'Physical_Link_Handle': 1,
        'Reason': 1
    },
    'HCI_Create_Logical_Link': {
        'Physical_Link_Handle': 1,
        'Tx_Flow_Spec': 16,
        'Rx_Flow_Spec': 16
    },
    'HCI_Accept_Logical_Link': {
        'Physical_Link_Handle': 1,
        'Tx_Flow_Spec': 16,
        'Rx_Flow_Spec': 16
    },
    'HCI_Disconnect_Logical_Link': {
        'Logical_Link_Handle': 2
    },
    'HCI_Logical_Link_Cancel': {
        'Physical_Link_Handle': 1,
        'Tx_Flow_Spec_ID': 1,
        #'Status': 1
    },
    'HCI_Flow_Spec_Modify' :{
        'Handle': 2,
        'Tx_Flow_Spec': 16,
        'Rx_Flow_Spec': 16
    },
    'HCI_Enhanced_Setup_Synchronous_Connection': {
        'Connection_Handle': 2,
        'Transmit_Bandwidth': 4,
        'Receive_Bandwidth': 4,
        'Transmit_Coding_Format': 5,
        'Receive_Coding_Format': 5,
        'Transmit_Codec_Frame_Size': 2,
        'Receive_Codec_Frame_Size': 2,
        'Input_Bandwidth': 4,
        'Output_Bandwidth': 4,
        'Input_Coding_Format': 5,
        'Output_Coding_Format': 5,
        'Input_Coded_Data_Size': 2,
        'Output_Coded_Data_Size': 2,
        'Input_PCM_Data_Format': 1,
        'Output_PCM_Data_Format': 1,
        'Input_PCM_Sample_Payload_MSB_Position': 1,
        'Output_PCM_Sample_Payload_MSB_Position': 1,
        'Input_Data_Path': 1,
        'Output_Data_Path': 1,
        'Input_Transport_Unit_Size': 1,
        'Output_Transport_Unit_Size': 1,
        'Max_Latency': 2,
        'Packet_Type': 2,
        'Retransmission_Effort': 1
    },
    'HCI_Enhanced_Accept_Synchronous_Connection_Request': {
        'BD_ADDR': 6,
        'Transmit_Bandwidth': 4,
        'Receive_Bandwidth': 4,
        'Transmit_Coding_Format': 5,
        'Receive_Coding_Format': 5,
        'Transmit_Codec_Frame_Size': 2,
        'Receive_Codec_Frame_Size': 2,
        'Input_Bandwidth': 4,
        'Output_Bandwidth': 4,
        'Input_Coding_Format': 5,
        'Output_Coding_Format': 5,
        'Input_Coded_Data_Size': 2,
        'Output_Coded_Data_Size': 2,
        'Input_PCM_Data_Format': 1,
        'Output_PCM_Data_Format': 1,
        'Input_PCM_Sample_Payload_MSB_Position': 1,
        'Output_PCM_Sample_Payload_MSB_Position': 1,
        'Input_Data_Path': 1,
        'Output_Data_Path': 1,
        'Input_Transport_Unit_Size': 1,
        'Output_Transport_Unit_Size': 1,
        'Max_Latency': 2,
        'Packet_Type': 2,
        'Retransmission_Effort': 1
    },
    'HCI_Truncated_Page': {
        'BD_ADDR': 6,
        'Page_Scan_Repetition_Mode': 1,
        'Clock_Offset': 2
    },
    'HCI_Truncated_Page_Cancel': {
        'BD_ADDR': 6,
        #'Status': 1
    },
    'HCI_Set_Connectionless_Slave_Broadcast': {
        'Enable': 1,
        'LT_ADDR': 1,
        'LPO_Allowed': 1,
        'Packet_Type': 2,
        'Interval_Min': 2,
        'Interval_Max': 2,
        'CSB_supervisionTO': 2,
        #'Status': 1,
        #'Interval': 2
    },
    'HCI_Set_Connectionless_Slave_Broadcast_Receive': {
        'Enable': 1,
        'BD_ADDR': 6,
        'LT_ADDR': 1,
        'Interval': 2,
        'Clock_Offset': 4,
        'Next_Connectionless_Slave_Broadcast_Clock': 4,
        'CSB_supervisionTO': 2,
        'Remote_Timing_Accuracy': 1,
        'Skip': 1,
        'Packet_Type': 2,
        'AFH_Channel_Map': 10,
        #'Status': 1
    },
    'HCI_Receive_Synchronization_Train': {
        'BD_ADDR': 6,
        'synchronization_scanTO': 2,
        'Sync_Scan_Window': 2,
        'Sync_Scan_Interval': 2
    },
    'HCI_Remote_OOB_Extended_Data_Request_Reply': {
        'BD_ADDR': 6,
        'C_192': 16,
        'R_192': 16,
        'C_256': 16,
        'R_256': 16,
        #'Status': 1
    }
}


# when OGF = 2
hci_link_policy_ocf_code = {
    1: 'HCI_Hold_Mode',
    3: 'HCI_Sniff_Mode',
    4: 'HCI_Exit_Sniff_Mode',
    7: 'HCI_QoS_Setup',
    9: 'HCI_Role_Discovery',
    11: 'HCI_Switch_Role',
    
}

hci_link_policy_ocf_parameters = {
    'HCI_Hold_Mode': {
        'Connection_Handle': 2,
        'Hold_Mode_Max_Interval': 2,
        'Hold_Mode_Min_Interval': 2
    },
    'HCI_Sniff_Mode':{
        'Connection_Handle': 2,
        'Sniff_Max_Interval': 2,
        'Sniff_Min_Interval': 2,
        'Sniff_Attempt': 2,
        'Sniff_Timeout': 2
    },
    'HCI_Exit_Sniff_Mode': {
        'Connection_Handle': 2
    },
    'HCI_QoS_Setup': {
        'Connection_Handle': 2,
        'Flags': 1,
        'Service_Type': 1,
        'Token_Rate': 4,
        'Peak_Bandwidth': 4,
        'Latency': 4,
        'Delay_Variation': 4
    },
    'HCI_Role_Discovery': {
        'Connection_Handle': 2,
        #'Status': 1,
        #'Current_Role': 1
    },
    'HCI_Switch_Role': {
         'BD_ADDR': 6,
         'Role': 1
    },
    
}


# when OGF = 3
hci_ctrller_baseband_ocf_code = {
    1: 'HCI_Set_Event_Mask',
    11: 'HCI_Write_PIN_Type',
    12: 'HCI_Create_New_Unit_Key',
    14: 'HCI_Read_Stored_Link_Key',
    26: 'HCI_Write_Scan_Enable',
    
}

hci_ctrller_baseband_ocf_parameters = {
    'HCI_Set_Event_Mask': {
        'Event_Mask': 8,
        #'Status': 1
    },
    'HCI_Write_PIN_Type': {
        'PIN_Type': 1
    },
    'HCI_Create_New_Unit_Key': {
        #'Status': 1
    },
    'HCI_Read_Stored_Link_Key': {
        'BD_ADDR': 6,
        'Read_All_Flag': 1
    },
    'HCI_Write_Scan_Enable': {
        'Scan_Enable': 1
    },
                
}


# when OGF = 4
hci_info_ocf_code = {
    1: 'HCI_Read_Local_Version_Information',
    2: 'HCI_Read_Local_Supported_Commands',
    
}

hci_info_ocf_parameters = {
    'HCI_Read_Local_Version_Information': {
        #'Status': 1,
        #'HCI Version': 1,
        #'HCI Revision': 2,
        #'LMP Version': 1,
        #'Manufacturer_Name': 2,
        #'LMP Subversion': 2
    },
    'HCI_Read_Local_Supported_Commands': {
        #'Status': 1,
        #'Supported_Commands': 64
    },
    
}


# when OGF = 5
hci_status_ocf_code = {
    1: 'HCI_Read_Failed_Contact_Counter',
    2: 'HCI_Reset_Failed_Contact_Counter',
    3: 'HCI_Read_Link_Quality',
    5: 'HCI_Read_RSSI',
    6: 'HCI_Read_AFH_Channel_Map',
    7: 'HCI_Read_Clock',
    8: 'HCI_Read_Encryption_Key_Size',
    9: 'HCI_Read_Local_AMP_Info',
    
}

hci_status_ocf_parameters = {
    'HCI_Read_Failed_Contact_Counter': {
        'Handle': 2,
        #'Status': 1,
        #'Failed_Contact_Counter': 2
    },
    'HCI_Reset_Failed_Contact_Counter': {
        'Handle': 2,
        #'Status': 1
    },
    'HCI_Read_Link_Quality': {
        'Handle': 2,
        #'Status': 1,
        #'Link_Quality': 1
    },
    'HCI_Read_RSSI': {
        'Handle': 2,
        #'Status': 1,
        #'RSSI': 1
    },
    'HCI_Read_AFH_Channel_Map': {
        'Connection_Handle': 2,
        #'Status': 1,
        #'AFH_Mode': 1,
        #'AFH_Channel_Map': 10
    },
    'HCI_Read_Clock': {
        'Connection_Handle': 2,
        'Which_Clock': 1,
        #'Status': 1,
        #'Clock': 4,
        #'Accuracy':2
    },
    'HCI_Read_Encryption_Key_Size': {
        'Connection_Handle': 2,
        #'Status': 1,
        #'Key_Size': 1
    },
    'HCI_Read_Local_AMP_Info': {
        #'Status': 1,
        #'AMP_Status': 1,
        #'Total_Bandwidth': 4,
        #'Max_Guaranteed_Bandwidth': 4,
        #'Min_Latency': 4,
        #'Max_PDU_Size': 2,
        #'Controller_Type': 1,
        #'PAL_Capabilities': 2,
        #'Max_AMP_ASSOC_Length': 2,
        #'Max_Flush_Timeout': 4,
        #'Best_Effort_Flush_Timeout': 4
    },
            
}


# when OGF = 6
hci_test_ocf_code = {
    1: 'HCI_Read_Loopback_Mode',
    
}

hci_test_ocf_parameters = {
    'HCI_Read_Loopback_Mode': {
        #'Status': 1,
        #'Loopback_Mode': 1
    },
            
}
