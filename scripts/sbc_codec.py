from decoder.sbc_decoder import sbc2wav
'''
SBC frame -> .sbc
'''
def output_sbc_file(packets) :
	isAudio = False
#	f = open('../data/output.sbc','wb')
	for packet in packets :
		if ('acl_data' in packet['data'] and 
			'Dynamic allocated' in packet['data']['acl_data'] and
			'AVDTP' in packet['data']['acl_data']['Dynamic allocated'] and
			'SBC_Codec' in packet['data']['acl_data']['Dynamic allocated']['AVDTP'] and
			'Frames' in packet['data']['acl_data']['Dynamic allocated']['AVDTP']['SBC_Codec']):
			if not isAudio :
				f = open('../data/output.sbc','wb')
				isAudio = True
			frm = packet['data']['acl_data']['Dynamic allocated']['AVDTP']['SBC_Codec']['Frames']
			f.write(frm)
	if isAudio:
		f.close()
	return isAudio
'''
.sbc -> .wav
'''
def output_wav_file() :
	sbc2wav()

'''
if not audio file , do nothing
else output .sbc and .wav
'''
def extract_audio(packets):
	if output_sbc_file(packets) :
		print ()
		print ("output file: ../data/output.sbc")
		output_wav_file()