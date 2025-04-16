import numpy as np

# cd audio at 44,100 hz and 16 bits per sample
SAMPLES_S = 44_100
BITS_SAMPLE = 16

# wave header constants
CHUNK_ID = b'RIFF'
FORMAT = b'WAVE'
SUBCHUNK_1_ID = b'fmt '
SUBCHUNK_2_ID = b'data'

# PCM constants
SUBCHUNK_1_SIZE = (16).to_bytes(4, byteorder='little')
AUDIO_FORMAT = (1).to_bytes(2, byteorder='little')

def create_pcm(frequency):
    ang_freq = 2*np.pi*frequency
    x_vals = np.arange(SAMPLES_S)
    y_vals = 32767 * .3 * np.sin(ang_freq * x_vals / SAMPLES_S)
    return np.int16(y_vals)

def new_wav(channels, filename, *args):
    seconds = len(args)

    chunk_size = (int(36 + (seconds * SAMPLES_S * BITS_SAMPLE/8))).to_bytes(4, 'little')
    num_channels = (channels).to_bytes(2, byteorder='little')
    sample_rate = (SAMPLES_S).to_bytes(4, byteorder='little')
    byte_rate = (int(SAMPLES_S * channels * BITS_SAMPLE/8)).to_bytes(4, byteorder='little')
    block_align = (int(channels * BITS_SAMPLE/8)).to_bytes(2, byteorder='little')
    bits_per_sample = (BITS_SAMPLE).to_bytes(2, byteorder='little')
    subchunk_2_size = (int(seconds * SAMPLES_S * BITS_SAMPLE/8)).to_bytes(4, byteorder='little')

    my_pcm = []

    for arg in args:
        my_pcm.append(create_pcm(arg))

    mat = np.array(my_pcm)

    with open(f'{filename}.wav', 'wb') as fo:
        fo.write(
            CHUNK_ID +
            chunk_size +
            FORMAT +
            SUBCHUNK_1_ID +
            SUBCHUNK_1_SIZE +
            AUDIO_FORMAT +
            num_channels +
            sample_rate +
            byte_rate +
            block_align +
            bits_per_sample +
            SUBCHUNK_2_ID +
            subchunk_2_size +
            mat.tobytes()
        )

new_wav(1,'mysong', 200, 252, 212, 400, 150, 360)
