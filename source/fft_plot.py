import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile

firstpiano = wavfile.read('sound_data/piano1_mono.wav')
secondpiano = wavfile.read('sound_data/piano2_mono.wav')
singletrumpet = np.loadtxt('sound_data/trumpet.csv', delimiter=',')
twotrumpets = np.loadtxt('sound_data/twotrumpetsAB.csv', delimiter=',')

firstpianofft = fft(firstpiano[1], n=len(firstpiano[1]), norm=None)
secondpianofft = fft(secondpiano[1], n=len(secondpiano[1]), norm=None)
singletrumpetfft = fft(singletrumpet, n=len(singletrumpet), norm=None)
twotrumpetsfft = fft(twotrumpets, n=len(twotrumpets), norm=None)

print(firstpianofft)
print('\n')
print(secondpianofft)
print('\n')
print(singletrumpetfft)
print('\n')
print(twotrumpetsfft)
