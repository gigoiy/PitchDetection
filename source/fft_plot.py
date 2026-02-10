import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile

firstpianorate, firstpianodata = wavfile.read('sound_data/piano1_mono.wav')
secondpianorate, secondpianodata = wavfile.read('sound_data/piano2_mono.wav')

firstpianodata = firstpianodata.astype(float)
firstpianodata = firstpianodata / np.max(np.abs(firstpianodata))

secondpianodata = secondpianodata.astype(float)
secondpianodata = secondpianodata / np.max(np.abs(secondpianodata))

singletrumpet = np.loadtxt('sound_data/trumpet.csv', delimiter=',')
twotrumpets = np.loadtxt('sound_data/twotrumpetsAB.csv', delimiter=',')

firstpianofft = fft(firstpianodata, n=len(firstpianodata), norm=None)
secondpianofft = fft(secondpianodata, n=len(secondpianodata), norm=None)
singletrumpetfft = fft(singletrumpet, n=len(singletrumpet), norm=None)
twotrumpetsfft = fft(twotrumpets, n=len(twotrumpets), norm=None)

print(firstpianofft)
print('\n')
print(secondpianofft)
print('\n')
print(singletrumpetfft)
print('\n')
print(twotrumpetsfft)
