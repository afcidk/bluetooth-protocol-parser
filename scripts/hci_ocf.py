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
        'Num_Responses': 1,
        'ORDER': [
            'LAP' ,
            'Inquiry_Length',
            'Num_Responses',
        ]
    },
    'HCI_Inquiry_Cancel': {
        #'Status': 1
        'ORDER': []
    },
    'HCI_Periodic_Inquiry_Mode': {
        'Max_Period_Length': 2,
        'Min_Period_Length': 2,
        'LAP': 3,
        'Inquiry_Length': 1,
        'Num_Responses': 1,
        #'Status': 1
        'ORDER': [
            'Max_Period_Length',
            'Min_Period_Length',
            'LAP',
            'Inquiry_Length',
            'Num_Responses',
        ]
    },
    'HCI_Exit_Periodic_Inquiry_Mode': {
        #'Status': 1
        'ORDER': []
    },
    'HCI_Create_Connection': {
        'BD_ADDR': 6,
        'Packet_Type': 2,
        'Page_Scan_Repetition_Mode': 1,
        'Reserved': 1,
        'Clock_Offset': 2,
        'Allow_Role_Switch': 1,
        'ORDER': [
            'BD_ADDR',
            'Packet_Type',
            'Page_Scan_Repetition_Mode',
            'Reserved',
            'Clock_Offset',
            'Allow_Role_Switch',
        ]
    },
    'HCI_Disconnect': {
        'Connection_Handle': 2,
        'Reason': 1,
        'ORDER': [
            'Connection_Handle',
            'Reason',
        ]
    },
    'HCI_Create_Connection_Cancel': {
        'BD_ADDR': 6,
        #'Status': 1
        'ORDER': ['BD_ADDR']
    },
    'HCI_Accept_Connection_Request': {
        'BD_ADDR': 6,
        'Role': 1,
        'ORDER': [
            'BD_ADDR',
            'Role',
        ]
    },
    'HCI_Reject_Connection_Request': {
        'BD_ADDR': 6,
        'Reason': 1,
        'ORDER': [
            'BD_ADDR',
            'Reason',
        ]
    },
    'HCI_Link_Key_Request_Reply': {
         'BD_ADDR': 6,
         'Link_Key': 16,
         #'Status': 1
         'ORDER': [
             'BD_ADDR',
             'Link_Key',
        ]
    },
    'HCI_Link_Key_Request_Negative_Reply': {
        'BD_ADDR': 6,
        #'Status': 1
        'ORDER': ['BD_ADDR']
    },
    'HCI_PIN_Code_Request_Reply': {
        'BD_ADDR': 6,
        'PIN_Code_Length': 1,
        'PIN_Code': 16,
        #'Status': 1
        'ORDER': [
            'BD_ADDR',
            'PIN_Code_Length',
            'PIN_Code',
        ]
    },
    'HCI_PIN_Code_Request_Negative_Reply': {
        'BD_ADDR': 3,
        #'Status': 1
        'ORDER': ['BD_ADDR']
    },
    'HCI_Change_Connection_Packet_Type': {
        'Connection_Handle': 2,
        'Packet_Type': 2,
        'ORDER': [
            'Connection_Handle',
            'Packet_Type',
        ]
    },
    'HCI_Authentication_Requested': {
        'Connection_Handle': 2,
        'ORDER': ['Connection_Handle']
    },
    'HCI_Set_Connection_Encryption': {
        'Connection_Handle': 2,
        'Encryption_Enable': 1,
        'ORDER': [
            'Connection_Handle',
            'Encryption_Enable',
        ]
    },
    'HCI_Change_Connection_Link_Key': {
        'Connection_Handle': 2,
        'ORDER': ['Connection_Handle']
    },
    'HCI_Master_Link_Key': {
        'Key_Flag': 1,
        'ORDER': ['Key_Flag']
    },
    'HCI_Remote_Name_Request': {
        'BD_ADDR': 6,
        'Page_Scan_Repetition_Mode': 1,
        'Reserved': 1,
        'Clock_Offset': 2,
        'ORDER': [
            'BD_ADDR',
            'Page_Scan_Repetition_Mode',
            'Reserved',
            'Clock_Offset',
        ]
    },
    'HCI_Remote_Name_Request_Cancel': {
        'BD_ADDR': 6,
        #'Status': 1
        'ORDER': ['BD_ADDR']
    },
    'HCI_Read_Remote_Supported_Features': {
        'Connection_Handle': 2,
        'ORDER': ['Connection_Handle']
    },
    'HCI_Read_Remote_Extended_Features': {
        'Connection_Handle': 2,
        'Page Number': 1,
        'ORDER': [
            'Connection_Handle',
            'Page Number',
        ]
    },
    'HCI_Read_Remote_Version_Information': {
        'Connection_Handle': 2,
        'ORDER': ['Connection_Handle']
    },
    'HCI_Read_Clock_Offset': {
        'Connection_Handle': 2,
        'ORDER': ['Connection_Handle']
    },
    'HCI_Read_LMP_Handle': {
        'Connection_Handle': 2,
        #'Status': 1,
        #'LMP_Handle': 1,
        #'Reserved': 4
        'ORDER': ['Connection_Handle']
    },
    'HCI_Setup_Synchronous_Connection': {
        'Connection_Handle': 2,
        'Transmit_Bandwidth': 4,
        'Receive_Bandwidth': 4,
        'Max_Latency': 2,
        'Voice_Setting': 2,
        'Retransmission_Effort': 1,
        'Packet Type': 2,
        'ORDER': [
            'Connection_Handle',
            'Transmit_Bandwidth',
            'Receive_Bandwidth',
            'Max_Latency',
            'Voice_Setting',
            'Retransmission_Effort',
            'Packet Type',
        ]
    },
    'HCI_Accept_Synchronous_Connection_Request': {
        'BD_ADDR': 6,
        'Transmit_Bandwidth': 4,
        'Receive_Bandwidth': 4,
        'Max_Latency': 2,
        'Voice_Setting': 2,
        'Retransmission_Effort': 1,
        'Packet_Type': 2,
        'ORDER': [
            'BD_ADDR',
            'Transmit_Bandwidth',
            'Receive_Bandwidth',
            'Max_Latency',
            'Voice_Setting',
            'Retransmission_Effort',
            'Packet_Type',
        ]
    },
    'HCI_Reject_Synchronous_Connection_Request': {
        'BD_ADDR': 6,
        'Reason': 1,
        'ORDER': [
            'BD_ADDR',
            'Reason',
        ]
    },
    'HCI_IO_Capability_Request_Reply': {
        'BD_ADDR': 6,
        'IO_Capability': 1,
        'OOB_Data_Present': 1,
        'Authentication_Requirements': 1,
        #'Status': 1
        'ORDER': [
            'BD_ADDR',
            'IO_Capability',
            'OOB_Data_Present',
            'Authentication_Requirements',
        ]
    },
    'HCI_User_Confirmation_Request_Reply': {
        'BD_ADDR': 6,
        #'Status': 1
        'ORDER': ['BD_ADDR']
    },
    'HCI_User_Confirmation_Request_Negative_Reply': {
        'BD_ADDR': 6,
        #'Status': 1
        'ORDER': ['BD_ADDR']
    },
    'HCI_User_Passkey_Request_Reply': {
        'BD_ADDR': 6,
        'Numeric_Value': 4,
        #'Status': 1
        'ORDER': [
            'BD_ADDR',
            'Numeric_Value',
        ]
    },
    'HCI_User_Passkey_Request_Negative_Reply': {
        'BD_ADDR': 6,
        #'Status': 1
        'ORDER': ['BD_ADDR']
    },
    'HCI_Remote_OOB_Data_Request_Reply': {
        'BD_ADDR': 6,
        'C': 16,
        'R': 16,
        #'Status': 1
        'ORDER': [
            'BD_ADDR',
            'C',
            'R',
        ]
    },
    'HCI_Remote_OOB_Data_Request_Negative_Reply': {
        'BD_ADDR': 6,
        #'Status': 1
        'ORDER': ['BD_ADDR']
    },
    'HCI_IO_Capability_Request_Negative_Reply': {
        'BD_ADDR': 6,
        'Reason': 1,
        #'Status': 1
        'ORDER': [
            'BD_ADDR',
            'Reason',
        ]
    },
    'HCI_Create_Physical_Link': {
        'Physical_Link_Handle': 1,
        'Dedicated_AMP_Key_Length': 1,
        'Dedicated_AMP_Key_Type': 1,
        #'Dedicated_AMP_Key': AMP_Key_Length Octets
        'ORDER': [
            'Physical_Link_Handle',
            'Dedicated_AMP_Key_Length',
            'Dedicated_AMP_Key_Type',
        ]
    },
    'HCI_Accept_Physical_Link': {
        'Physical_Link_Handle': 1,
        'Dedicated_AMP_Key_Length': 1,
        'Dedicated_AMP_Key_Type': 1,
        #'Dedicated_AMP_Key':  Dedicated_AMP_Key_Length Octets
        'ORDER': [
            'Physical_Link_Handle',
            'Dedicated_AMP_Key_Length',
            'Dedicated_AMP_Key_Type',
        ]
    },
    'HCI_Disconnect_Physical_Link': {
        'Physical_Link_Handle': 1,
        'Reason': 1,
        'ORDER': [
            'Physical_Link_Handle',
            'Reason',
        ]
    },
    'HCI_Create_Logical_Link': {
        'Physical_Link_Handle': 1,
        'Tx_Flow_Spec': 16,
        'Rx_Flow_Spec': 16,
        'ORDER': [
            'Physical_Link_Handle',
            'Tx_Flow_Spec',
            'Rx_Flow_Spec',
        ]
    },
    'HCI_Accept_Logical_Link': {
        'Physical_Link_Handle': 1,
        'Tx_Flow_Spec': 16,
        'Rx_Flow_Spec': 16,
        'ORDER': [
            'Physical_Link_Handle',
            'Tx_Flow_Spec',
            'Rx_Flow_Spec',
        ]
    },
    'HCI_Disconnect_Logical_Link': {
        'Logical_Link_Handle': 2,
        'ORDER': ['Logical_Link_Handle']
    },
    'HCI_Logical_Link_Cancel': {
        'Physical_Link_Handle': 1,
        'Tx_Flow_Spec_ID': 1,
        #'Status': 1
        'ORDER': [
            'Physical_Link_Handle',
            'Tx_Flow_Spec_ID',
        ]
    },
    'HCI_Flow_Spec_Modify' :{
        'Handle': 2,
        'Tx_Flow_Spec': 16,
        'Rx_Flow_Spec': 16,
        'ORDER': [
            'Handle',
            'Tx_Flow_Spec',
            'Rx_Flow_Spec',
        ]
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
        'Retransmission_Effort': 1,
        'ORDER': [
            'Connection_Handle',
            'Transmit_Bandwidth',
            'Receive_Bandwidth',
            'Transmit_Coding_Format',
            'Receive_Coding_Format',
            'Transmit_Codec_Frame_Size',
            'Receive_Codec_Frame_Size',
            'Input_Bandwidth',
            'Output_Bandwidth',
            'Input_Coding_Format',
            'Output_Coding_Format',
            'Input_Coded_Data_Size',
            'Output_Coded_Data_Size',
            'Input_PCM_Data_Format',
            'Output_PCM_Data_Format',
            'Input_PCM_Sample_Payload_MSB_Position',
            'Output_PCM_Sample_Payload_MSB_Position',
            'Input_Data_Path',
            'Output_Data_Path',
            'Input_Transport_Unit_Size',
            'Output_Transport_Unit_Size',
            'Max_Latency',
            'Packet_Type',
            'Retransmission_Effort',
        ]
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
        'Retransmission_Effort': 1,
        'ORDER': [
            'BD_ADDR',
            'Transmit_Bandwidth',
            'Receive_Bandwidth',
            'Transmit_Coding_Format',
            'Receive_Coding_Format',
            'Transmit_Codec_Frame_Size',
            'Receive_Codec_Frame_Size',
            'Input_Bandwidth',
            'Output_Bandwidth',
            'Input_Coding_Format',
            'Output_Coding_Format',
            'Input_Coded_Data_Size',
            'Output_Coded_Data_Size',
            'Input_PCM_Data_Format',
            'Output_PCM_Data_Format',
            'Input_PCM_Sample_Payload_MSB_Position',
            'Output_PCM_Sample_Payload_MSB_Position',
            'Input_Data_Path',
            'Output_Data_Path',
            'Input_Transport_Unit_Size',
            'Output_Transport_Unit_Size',
            'Max_Latency',
            'Packet_Type',
            'Retransmission_Effort',
        ]
    },
    'HCI_Truncated_Page': {
        'BD_ADDR': 6,
        'Page_Scan_Repetition_Mode': 1,
        'Clock_Offset': 2,
        'ORDER': [
            'BD_ADDR',
            'Page_Scan_Repetition_Mode',
            'Clock_Offset',
        ]
    },
    'HCI_Truncated_Page_Cancel': {
        'BD_ADDR': 6,
        #'Status': 1
        'ORDER': ['BD_ADDR']
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
        'ORDER': [
            'Enable',
            'LT_ADDR',
            'LPO_Allowed',
            'Packet_Type',
            'Interval_Min',
            'Interval_Max',
            'CSB_supervisionTO',
        ]
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
        'ORDER': [
            'Enable',
            'BD_ADDR',
            'LT_ADDR',
            'Interval',
            'Clock_Offset',
            'Next_Connectionless_Slave_Broadcast_Clock',
            'CSB_supervisionTO',
            'Remote_Timing_Accuracy',
            'Skip',
            'Packet_Type',
            'AFH_Channel_Map',
        ]
    },
    'HCI_Receive_Synchronization_Train': {
        'BD_ADDR': 6,
        'synchronization_scanTO': 2,
        'Sync_Scan_Window': 2,
        'Sync_Scan_Interval': 2,
        'ORDER': [
            'BD_ADDR',
            'synchronization_scanTO',
            'Sync_Scan_Window',
            'Sync_Scan_Interval',
        ]
    },
    'HCI_Remote_OOB_Extended_Data_Request_Reply': {
        'BD_ADDR': 6,
        'C_192': 16,
        'R_192': 16,
        'C_256': 16,
        'R_256': 16,
        #'Status': 1
        'ORDER': [
            'BD_ADDR',
            'C_192',
            'R_192',
            'C_256',
            'R_256',
        ]
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
        'Hold_Mode_Min_Interval': 2,
        'ORDER': [
            'Connection_Handle',
            'Hold_Mode_Max_Interval',
            'Hold_Mode_Min_Interval',
        ]
    },
    'HCI_Sniff_Mode':{
        'Connection_Handle': 2,
        'Sniff_Max_Interval': 2,
        'Sniff_Min_Interval': 2,
        'Sniff_Attempt': 2,
        'Sniff_Timeout': 2,
        'ORDER': [
            'Connection_Handle',
            'Sniff_Max_Interval',
            'Sniff_Min_Interval',
            'Sniff_Attempt',
            'Sniff_Timeout',
        ]
    },
    'HCI_Exit_Sniff_Mode': {
        'Connection_Handle': 2,
        'ORDER': ['Connection_Handle']
    },
    'HCI_QoS_Setup': {
        'Connection_Handle': 2,
        'Flags': 1,
        'Service_Type': 1,
        'Token_Rate': 4,
        'Peak_Bandwidth': 4,
        'Latency': 4,
        'Delay_Variation': 4,
        'ORDER': [
            'Connection_Handle',
            'Flags',
            'Service_Type',
            'Token_Rate',
            'Peak_Bandwidth',
            'Latency',
            'Delay_Variation',
        ]
    },
    'HCI_Role_Discovery': {
        'Connection_Handle': 2,
        #'Status': 1,
        #'Current_Role': 1
        'ORDER': ['Connection_Handle']
    },
    'HCI_Switch_Role': {
         'BD_ADDR': 6,
         'Role': 1,
         'ORDER': [
             'BD_ADDR',
             'Role'
          ]
    },
    
}


