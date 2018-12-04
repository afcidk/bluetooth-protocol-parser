'''
pcap format:
    Global header | Packet Header | Packet Data | Packet Header | Packet Data | ....
'''

'''
packet header format:
typedef struct pcaprec_hdr_s {
    guint32 ts_sec;     /* timestamp seconds */
    guint32 ts_usec;    /* timestamp microseconds */
    guint32 incl_len    /* number of octets of packet */
    guint32 orig_len    /* actual length of packet */
} pcaprec_hdr_t;
'''
from field_spec import header_field, data_field
from field_spec import parse_field
from field_spec import int_from_bits
from sbc_codec  import extract_audio
import os

# temporary input for testing
print(os.listdir('../pcap_files'))
selection = os.listdir('../pcap_files')
select = int(input('Enter selection: ').strip())
FILE = '../pcap_files/' + selection[select]
print('Parsing file: ' + FILE)

with open(FILE, 'rb') as f:
    data = f.read()

global_header = data[:24]
data = data[24:] # remove global header

packets = list()
tot_len = len(data)

cc = 1
try:
    while data: 
        print('Data: {}, Progress: {}'.format(cc, len(data)/tot_len), end='\r')
        cc += 1
        # parse packet header
        pkt, data = parse_field(header_field, data)

    # parse packet data and the remaining data
        try:
            packet_data, data = parse_field(data_field[pkt['packet_type']], data)
        except KeyboardInterrupt as e:
            pass

        pkt.update({'data': packet_data})
        #unparsed_data = data[:packet_data['Length']]
        #pkt.update({'unparsed_data': unparsed_data})

        data = data[packet_data['Length']:]

        # discard packet data
        pkt['incl_len'] -= 4
        pkt['orig_len'] -= 4
        packets.append(pkt)
        
        '''
        if(len(packets) >= 28):
            break
        '''
except KeyboardInterrupt:
    pass

########Print parsed packets (Uncomment to print)##############
extract_audio(packets)
nn = 1

for packet in packets:
    print('{} {}'.format(nn, packet))
    nn += 1
    input()
print()
print('packet numbers: {}'.format(len(packets)))
