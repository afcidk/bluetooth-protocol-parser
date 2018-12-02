event_code = {
    1: 'Inquiry Complete',
    2: 'Inquiry Result',
    3: 'Connection Complete',
    4: 'Connection Request',
    5: 'Disconnection Complete',
    6: 'Authentication Complete',
    7: 'Remote Name Request Complete',
    8: 'Encryption Change',
    9: 'Change Connection Link Key Complete',
    10: 'Master Link Key Complete',
    11: 'Read Remote Supported Features Complete',
    12: 'Read Remote Version Information Complete',
    13: 'QoS Setup Complete',
    14: 'Command Complete',
    15: 'Command Status',
    16: 'Hardware Error',
    17: 'Flush Occurred',
    18: 'Role Change',
    19: 'Number Of Completed Packets',
    20: 'Mode Change',
    21: 'Return Link Keys',
    22: 'PIN Code Request',
    23: 'Link Key Request',
    24: 'Link Key Notification',
    25: 'Loopback Command',
    26: 'Data Buffer Overflow',
    27: 'Max Slots Change',
    28: 'Read Clock Offset Complete',
    29: 'Connection Packet Type Changed',
    30: 'QoS Violation',
    32: 'Page Scan Repetition Mode Change',
    33: 'Flow Specification Complete',
    34: 'Inquiry Result with RSSI',
    35: 'Read Remote Extended Features Complete',
    44: 'Synchronous Connection Complete',
    45: 'Synchronous Connection Changed',
    46: 'Sniff Subrating',
    47: 'Extended Inquiry Result',
    48: 'Encryption Key Refresh Complete',
    49: 'IO Capability Request',
    50: 'IO Capability Response',
    51: 'User Confirmation Request',
    52: 'User Passkey Request',
    53: 'Remote OOB Data Request',
    54: 'Simple Pairing Complete',
    56: 'Link Supervision Timeout Changed',
    57: 'Enhanced Flush Complete',
    59: 'User Passkey Notification',
    60: 'Keypress Notification',
    61: 'Remote Host Supported Features Notification',
    62: 'LE',  # LE, MUST PROCESS SUBEVENT_CODE...
    64: 'Physical Link Complete',
    65: 'Channel Selected',
    66: 'Disconnection Physical Link Complete',
    67: 'Physical Link Loss Early Warning',
    68: 'Physical Link Recovery',
    69: 'Logical Link Complete',
    70: 'Disconnection Logical Link Complete',
    71: 'Flow Spec Modify Complete',
    72: 'Number Of Completed Data Blocks',
    73: 'AMP Start Test',
    74: 'AMP Test End',
    75: 'AMP Receiver Report',
    76: 'Short_ Range_ Mode_ Change_Complete',
    77: 'AMP_Status_Change',
    78: 'Triggered Clock Capture',
    79: 'Synchronization Train Complete',
    80: 'Synchronization Train Received',
    81: 'Connectionless Slave Broadcast Receive',
    82: 'Connectionless Slave Broadcast Timeout',
    83: 'Truncated Page Complete',
    84: 'Slave Page Response Timeout',
    85: 'Connectionless Slave Broadcast Channel Map Change',
    86: 'Inquiry Response Notification',
    87: 'Authenticated Payload Timeout Expired',
    88: 'SAMStatusChange'
}

