import os
import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display

# Plot settings
plt.rcParams['text.color'] = '#FFFFFF'
plt.rcParams['axes.labelcolor'] = '#FFFFFF'
plt.rcParams['xtick.color'] = '#FFFFFF'
plt.rcParams['ytick.color'] = '#FFFFFF'

def dis_mfccs(y, sr, save_path):
    # Extract MFCCs
    mfccs = librosa.feature.mfcc(y=y, sr=sr)
    librosa.display.specshow(mfccs, x_axis='time', cmap='magma') # cmap to change color

    # Title and labels
    plt.colorbar(format='%+2.0f dB')
    plt.title('MFCCs')
    plt.savefig(save_path, facecolor='#1F1B24')
    plt.close()

def dis_spectrogram(y, sr, save_path):
    # Compute spectrogram
    S = librosa.stft(y)
    S_db = librosa.amplitude_to_db(np.abs(S), ref=np.max)

    # Display the spectrogram
    librosa.display.specshow(S_db, sr=sr, x_axis='time', y_axis='log', cmap='twilight', alpha=0.5)

    # Title and labels
    plt.title('Spectrogram (Time-Frequency Energy)', fontsize=14, fontweight='bold')
    plt.colorbar(format='%+2.0f dB', label='Amplitude (dB)')
    plt.tight_layout()
    plt.savefig(save_path, facecolor='#1F1B24')
    plt.close()


def dis_beatmarkers(y, sr, save_path):
    # Beat tracking
    tempo, beat_frames = librosa.beat.beat_track(y=y, sr=sr)
    beat_times = librosa.frames_to_time(beat_frames, sr=sr)

    # Add vertical lines at beat times
    for bt in beat_times:
        plt.axvline(x=bt, color='cyan', linestyle='--', alpha=0.8, linewidth=1) # '-', '--', '-.', ':',

    # Title and labels
    plt.title('Beat Markers', fontsize=14, fontweight='bold')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.savefig(save_path, facecolor='#1F1B24')
    plt.close()


def dis_waveform(y, sr, save_path):
    librosa.display.waveshow(y, sr=sr, color='cyan', alpha=0.8)

    # Title and labels
    plt.title('Waveform', fontsize=14, fontweight='bold')
    plt.xlabel('Time (seconds)')
    plt.ylabel('Amplitude')
    plt.tight_layout()
    plt.savefig(save_path, facecolor='#1F1B24')
    plt.close()


def dis_mel(y, sr, save_path):
    # Create the Mel filter bank
    n_fft = 2048  # Number of FFT components
    n_mels = 20  # Number of Mel bands
    fmin = 100
    fmax = 8000 # for focusing on low or high frequencies
    # mel_filter_bank = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)
    melfb = librosa.filters.mel(sr=sr, n_fft=n_fft, n_mels=n_mels)
    # Plot mel filter
    img = librosa.display.specshow(melfb, x_axis='linear') # 'log'

    # Title and labels
    plt.title('Mel Filter Bank')
    plt.xlabel('FFT Bin')
    plt.ylabel('Mel Filter Index')
    plt.colorbar(img, format="%+2.0f dB") 
    plt.tight_layout()
    plt.savefig(save_path, facecolor='#1F1B24')
    plt.close()


def load_audio(file_path):
    # y, array of amplitude vals of the audio waveform. each val represents a smaple
    # sr, sample rate is the Hz or samples per second audio was loaded at
    y, sr = librosa.load(file_path)
    duration = librosa.get_duration(y=y, sr=sr)
    return y, sr, duration

# Takes arguments from GUI-graphs.py then genertes and saves a graph image png
def make_graph(file_path, graph_type, output_folder="OutputGraphs"):
    y, sr, duration = load_audio(file_path)
    # Create filename and path to store generated graph
    output_path = os.path.join(output_folder, f"graph.png")

    # Call selected graph function
    if graph_type == "MFCC":
        dis_mfccs(y, sr, output_path)
    elif graph_type == "Spectrogram":
        dis_spectrogram(y, sr, output_path)
    elif graph_type == "Beat Markers":
        dis_beatmarkers(y, sr, output_path)
    elif graph_type == "Waveform":
        dis_waveform(y, sr, output_path)
    elif graph_type == "Mel":
        dis_mel(y, sr, output_path)
    else:
        raise ValueError(f"Unsupported graph type: {graph_type}")
        

#### Keep commented when using with GUI-graphs.py, will throw RuntimeError: 
#### Please destroy the QApplication singleton before creating a new QApplication instance
# def main():
#     audio_file = 'TestAudioFiles/phub_and.mp3'
#     y, sr, duration = load_audio(audio_file)

#     # # Some file info
#     # print(f"File: {audio_file}")
#     # print(f"Sample rate: {sr} Hz")
#     # print(f"Total samples: {len(y)}")
#     # print(f"Duration: {duration:.2f} s")

#     # Call functions here
#     dis_mfccs(y, sr, audio_file)


# if __name__ == '__main__':
#     main()