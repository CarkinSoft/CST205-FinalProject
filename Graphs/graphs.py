import os
import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display

# plot settings
plt.rcParams['text.color'] = '#FFFFFF'
plt.rcParams['axes.labelcolor'] = '#FFFFFF'
plt.rcParams['xtick.color'] = '#FFFFFF'
plt.rcParams['ytick.color'] = '#FFFFFF'
plt.figure(figsize=(10, 4), facecolor='#1F1B24')

def dis_mfccs(y, sr):
    # Extract MFCCs
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    librosa.display.specshow(mfccs, x_axis='time', cmap='magma') # cmap to change color
    plt.colorbar(format='%+2.0f dB')
    plt.title('MFCCs')
    plt.show()

def dis_spectrogram(y, sr):
    # Compute spectrogram
    S = librosa.stft(y)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)

    # Display the spectrogram in the background 
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log', cmap='twilight', alpha=0.5)

    # Title and labels
    plt.title('Spectrogram (Time-Frequency Energy)', fontsize=16, fontweight='bold')
    plt.colorbar(format='%+2.0f dB', label='Amplitude (dB)')
    plt.tight_layout()
    plt.show()


def dis_beatmarkers(y, sr):
    # Beat tracking
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    # Add vertical lines at beat times
    for bt in beat_times:
        plt.axvline(x=bt, color='cyan', linestyle='--', alpha=0.8) # '-', '--', '-.', ':',

    # Title and labels
    plt.title('Beat Markers Only', fontsize=14, fontweight='bold')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()


def dis_waveform(y, sr):
    # Plot the waveform
    librosa.display.waveshow(y, sr=sr, color='cyan', alpha=0.8)

    # Title and labels
    plt.title('Waveform', fontsize=14, fontweight='bold')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.show()


def dis_mel(y, sr):
    # plot mel filter
    # Create the Mel filter bank
    n_fft = 2048  # Number of FFT components
    n_mels = 20  # Number of Mel bands
    fmin = 100
    fmax = 8000 # for focusing on low or high frequencies
    # mel_filter_bank = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)
    melfb = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)
    # Plot mel filter
    img = librosa.display.specshow(melfb, x_axis='linear') # 'log'
    plt.title('Mel Filter Bank')
    plt.xlabel('FFT Bin')
    plt.ylabel('Mel Filter Index')
    plt.colorbar(img, format="%+2.0f dB") 
    plt.tight_layout()
    plt.show()


def load_audio(file_path):
    # y, array of amplitude vals of the audio waveform. each val represents a smaple
    # sr, sample rate is the Hz or samples per second audio was loaded at
    y, sr = librosa.load(file_path)
    duration = librosa.get_duration(y=y, sr=sr)
    return y, sr, duration

def main():
    audio_file = 'TestAudioFiles/phub_and.mp3'
    y, sr, duration = load_audio(audio_file)

    # Some file info
    print(f"File: {audio_file}")
    print(f"Sample rate: {sr} Hz")
    print(f"Total samples: {len(y)}")
    print(f"Duration: {duration:.2f} s")

    # Call functions here
    dis_mfccs(y, sr)


if __name__ == '__main__':
    main()