event_parameters = {
    'Inquiry Complete': {'Status': 8},
    'Inquiry Result': {'Num_Responses': 8,
                       'BD_ADDR': -48,
                       'Page_Scan_Repetition_Mode': 0,
                       'Reserved1': -8,
                       'Reserved2': -8,
                       'Class_of_Device': -24,
                       'Clock_Offset': -16
                       },
    'Connection Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'BD_ADDR': 48,
        'Link_Type': 8,
        'Encryption_Enabled': 8
    },
    'Connection Request': {
        'BD_ADDR': 8,
        'Class_of_Device': 24,
        'Link_Type': 8
    },
    'Disconnection Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Reason': 8
    },
    'Authentication Complete': {
        'Status': 8,
        'Connection_Handle': 16
    },
    'Remote Name Request Complete': {
        'Status': 8,
        'BD_ADDR': 48,
        'Remote_Name': 1984
    },
    'Encryption Change': {
        'Status': 8,
        'Connection_Handle': 16,
        'Encryption_Enabled': 8
    },
    'Change Connection Link Key Complete': {
        'Status': 8,
        'Connection_Handle': 16
    },
    'Master Link Key Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Key_Flag': 8
    },
    'Read Remote Supported Features Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'LMP_Features': 64
    },
    'Read Remote Version Information Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Version': 8,
        'Manufacturer_Name': 16,
        'Subversion': 16
    },
    'QoS Setup Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Flag': 8,
        'Service_Type': 8,
        'Token_Rate': 32,
        'Peak_Bandwidth': 32,
        'Latency': 32,
        'Delay_Variation': 32
    },
    'Command Complete': {
        'Num_HCI_Command_Packets': 8,
        'Command_Opcode': 16,
        'Return_Parameters': -2  # TODO SIZE DEPEND ON COMMAND
    },
    'Command Status': {
        'Status': 8,
        'Num_HCI_Command_Packets': 8,
        'Command_Opcode': 16
    },
    'Hardware Error': {
        'Hardware_Code': 8
    },
    'Flush Occurred': {
        'Handle': 16
    },
    'Role Change': {
        'Status': 8,
        'BD_ADDR': 48,
        'New_Role': 8
    },
    'Number Of Completed Packets': {
        'Number_of_Handles': 8,
        'Connection_of_Handle': -16,
        'HC_Num_Of_Completed_Packets': -16
    },
    'Mode Change': {
        'Status': 8,
        'Connection_Handle': 16,
        'Current_Mode': 8,
        'Interval': 16
    },
    'Return Link Keys': {
        'Num_Keys': 8,
        'BD_ADDR': -48,
        'Link_Key': -128
    },
    'PIN Code Request': {
        'BD_ADDR': 48
    },
    'Link Key Request': {
        'BD_ADDR': 48
    },
    'Link Key Notification': {
        'BD_ADDR': 48,
        'Link_Key': 128,
        'Key_Type': 8
    },
    'Loopback Command': {
        'HCI_Command_Packet': -2  # TODO Depend on command
    },
    'Data Buffer Overflow': {
        'Link_type': 8
    },
    'Max Slots Change': {
        'Connection': 16,
        'LMP_Max_Slots': 8
    },
    'Read Clock Offset Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Clock_Offset': 16
    },
    'Connection Packet Type Changed': {
        'Status': 8,
        'Connection_Handle': 16,
        'Packet_Type': 16
    },
    'QoS Violation': {
        'Handle': 16
    },
    'Page Scan Repetition Mode Change': {
        'BD_ADDR': 48,
        'Page_Scan_Repetition_Mode': 8
    },
    'Flow Specification Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Flags': 8,
        'Flow_direction': 8,
        'Service_Type': 8,
        'Token Rate': 32,
        'Token Bucket Size': 32,
        'Peak_Bandwidth': 32,
        'Access Latency': 32
    },
    'Inquiry Result with RSSI': {
        'Num_Responses': 8,
        'BD_ADDR': -48,
        'Page_Scan_Repetition_Mode': 0,
        'Reserved': -8,
        'Class_of_Device': -24,
        'Clock_Offset': -16,
        'RSS': -8
    },
    'Read Remote Extended Features Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Page Number': 8,
        'Maximum Page Number': 8,
        'Extended_LMP_Feature': 64
    },
    'Synchronous Connection Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'BD_ADDR': 48,
        'Link_Type': 8,
        'Transmission_Interval': 8,
        'Retransmission window': 8,
        'Rx_Packet_Length': 16,
        'Tx_Packet_Length': 16,
        'Air Mode': 8
    },
    'Synchronous Connection Changed': {
        'Status': 8,
        'Connection_Handle': 16,
        'Transmission_Interval': 8,
        'Retransmission window': 8,
        'Rx_Packet_Length': 16,
        'Tx_Packet_Length': 16
    },
    'Sniff Subrating': {
        'Status': 8,
        'Connection_Handle': 16,
        'Maximum_Transmit_Latency': 16,
        'Maximum_Receive_Latency': 16,
        'Minimum_Remote_Timeout': 16,
        'Minimum_Local_Timeout': 16
    },
    'Extended Inquiry Result': {
        'Num_Responses': 8,
        'BD_ADDR': 48,
        'Page_Scan_Repetition_Mode': 8,
        'Reserved': 8,
        'Class_of_Device': 24,
        'Clock_Offset': 24,
        'RSSI': 8
    },
    'Encryption Key Refresh Complete': {
        'Status': 8,
        'Connection_Handle': 16
    },
    'IO Capability Request': {
        'BD_ADDR': 48
    },
    'IO Capability Response': {
        'BD_ADDR': 48,
        'IO_Capbility': 8,
        'OOB_Data_Present': 8,
        'Authentication_Requirement': 8
    },
    'User Confirmation Request': {
        'BD_ADDR': 48,
        'Numeric_Value': 32
    },
    'User Passkey Request': {
        'BD_ADDR': 48
    },
    'Remote OOB Data Request': {
        'BD_ADDR': 48
    },
    'Simple Pairing Complete': {
        'Status': 8,
        'BD_ADDR': 48
    },
    'Link Supervision Timeout Changed': {
        'Connection_Handle': 16,
        'Link_Supervision_Timeout': 16
    },
    'Enhanced Flush Complete': {
        'Handle': 16
    },
    'User Passkey Notification': {
        'BD_ADDR': 48,
        'Passkey': 32
    },
    'Keypress Notification': {
        'BD_ADDR': 48,
        'Notification_Type': 8
    },
    'Remote Host Supported Features Notification': {
        'BD_ADDR': 48,
        'Host_Supported_Feature': 48
    },
    'LE': {},  # LE, MUST PROCESS SUBEVENT_CODE...
    'Physical Link Complete': {
        'Status': 8,
        'Physical_Link_Handle': 8
    },
    'Channel Selected': {
        'Physical_Link_Handle': 8
    },
    'Disconnection Physical Link Complete': {
        'Status': 8,
        'Physical_Link_Handle': 8,
        'Reason': 8
    },
    'Physical Link Loss Early Warning': {
        'Physical_Link_Handle': 8,
        'Link_Loss_Reason': 8
    },
    'Physical Link Recovery': {
        'Physical_Link_Handle': 8
    },
    'Logical Link Complete': {
        'Status': 8,
        'Logical_Link_Handle': 16,
        'Physical_Link_Handle': 8,
        'TX_Flow_Spec_ID': 8
    },
    'Disconnection Logical Link Complete': {
        'Status': 8,
        'Logical_Link_Handle': 16,
        'Reason': 8
    },
    'Flow Spec Modify Complete': {
        'Status': 8,
        'Handle': 16
    },
    'Number Of Completed Data Blocks': {
        'Total_Num_Data_Blocks': 16,
        'Num_of_Handles': 8,
        'Handle': -16,
        'Num_Of_Completed_Packets': -16,
        'Num_Of_Completed_Blocks': -16
    },
    'AMP Start Test': {
        'Status': 8,
        'Test Scenario': 8
    },
    'AMP Test End': {
        'Status': 8,
        'Test Scenario': 8
    },
    'AMP Receiver Report': {  # TODO 此項比較不一樣
        'Controller_Type': 8,
        'Reason': 8,
        'Event_type': 8,
        'Number_Of_Frames': 16,
        'Number_Of_Error_Frames': 16,
        'Number_Of_Bits': 32,
        'Number_Of_Error_Bits': 32
    },
    'Short_Range_ Mode_Change_Complete': {
        'Status': 8,
        'Physical_Link_Handle': 8,
        'Short_Range_Mode_State': 8
    },
    'AMP_Status_Change': {
        'Status': 8,
        'AMP_Status': 8
    },
    'Triggered Clock Capture': {
        'Connection_Handle': 16,
        'Which_Clock': 8,
        'Clock': 32,
        'Slot_Offset': 16
    },
    'Synchronization Train Complete': {
        'Status': 8
    },
    'Synchronization Train Received': {
        'Status': 8,
        'BD_ADDR': 48,
        'Clock_Offset': 32,
        'AFH_Channel_Map': 80,
        'LT_ADDR': 8,
        'Next_Broadcast_Instant': 32,
        'Connectionless_Slave_Broadcast_Interval': 16,
        'Service_Data': 8
    },
    'Connectionless Slave Broadcast Receive': {
        'BD_ADDR': 48,
        'LT_ADDR': 8,
        'CLK': 32,
        'Offset': 32,
        'Receive Status': 8,
        'Fragment': 8,
        'Data_Length': 8,
        'Data': -2  # TODO DATA_LENGTH OCTETS
    },
    'Connectionless Slave Broadcast Timeout': {
        'BD_ADDR': 48,
        'LT_ADDR': 8
    },
    'Truncated Page Complete': {
        'Status': 8,
        'BD_ADDR': 48
    },
    'Slave Page Response Timeout': {},
    'Connectionless Slave Broadcast Channel Map Change': {
        'Channel_Map': 80
    },
    'Inquiry Response Notification': {
        'LAP': 24,
        'RSSI': 8
    },
    'Authenticated Payload Timeout Expired': {
        'Connection_Handle': 16
    },
    'SAMStatusChange': {
        'Connection_Handle': 16,
        'Local_SAM_Index': 8,
        'Local_SAM_TX_Availability': 8,
        'Local_SAM_RX_Availability': 8,
        'Remote_SAM_Index': 8,
        'Remote_SAM_TX_Availability': 8,
        'Remote_SAM_RX_Availability': 8
    }
}
