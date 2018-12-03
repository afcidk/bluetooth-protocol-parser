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
    'Inquiry Complete': {'Status': 8, 'ORDER': ['Status']},
    'Inquiry Result': {
        'Num_Responses': 8,
        'BD_ADDR': -48,
        'Page_Scan_Repetition_Mode': 0,
        'Reserved1': -8,
        'Reserved2': -8,
        'Class_of_Device': -24,
        'Clock_Offset': -16,
        'ORDER': [
            'Num_Responses',
            'BD_ADDR',
            'Page_Scan_Repetition_Mode',
            'Reserved1',
            'Reserved2',
            'Class_of_Device',
            'Clock_Offset',
        ]
    },
    'Connection Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'BD_ADDR': 48,
        'Link_Type': 8,
        'Encryption_Enabled': 8,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'BD_ADDR',
            'Link_Type',
            'Encryption_Enabled',
        ]
    },
    'Connection Request': {
        'BD_ADDR': 8,
        'Class_of_Device': 24,
        'Link_Type': 8,
        'ORDER': [
            'BD_ADDR',
            'Class_of_Device',
            'Link_Type',
        ]
    },
    'Disconnection Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Reason': 8,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Reason',
        ]
    },
    'Authentication Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'ORDER': [
            'Status',
            'Connection_Handle',
        ]
    },
    'Remote Name Request Complete': {
        'Status': 8,
        'BD_ADDR': 48,
        'Remote_Name': 1984,
        'ORDER': [
            'Status',
            'BD_ADDR',
            'Remote_Name',
        ]
    },
    'Encryption Change': {
        'Status': 8,
        'Connection_Handle': 16,
        'Encryption_Enabled': 8,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Encryption_Enabled',
        ]
    },
    'Change Connection Link Key Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'ORDER': [
            'Status',
            'Connection_Handle',
        ]
    },
    'Master Link Key Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Key_Flag': 8,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Key_Flag',
        ]
    },
    'Read Remote Supported Features Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'LMP_Features': 64,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'LMP_Features',
        ]
    },
    'Read Remote Version Information Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Version': 8,
        'Manufacturer_Name': 16,
        'Subversion': 16,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Version',
            'Manufacturer_Name',
            'Subversion',
        ]
    },
    'QoS Setup Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Flag': 8,
        'Service_Type': 8,
        'Token_Rate': 32,
        'Peak_Bandwidth': 32,
        'Latency': 32,
        'Delay_Variation': 32,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Flag',
            'Service_Type',
            'Token_Rate',
            'Peak_Bandwidth',
            'Latency',
            'Delay_Variation',
        ]
    },
    'Command Complete': {
        'Num_HCI_Command_Packets': 8,
        'Command_Opcode': 16,
        'Return_Parameters': -2,  # TODO SIZE DEPEND ON COMMAND
        'ORDER': [
            'Num_HCI_Command_Packets',
            'Command_Opcode',
            'Return_Parameters',  
        ]
    },
    'Command Status': {
        'Status': 8,
        'Num_HCI_Command_Packets': 8,
        'Command_Opcode': 16,
        'ORDER': [
            'Status',
            'Num_HCI_Command_Packets',
            'Command_Opcode',
        ]
    },
    'Hardware Error': {
        'Hardware_Code': 8,
        'ORDER': ['Hardware_Code']
    },
    'Flush Occurred': {
        'Handle': 16,
        'ORDER': ['Handle']
    },
    'Role Change': {
        'Status': 8,
        'BD_ADDR': 48,
        'New_Role': 8,
        'ORDER': [
            'Status',
            'BD_ADDR',
            'New_Role',
        ]
    },
    'Number Of Completed Packets': {
        'Number_of_Handles': 8,
        'Connection_of_Handle': -16,
        'HC_Num_Of_Completed_Packets': -16,
        'ORDER': [
            'Number_of_Handles',
            'Connection_of_Handle',
            'HC_Num_Of_Completed_Packets',
        ]
    },
    'Mode Change': {
        'Status': 8,
        'Connection_Handle': 16,
        'Current_Mode': 8,
        'Interval': 16,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Current_Mode',
            'Interval',
        ]
    },
    'Return Link Keys': {
        'Num_Keys': 8,
        'BD_ADDR': -48,
        'Link_Key': -128,
        'ORDER': [
            'Num_Keys',
            'BD_ADDR',
            'Link_Key',
        ]
    },
    'PIN Code Request': {
        'BD_ADDR': 48,
        'ORDER': ['BD_ADDR']
    },
    'Link Key Request': {
        'BD_ADDR': 48,
        'ORDER': ['BD_ADDR']
    },
    'Link Key Notification': {
        'BD_ADDR': 48,
        'Link_Key': 128,
        'Key_Type': 8,
        'ORDER': [
            'BD_ADDR',
            'Link_Key',
            'Key_Type',
        ]
    },
    'Loopback Command': {
        'HCI_Command_Packet': -2,  # TODO Depend on command
        'ORDER': ['HCI_Command_Packet']
    },
    'Data Buffer Overflow': {
        'Link_type': 8,
        'ORDER': ['Link_type']
    },
    'Max Slots Change': {
        'Connection': 16,
        'LMP_Max_Slots': 8,
        'ORDER': [
            'Connection',
            'LMP_Max_Slots',
        ]
    },
    'Read Clock Offset Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Clock_Offset': 16,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Clock_Offset',
        ]
    },
    'Connection Packet Type Changed': {
        'Status': 8,
        'Connection_Handle': 16,
        'Packet_Type': 16,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Packet_Type',
        ]
    },
    'QoS Violation': {
        'Handle': 16,
        'ORDER': ['Handle']
    },
    'Page Scan Repetition Mode Change': {
        'BD_ADDR': 48,
        'Page_Scan_Repetition_Mode': 8,
        'ORDER': [
            'BD_ADDR',
            'Page_Scan_Repetition_Mode',
        ]
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
        'Access Latency': 32,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Flags',
            'Flow_direction',
            'Service_Type',
            'Token Rate',
            'Token Bucket Size',
            'Peak_Bandwidth',
            'Access Latency',
        ]
    },
    'Inquiry Result with RSSI': {
        'Num_Responses': 8,
        'BD_ADDR': -48,
        'Page_Scan_Repetition_Mode': 0,
        'Reserved': -8,
        'Class_of_Device': -24,
        'Clock_Offset': -16,
        'RSS': -8,
        'ORDER': [
            'Num_Responses',
            'BD_ADDR',
            'Page_Scan_Repetition_Mode',
            'Reserved',
            'Class_of_Device',
            'Clock_Offset',
            'RSS',
        ]
    },
    'Read Remote Extended Features Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'Page Number': 8,
        'Maximum Page Number': 8,
        'Extended_LMP_Feature': 64,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Page Number',
            'Maximum Page Number',
            'Extended_LMP_Feature',
        ]
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
        'Air Mode': 8,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'BD_ADDR',
            'Link_Type',
            'Transmission_Interval',
            'Retransmission window',
            'Rx_Packet_Length',
            'Tx_Packet_Length',
            'Air Mode',
        ]
    },
    'Synchronous Connection Changed': {
        'Status': 8,
        'Connection_Handle': 16,
        'Transmission_Interval': 8,
        'Retransmission window': 8,
        'Rx_Packet_Length': 16,
        'Tx_Packet_Length': 16,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Transmission_Interval',
            'Retransmission window',
            'Rx_Packet_Length',
            'Tx_Packet_Length',
        ]
    },
    'Sniff Subrating': {
        'Status': 8,
        'Connection_Handle': 16,
        'Maximum_Transmit_Latency': 16,
        'Maximum_Receive_Latency': 16,
        'Minimum_Remote_Timeout': 16,
        'Minimum_Local_Timeout': 16,
        'ORDER': [
            'Status',
            'Connection_Handle',
            'Maximum_Transmit_Latency',
            'Maximum_Receive_Latency',
            'Minimum_Remote_Timeout',
            'Minimum_Local_Timeout',
        ]
    },
    'Extended Inquiry Result': {
        'Num_Responses': 8,
        'BD_ADDR': 48,
        'Page_Scan_Repetition_Mode': 8,
        'Reserved': 8,
        'Class_of_Device': 24,
        'Clock_Offset': 24,
        'RSSI': 8,
        'ORDER': [
            'Num_Responses',
            'BD_ADDR',
            'Page_Scan_Repetition_Mode',
            'Reserved',
            'Class_of_Device',
            'Clock_Offset',
            'RSSI',
        ]
    },
    'Encryption Key Refresh Complete': {
        'Status': 8,
        'Connection_Handle': 16,
        'ORDER': [
            'Status',
            'Connection_Handle',
        ]

    },
    'IO Capability Request': {
        'BD_ADDR': 48,
        'ORDER': 'BD_ADDR'
    },
    'IO Capability Response': {
        'BD_ADDR': 48,
        'IO_Capbility': 8,
        'OOB_Data_Present': 8,
        'Authentication_Requirement': 8,
        'ORDER': [
            'BD_ADDR',
            'IO_Capbility',
            'OOB_Data_Present',
            'Authentication_Requirement',
        ]
    },
    'User Confirmation Request': {
        'BD_ADDR': 48,
        'Numeric_Value': 32,
        'ORDER': [
            'BD_ADDR',
            'Numeric_Value'
        ]
    },
    'User Passkey Request': {
        'BD_ADDR': 48,
        'ORDER': ['BD_ADDR']
    },
    'Remote OOB Data Request': {
        'BD_ADDR': 48,
        'ORDER': ['BD_ADDR']
    },
    'Simple Pairing Complete': {
        'Status': 8,
        'BD_ADDR': 48,
        'ORDER': [
            'Status',
            'BD_ADDR',
        ]
    },
    'Link Supervision Timeout Changed': {
        'Connection_Handle': 16,
        'Link_Supervision_Timeout': 16,
        'ORDER': [
            'Connection_Handle',
            'Link_Supervision_Timeout',
        ]
    },
    'Enhanced Flush Complete': {
        'Handle': 16,
        'ORDER': ['Handle']
    },
    'User Passkey Notification': {
        'BD_ADDR': 48,
        'Passkey': 32,
        'ORDER': [
            'BD_ADDR',
            'Passkey'
        ]
    },
    'Keypress Notification': {
        'BD_ADDR': 48,
        'Notification_Type': 8,
        'ORDER': [
            'BD_ADDR',
            'Notification_Type',
        ]
    },
    'Remote Host Supported Features Notification': {
        'BD_ADDR': 48,
        'Host_Supported_Feature': 48,
        'ORDER': [
            'BD_ADDR',
            'Host_Supported_Feature',
        ]
    },
    'LE': {'ORDER': []},  # LE, MUST PROCESS SUBEVENT_CODE...
    'Physical Link Complete': {
        'Status': 8,
        'Physical_Link_Handle': 8,
        'ORDER': [
            'Status',
            'Physical_Link_Handle',
        ]
    },
    'Channel Selected': {
        'Physical_Link_Handle': 8,
        'ORDER': ['Physical_Link_Handle']
    },
    'Disconnection Physical Link Complete': {
        'Status': 8,
        'Physical_Link_Handle': 8,
        'Reason': 8,
        'ORDER': [
            'Status',
            'Physical_Link_Handle',
            'Reason',
        ]
    },
    'Physical Link Loss Early Warning': {
        'Physical_Link_Handle': 8,
        'Link_Loss_Reason': 8,
        'ORDER': [
            'Physical_Link_Handle',
            'Link_Loss_Reason',
        ]

    },
    'Physical Link Recovery': {
        'Physical_Link_Handle': 8,
        'ORDER': ['Physical_Link_Handle']
    },
    'Logical Link Complete': {
        'Status': 8,
        'Logical_Link_Handle': 16,
        'Physical_Link_Handle': 8,
        'TX_Flow_Spec_ID': 8,
        'ORDER': [
            'Status',
            'Logical_Link_Handle',
            'Physical_Link_Handle',
            'TX_Flow_Spec_ID'
        ]
    },
    'Disconnection Logical Link Complete': {
        'Status': 8,
        'Logical_Link_Handle': 16,
        'Reason': 8,
        'ORDER': [
            'Status',
            'Logical_Link_Handle',
            'Reason',
        ]
    },
    'Flow Spec Modify Complete': {
        'Status': 8,
        'Handle': 16,
        'ORDER': [
            'Status',
            'Handle',
        ]
    },
    'Number Of Completed Data Blocks': {
        'Total_Num_Data_Blocks': 16,
        'Num_of_Handles': 8,
        'Handle': -16,
        'Num_Of_Completed_Packets': -16,
        'Num_Of_Completed_Blocks': -16,
        'ORDER': [
            'Total_Num_Data_Blocks',
            'Num_of_Handles',
            'Handle',
            'Num_Of_Completed_Packets',
            'Num_Of_Completed_Blocks'
        ]
    },
    'AMP Start Test': {
        'Status': 8,
        'Test Scenario': 8,
        'ORDER': [
            'Status',
            'Test Scenario',
        ]
    },
    'AMP Test End': {
        'Status': 8,
        'Test Scenario': 8,
        'ORDER': [
            'Status',
            'Test Scenario',
        ]
    },
    'AMP Receiver Report': {  # TODO 此項比較不一樣
        'Controller_Type': 8,
        'Reason': 8,
        'Event_type': 8,
        'Number_Of_Frames': 16,
        'Number_Of_Error_Frames': 16,
        'Number_Of_Bits': 32,
        'Number_Of_Error_Bits': 32,
        'ORDER': [
            'Controller_Type',
            'Reason',
            'Event_type',
            'Number_Of_Frames',
            'Number_Of_Error_Frames',
            'Number_Of_Bits',
            'Number_Of_Error_Bits',
        ]
    },
    'Short_Range_ Mode_Change_Complete': {
        'Status': 8,
        'Physical_Link_Handle': 8,
        'Short_Range_Mode_State': 8,
        'ORDER': [
            'Status',
            'Physical_Link_Handle',
            'Short_Range_Mode_State',
        ]
    },
    'AMP_Status_Change': {
        'Status': 8,
        'AMP_Status': 8,
        'ORDER': [
            'Status',
            'AMP_Status',
        ]
    },
    'Triggered Clock Capture': {
        'Connection_Handle': 16,
        'Which_Clock': 8,
        'Clock': 32,
        'Slot_Offset': 16,
        'ORDER': [
            'Connection_Handle',
            'Which_Clock',
            'Clock',
            'Slot_Offset',
        ]
    },
    'Synchronization Train Complete': {
        'Status': 8,
        'ORDER': ['Status']
    },
    'Synchronization Train Received': {
        'Status': 8,
        'BD_ADDR': 48,
        'Clock_Offset': 32,
        'AFH_Channel_Map': 80,
        'LT_ADDR': 8,
        'Next_Broadcast_Instant': 32,
        'Connectionless_Slave_Broadcast_Interval': 16,
        'Service_Data': 8,
        'ORDER': [
            'Status',
            'BD_ADDR',
            'Clock_Offset',
            'AFH_Channel_Map',
            'LT_ADDR',
            'Next_Broadcast_Instant',
            'Connectionless_Slave_Broadcast_Interval',
            'Service_Data',
        ]
    },
    'Connectionless Slave Broadcast Receive': {
        'BD_ADDR': 48,
        'LT_ADDR': 8,
        'CLK': 32,
        'Offset': 32,
        'Receive Status': 8,
        'Fragment': 8,
        'Data_Length': 8,
        'Data': -2,  # TODO DATA_LENGTH OCTETS
        'ORDER': [
            'BD_ADDR',
            'LT_ADDR',
            'CLK',
            'Offset',
            'Receive Status',
            'Fragment',
            'Data_Length',
            'Data',
        ]
    },
    'Connectionless Slave Broadcast Timeout': {
        'BD_ADDR': 48,
        'LT_ADDR': 8,
        'ORDER': [
            'BD_ADDR',
            'LT_ADDR',
        ]
    },
    'Truncated Page Complete': {
        'Status': 8,
        'BD_ADDR': 48,
        'ORDER': [
            'Status',
            'BD_ADDR',
        ]
    },
    'Slave Page Response Timeout': {'ORDER': []},
    'Connectionless Slave Broadcast Channel Map Change': {
        'Channel_Map': 80,
        'ORDER': [
            'Channel_Map'
        ]
    },
    'Inquiry Response Notification': {
        'LAP': 24,
        'RSSI': 8,
        'ORDER': [
            'LAP',
            'RSSI',
        ]
    },
    'Authenticated Payload Timeout Expired': {
        'Connection_Handle': 16,
        'ORDER': [
            'Connection_Handle'
        ]
    },
    'SAMStatusChange': {
        'Connection_Handle': 16,
        'Local_SAM_Index': 8,
        'Local_SAM_TX_Availability': 8,
        'Local_SAM_RX_Availability': 8,
        'Remote_SAM_Index': 8,
        'Remote_SAM_TX_Availability': 8,
        'Remote_SAM_RX_Availability': 8,
        'ORDER': [
            'Connection_Handle',
            'Local_SAM_Index',
            'Local_SAM_TX_Availability',
            'Local_SAM_RX_Availability',
            'Remote_SAM_Index',
            'Remote_SAM_TX_Availability',
            'Remote_SAM_RX_Availability',
        ]
    }
}
