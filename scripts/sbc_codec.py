from decoder.sbc_decoder import sbc2wav
'''
SBC frame -> .sbc
'''
def ouput_sbc_file(packets) :
	isAudio = False
	f = open('../data/output.sbc','wb')
	for packet in packets :
		if ('acl_data' in packet['data'] and 
			'AVDTP' in packet['data']['acl_data'] and
			'SBC_Codec' in packet['data']['acl_data']['AVDTP'] and
			'Frames' in packet['data']['acl_data']['AVDTP']['SBC_Codec']):
			isAudio = True
			frm = packet['data']['acl_data']['AVDTP']['SBC_Codec']['Frames']
			f.write(frm)
	f.close()
	return isAudio
'''
.sbc -> .wav
'''
def ouput_wav_file() :
	sbc2wav()

'''
if not audio file , do nothing
else output .sbc and .wav
'''
def extract_audio(packets):
	if ouput_sbc_file(packets) :
		print ()
		print ("output file: ../data/output.sbc")
		ouput_wav_file()