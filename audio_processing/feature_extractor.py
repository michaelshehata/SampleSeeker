import librosa
import numpy as np

def extract_tempo_and_key(path, sr=22050):
    # load audio
    y, sr = librosa.load(path, sr=sr, mono=True)
    # BPM
    tempo, beats = librosa.beat.beat_track(y=y, sr=sr)
    # Chromagram for key estimation
    chroma = librosa.feature.chroma_cqt(y=y, sr=sr)
    # average chroma vector
    chroma_mean = np.mean(chroma, axis=1)
    # map index to pitch class
    pitch_classes = ['C','C#','D','D#','E','F','F#','G','G#','A','A#','B']
    # pick strongest pitch class
    key = pitch_classes[np.argmax(chroma_mean)]
    return round(tempo,1), key