# when OGF = 3
hci_ctrller_baseband_ocf_code = {
    1: 'HCI_Set_Event_Mask',
    11: 'HCI_Write_PIN_Type',
    12: 'HCI_Create_New_Unit_Key',
    14: 'HCI_Read_Stored_Link_Key',
    #17: 'HCI_Write_Stored_Link_Key',
    18: 'HCI_Delete_Stored_Link_Key',
    19: 'HCI_Write_Local_Name',
    20: 'HCI_Read_Local_Name',
    22: 'HCI_Write_Connection_Accept_Timeout',
    24: 'HCI_Write_Page_Timeout',
    26: 'HCI_Write_Scan_Enable',
    28: 'HCI_Write_Page_Scan_Activity',
    30: 'HCI_Write_Inquiry_Scan_Activity',
    32: 'HCI_Write_Authentication_Enable',
    36: 'HCI_Write_Class_of_Device',
    38: 'HCI_Write_Voice_Setting',
    39: 'HCI_Read_Automatic_Flush_Timeout',
    40: 'HCI_Write_Automatic_Flush_Timeout',
    #41: 'HCI_Read_Num_Broadcast_Retransmissions',
    42: 'HCI_Write_Num_Broadcast_Retransmissions',
    44: 'HCI_Write_Hold_Mode_Activity',
    45: 'HCI_Read_Transmit_Power_Level',
    47: 'HCI_Write_Synchro-nous_Flow_Control_Enable',
    49: 'HCI_Set_Controller_To_Host_Flow_Control',
    51: 'HCI_Host_Buffer_Size',
    #53: 'HCI_Host_Number_Of_Completed_Packets',
    54: 'HCI_Read_Link_Supervision_Timeout',
    55: 'HCI_Write_Link_Supervision_Timeout',
    63: 'Set_AFH_Host_Channel_Classification',
    67: 'HCI_Write_Inquiry_Scan_Type',
    69: 'HCI_Write_Inquiry_Mode',
    71: 'HCI_Write_Page_Scan_Type',
    73: 'Write_AFH_Channel_Assessment_Mode',
    82: 'HCI_Write_Extended_Inquiry_Response',
    83: 'HCI_Refresh_Encryption_Key',
    86: 'HCI_Write_Simple_Pairing_Mode',
    89: 'HCI_Write_Inquiry_Transmit_Power_Level',
    96: 'HCI_Send_Keypress_Notification',
    
}

