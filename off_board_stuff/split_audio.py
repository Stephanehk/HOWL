from pydub import AudioSegment
sound = AudioSegment.from_file("/Users/2020shatgiskessell/Downloads/coyote_howl_dataset/macaulay_library_audio/raw_audio/nature_sounds.wav")

# halfway_point = len(sound) // 2
# first_half = sound[:halfway_point]

# create a new file "first_half.mp3":
count = 0
for i in range (1,50,1):
    print ("saving file: " + str(count))
    sound_clip = sound[i*1000:(i+3)*1000]
    sound_clip+=10
    sound_clip.export("/Users/2020shatgiskessell/Downloads/coyote_howl_dataset/macaulay_library_audio/split_audio_bg/sound" + str(count) + ".wav", format="wav")
    count+=1

for j in range (50,100,2):
    print ("saving file: " + str(count))
    sound_clip = sound[j*1000:(j+3)*1000]
    sound_clip+=10
    sound_clip.export("/Users/2020shatgiskessell/Downloads/coyote_howl_dataset/macaulay_library_audio/split_audio_bg/sound" + str(count) + ".wav", format="wav")
    count+=1
