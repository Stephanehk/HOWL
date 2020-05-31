from pyAudioAnalysis import audioTrainTest as aT

coyote_data_path = "/Users/2020shatgiskessell/Downloads/coyote_howl_dataset/macaulay_library_audio/split_audio_coyote"
not_coyote_data_path = "/Users/2020shatgiskessell/Downloads/coyote_howl_dataset/macaulay_library_audio/split_audio_bg"

aT.extract_features_and_train([coyote_data_path,not_coyote_data_path], 1.0, 1.0, aT.shortTermWindow, aT.shortTermStep, "svm", "svmSMtemp", False)





# import librosa
# import os
# from scipy.fftpack import fft
#
#
# failures = 0
# for filename in os.listdir("/Users/2020shatgiskessell/Downloads/coyote_howl_dataset/macaulay_library_audio/split_audio_coyote/"):
#     try:
#         x, sample_rate = librosa.load(filename, sr=None)
#     except FileNotFoundError:
#         pass
#
#     # #train fft
#     # X = fft(x, n_fft)
#     # X_magnitude, X_phase = librosa.magphase(X)
#     # X_magnitude_db = librosa.amplitude_to_db(X_magnitude)
#     # # duration = librosa.get_duration(y=clip, sr=sample_rate)
#     # # clip = clip[:44,100*duration]
#
# #perform short time fourier transformation (converts audio in time domain to frequency domain)