hci_ctrller_baseband_ocf_parameters = {
    'HCI_Set_Event_Mask': {
        'Event_Mask': 8,
        #'Status': 1
        'ORDER': ['Event_Mask']
    },
    'HCI_Write_PIN_Type': {
        'PIN_Type': 1,
        'ORDER': ['PIN_Type']
    },
    'HCI_Create_New_Unit_Key': {
        #'Status': 1
        'ORDER': []
    },
    'HCI_Read_Stored_Link_Key': {
        'BD_ADDR': 6,
        'Read_All_Flag': 1,
        'ORDER': [
            'BD_ADDR',
            'Read_All_Flag',
        ]
    },
    'HCI_Write_Stored_Link_Key': {
        'ORDER': []
    },
    'HCI_Delete_Stored_Link_Key': {
        'BD_ADDR': 6,
        'Delete_All_Flag': 1,
        'ORDER': [
            'BD_ADDR',
            'Delete_All_Flag',
        ]
    },
    'HCI_Write_Local_Name': {
        'Local Name': 248,
        'ORDER': ['Local Name']
    },
    'HCI_Read_Local_Name': {
        'ORDER': []
    },
    'HCI_Write_Connection_Accept_Timeout': {
        'Conn_Accept_Timeout': 2,
        'ORDER': ['Conn_Accept_Timeout']
    },
    'HCI_Write_Page_Timeout': {
        'Page_Timeout': 2,
        'ORDER': ['Page_Timeout']
    },
    'HCI_Write_Scan_Enable': {
        'Scan_Enable': 1,
        'ORDER': ['Scan_Enable']
    },
    'HCI_Write_Page_Scan_Activity': {
        'Page_Scan_Interval': 2,
        'Page_Scan_Window': 2,
        'ORDER': [
            'Page_Scan_Interval',
            'Page_Scan_Window',
        ]
    },
    'HCI_Write_Inquiry_Scan_Activity': {
        'Inquiry_Scan_Interval': 2,
        'Inquiry_Scan_Window': 2,
        'ORDER': [
            'Inquiry_Scan_Interval',
            'Inquiry_Scan_Window',
        ]
    },
    'HCI_Write_Authentication_Enable': {
        'Authentication_Enable': 1,
        'ORDER': ['Authentication_Enable']
    },
    'HCI_Write_Class_of_Device': {
        'Class_of_Device': 3,
        'ORDER': ['Class_of_Device']
    },
    'HCI_Write_Voice_Setting': {
        'Voice_Setting': 2,
        'ORDER': ['Voice_Setting']
    },
    'HCI_Read_Automatic_Flush_Timeout': {
        'Connection_Handle': 2,
        'ORDER': ['Connection_Handle']
    },
    'HCI_Write_Automatic_Flush_Timeout': {
        'Connection_Handle': 2,
        'Flush_Timeout': 2,
        'ORDER': [
            'Connection_Handle',
            'Flush_Timeout',
        ]
    },
    'HCI_Read_Num_Broadcast_Retransmissions': {
        'ORDER': []
    },
    'HCI_Write_Num_Broadcast_Retransmissions': {
        'Num_Broadcast_Retransmissions' : 1,
        'ORDER': ['Num_Broadcast_Retransmissions']
    },
    'HCI_Write_Hold_Mode_Activity': {
        'Hold_Mode_Activity': 1,
        'ORDER': ['Hold_Mode_Activity']
    },
    'HCI_Read_Transmit_Power_Level': {
        'Connection_Handle': 2,
        'Type': 1,
        'ORDER': [
            'Connection_Handle',
            'Type',
        ]
    },
    'HCI_Write_Synchro-nous_Flow_Control_Enable': {
        'Synchronous_Flow_Control_Enable': 1,
        'ORDER': ['Synchronous_Flow_Control_Enable']
    },
    'HCI_Set_Controller_To_Host_Flow_Control': {
        'Flow_Control_Enable': 1,
        'ORDER': ['Flow_Control_Enable']
    },
    'HCI_Host_Buffer_Size': {
        'Host_ACL_Data_Packet_Length': 2,
        'Host_Synchronous_Data_Packet_Length': 1,
        'Host_Total_Num_ACL_Data_Packets': 2,
        'Host_Total_Num_Synchronous_Data_Packets': 2,
        'ORDER': [
            'Host_ACL_Data_Packet_Length',
            'Host_Synchronous_Data_Packet_Length',
            'Host_Total_Num_ACL_Data_Packets',
            'Host_Total_Num_Synchronous_Data_Packets'
        ]
    },
    'HCI_Host_Number_Of_Completed_Packets': {
        'Number_Of_Handles': 1, 
        #'Connection_Handle[i]': Number_Of_Handles*2,
        #'Host_Num_Of_Completed_Packets [i]': Number_Of_Handles*2
        'ORDER': ['Number_Of_Handles']
    },
    'HCI_Read_Link_Supervision_Timeout': {
        'Handle': 2,
        'ORDER': ['Handle']
    },
    'HCI_Write_Link_Supervision_Timeout': {
        'Handle': 2,
        'Link_Supervision_Timeout': 2,
        'ORDER': [
            'Handle',
            'Link_Supervision_Timeout',
        ]
    },
    'Set_AFH_Host_Channel_Classification': {
        'AFH_Host_Channel_Classification': 10,
        'ORDER': ['AFH_Host_Channel_Classification']
    },
    'HCI_Write_Inquiry_Scan_Type': {
        'Scan_Type': 1,
        'ORDER': ['Scan_Type']
    },
    'HCI_Write_Inquiry_Mode': {
        'Inquiry_Mode': 1,
        'ORDER': ['Inquiry_Mode']
    },
    'HCI_Write_Page_Scan_Type': {
        'Page_Scan_Type': 1,
        'ORDER': ['Page_Scan_Type']
    },
    'Write_AFH_Channel_Assessment_Mode': {
        'AFH_Channel_Assessment_Mode': 1,
        'ORDER': ['AFH_Channel_Assessment_Mode']
    },
    'HCI_Write_Extended_Inquiry_Response': {
        'FEC_Required': 1, 
        'Extended_Inquiry_Response': 240,
        'ORDER': [
            'FEC_Required',
            'Extended_Inquiry_Response',
        ]
    },
    'HCI_Refresh_Encryption_Key': {
        'Connection_Handle': 2,
        'ORDER': ['Connection_Handle']
    },
    'HCI_Write_Simple_Pairing_Mode': {
        'Simple_Pairing_Mode': 1,
        'ORDER': ['Simple_Pairing_Mode']
    },
    'HCI_Write_Inquiry_Transmit_Power_Level': {
        'TX_Power': 1,
        'ORDER': ['TX_Power']
    },
    'HCI_Send_Keypress_Notification': {
        'BD_ADDR': 6, 
        'Notification_Type': 1,
        'ORDER': [
            'BD_ADDR',
            'Notification_Type',
        ]
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
        #'LMP Subversion': 2,
        'ORDER': []
    },
    'HCI_Read_Local_Supported_Commands': {
        #'Status': 1,
        #'Supported_Commands': 64,
        'ORDER': []
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
        #'Failed_Contact_Counter': 2,
        'ORDER': ['Handle']
    },
    'HCI_Reset_Failed_Contact_Counter': {
        'Handle': 2,
        #'Status': 1,
        'ORDER': ['Handle']
    },
    'HCI_Read_Link_Quality': {
        'Handle': 2,
        #'Status': 1,
        #'Link_Quality': 1,
        'ORDER': ['Handle']
    },
    'HCI_Read_RSSI': {
        'Handle': 2,
        #'Status': 1,
        #'RSSI': 1,
        'ORDER': ['Handle']
    },
    'HCI_Read_AFH_Channel_Map': {
        'Connection_Handle': 2,
        #'Status': 1,
        #'AFH_Mode': 1,
        #'AFH_Channel_Map': 10,
        'ORDER': ['Connection_Handle']
    },
    'HCI_Read_Clock': {
        'Connection_Handle': 2,
        'Which_Clock': 1,
        #'Status': 1,
        #'Clock': 4,
        #'Accuracy':2,
        'ORDER': [
            'Connection_Handle',
            'Which_Clock',
        ]
    },
    'HCI_Read_Encryption_Key_Size': {
        'Connection_Handle': 2,
        #'Status': 1,
        #'Key_Size': 1,
        'ORDER': ['Connection_Handle']
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
        #'Best_Effort_Flush_Timeout': 4,
        'ORDER': ['']
    },
            
}


# when OGF = 6
hci_test_ocf_code = {
    1: 'HCI_Read_Loopback_Mode',
    
}

hci_test_ocf_parameters = {
    'HCI_Read_Loopback_Mode': {
        #'Status': 1,
        #'Loopback_Mode': 1,
        'ORDER': ['']
    },
            
}
