from decoder.sbc_decoder import sbc2wav
# SBC Codec -> .sbc
def ouput_sbc_file(packets) :
	f = open('../data/output.sbc','wb')
	for packet in packets :
		if ('acl_data' in packet['data'] and 
			'AVDTP' in packet['data']['acl_data'] and
			'SBC_Codec' in packet['data']['acl_data']['AVDTP'] and
			'Frames' in packet['data']['acl_data']['AVDTP']['SBC_Codec']):
			frm = packet['data']['acl_data']['AVDTP']['SBC_Codec']['Frames']
			f.write(frm)
	f.close()
# .sbc -> .wav
def ouput_wav_file() :
	sbc2wav()			