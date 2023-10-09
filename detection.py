"""
Provides some librosa functions
"""
# 註解/取消註解:ctrl + /
import librosa
import numpy as np

y0 , sr = librosa.load('./audio_spleeter_out/紳士/vocals.wav')
n_fft = 2048
S = librosa.stft(y0, n_fft=n_fft, hop_length=n_fft//2)
D = librosa.amplitude_to_db(np.abs(S), ref=np.max)
np.max(abs(D))

nonMuteSections = librosa.effects.split(y0, top_db = 20)
y = []

for sliced in nonMuteSections:
    y.extend(y0[sliced[0]:sliced[1]])


f0, voiced_flag, voiced_probabilities = librosa.pyin(
    y, frame_length=2048, fmin=librosa.note_to_hz('G2'), fmax=librosa.note_to_hz('C6'))  # 110~1046Hz

appear = []
midi_note = np.around(librosa.hz_to_midi(f0))
i = len(midi_note)-1

while i >= 0:
    if midi_note[i] != 'nan':
        is_a_note = True
        for t in range(3):
            if midi_note[i-t-1] != midi_note[i]:
                is_a_note = False
                break
        if is_a_note == True:
            appear.append(midi_note[i])
            i -= 5
        else:
            i -= 1
    
    
appear.sort()
# 5 index
print("average", librosa.midi_to_note(appear[(int)(len(appear)/2)]))
print("average high", librosa.midi_to_note(appear[(int)(3*len(appear)/4)]))
print("average low", librosa.midi_to_note(appear[(int)(len(appear)/4)]))
print("low", librosa.midi_to_note(appear[(int)(len(appear)/100)]))
print("high", librosa.midi_to_note(appear[(int)(98*len(appear)/100)]))
