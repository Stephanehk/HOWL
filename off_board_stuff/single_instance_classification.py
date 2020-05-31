from pyAudioAnalysis import audioTrainTest as aT

out = aT.file_classification("/Users/2020shatgiskessell/Downloads/coyote_howl_dataset/macaulay_library_audio/split_audio_coyote/sound12.wav", "svmSMtemp","svm")
print (int(out[1][0]))
