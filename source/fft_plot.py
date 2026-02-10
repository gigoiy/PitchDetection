import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
from scipy.io import wavfile

### Sound signal data processing

firstpianorate, firstpianodata = wavfile.read('sound_data/piano1_mono.wav')
secondpianorate, secondpianodata = wavfile.read('sound_data/piano2_mono.wav')
singletrumpet = np.loadtxt('sound_data/trumpet.csv', delimiter=',')
twotrumpets = np.loadtxt('sound_data/twotrumpetsAB.csv', delimiter=',')
singletrumpetrate = 44100
twotrumpetsrate = 44100

### Normalizing the data from the .wav files

firstpianodata = firstpianodata.astype(float)
firstpianodata = firstpianodata / np.max(np.abs(firstpianodata))

secondpianodata = secondpianodata.astype(float)
secondpianodata = secondpianodata / np.max(np.abs(secondpianodata))

### FFT on sound signal data

firstpianofft = fft(firstpianodata, n=len(firstpianodata), norm=None)
secondpianofft = fft(secondpianodata, n=len(secondpianodata), norm=None)
singletrumpetfft = fft(singletrumpet, n=len(singletrumpet), norm=None)
twotrumpetsfft = fft(twotrumpets, n=len(twotrumpets), norm=None)

### Getting the frequency axis, N, and magnitudes of the four signals

N_firstpiano = len(firstpianofft)
N_secondpiano = len(secondpianofft)
N_singletrumpet = len(singletrumpetfft)
N_twotrumpets = len(twotrumpetsfft)

magnitude_firstpiano = np.abs(firstpianofft) / N_firstpiano
magnitude_secondpiano = np.abs(secondpianofft) / N_secondpiano
magnitude_singletrumpet = np.abs(singletrumpetfft) / N_singletrumpet
magnitude_twotrumpets = np.abs(twotrumpetsfft) / N_twotrumpets

frequency_firstpiano = fftfreq(n=N_firstpiano, d=1/firstpianorate)
frequency_secondpiano = fftfreq(n=N_secondpiano, d=1/secondpianorate)
frequency_singletrumpet = fftfreq(n=N_singletrumpet, d=1/singletrumpetrate)
frequency_twotrumpets = fftfreq(n=N_twotrumpets, d=1/twotrumpetsrate)

### Getting the first half of the signals

frequency_firstpiano = frequency_firstpiano[:N_firstpiano//2]
frequency_secondpiano = frequency_secondpiano[:N_secondpiano//2]
frequency_singletrumpet = frequency_singletrumpet[:N_singletrumpet//2]
frequency_twotrumpets = frequency_twotrumpets[:N_twotrumpets//2]

magnitude_firstpiano = magnitude_firstpiano[:N_firstpiano//2]
magnitude_secondpiano = magnitude_secondpiano[:N_secondpiano//2]
magnitude_singletrumpet = magnitude_singletrumpet[:N_singletrumpet//2]
magnitude_twotrumpets = magnitude_twotrumpets[:N_twotrumpets//2]

### Noting the fundamental frequencies of each file

fundamentals_firstpiano = [116.23, 276.598]
fundamentals_secondpiano = [116.279]
fundamentals_singletrumpet = [981.107]
fundamentals_twotrumpets = [872.094, 981.107]

### Create the plots

plt.figure(figsize=(10, 5))
plt.plot(frequency_firstpiano, magnitude_firstpiano)

for f0 in fundamentals_firstpiano:
    plt.axvline(f0, color='r', linestyle='--', linewidth=1)
    plt.text(
        f0 + 10,
        max(magnitude_firstpiano) * 0.8,
        f"{f0:.1f} Hz",
        color='r'
    )

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Magnitude Spectrum of piano1_mono.wav")
plt.xlim(0, 5000)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(frequency_secondpiano, magnitude_secondpiano)

for f0 in fundamentals_secondpiano:
    plt.axvline(f0, color='r', linestyle='--', linewidth=1)
    plt.text(
        f0 + 10,
        max(magnitude_secondpiano) * 0.8,
        f"{f0:.1f} Hz",
        color='r'
    )

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Magnitude Spectrum of piano2_mono.wav")
plt.xlim(0, 5000)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(frequency_singletrumpet, magnitude_singletrumpet)

for f0 in fundamentals_singletrumpet:
    plt.axvline(f0, color='r', linestyle='--', linewidth=1)
    plt.text(
        f0 + 10,
        max(magnitude_singletrumpet) * 0.8,
        f"{f0:.1f} Hz",
        color='r'
    )

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Magnitude Spectrum of trumpet.csv")
plt.xlim(0, 5000)
plt.grid(True)
plt.show()

plt.figure(figsize=(10, 5))
plt.plot(frequency_twotrumpets, magnitude_twotrumpets)

for f0 in fundamentals_twotrumpets:
    plt.axvline(f0, color='r', linestyle='--', linewidth=1)
    plt.text(
        f0 + 10,
        max(magnitude_twotrumpets) * 0.8,
        f"{f0:.1f} Hz",
        color='r'
    )

plt.xlabel("Frequency (Hz)")
plt.ylabel("Magnitude")
plt.title("FFT Magnitude Spectrum of twotrumpetsAB.csv")
plt.xlim(0, 5000)
plt.grid(True)
plt.show()
