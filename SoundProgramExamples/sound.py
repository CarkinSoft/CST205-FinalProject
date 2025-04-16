import numpy as np
from scipy.io.wavfile import write

# samples per second
samples_s = 44100

# frequence of the sine wave, Concert C
freq_hz = 260.0

# duration
duration_s = 5.0

# an array from 0 to 220,499
# https://docs.scipy.org/doc/numpy-1.13.0/reference/generated/numpy.arange.html
sample_nums = np.arange(duration_s * samples_s)

# see Digital Sound handout http://bit.ly/2zXGGK6
waveform = np.sin(2 * np.pi * sample_nums * freq_hz / samples_s)

# reduce amplitude
waveform_quiet = waveform * 0.3

# https://docs.scipy.org/doc/numpy-1.10.4/user/basics.types.html
# http://soundfile.sapp.org/doc/WaveFormat/
waveform_integers = np.int16(waveform_quiet * 32767)

# write to file using scipy.io.wavfile
# https://docs.scipy.org/doc/scipy-0.19.1/reference/generated/scipy.io.wavfile.write.html
write('mine.wav', samples_s, waveform_integers)