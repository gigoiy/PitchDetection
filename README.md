# Pitch Detection - Signals and Systems
| File Name            | Fundamental Frequency (Hz) | Simultaneous / Sequential | Notes |
|----------------------|----------------------------|----------------------------|-------|
| trumpet.csv          |   981.107                      | Neither                 | Single dominant fundamental |
| twotrumpetsAB.csv    | 872.094, 981.107                   | Simultaneous                | Two trumpets playing together |
| piano2_mono.wav      | 116.379                      | Neither?                 | One fundamental but sequential notes playing? |
| piano1_mono.wav      | 116.23, 276.598                 | Sequential                 | Notes occur at different times |

## Techniques Used to Analyze the Data

- Used Scipy for signal analysis functionality such as FFT functions and used matplotlib to plot the data.
- Normalized the data extracted from the .wav files before plotting the transforms.

## Equations *Kind Of* Used During Analysis

So, I kind of used these equations, but SciPy did most of it for me.

$$
x[n], \quad n = 0, 1, 2, \dots, N-1
$$

**Equation (1):** Discrete-time signal obtained by sampling the continuous-time audio waveform.

$$
X[k] = \sum_{n=0}^{N-1} x[n] e^{-j 2\pi kn / N}
$$

**Equation (2):** Definition of the discrete Fourier transform (DFT).

$$
f_k = \frac{k F_s}{N}
$$

**Equation (3)**: Mapping FFT bin index to physical frequency.

$$
T_s = \frac{1}{F_s}
$$

**Equation (4):** Sampling interval in seconds per sample.

$$
\Delta f = \frac{F_s}{N}
$$

**Equation (5):** Frequency resolution of the FFT.

$$
|X[k]| = \sqrt{\Re\{X[k]\}^2 + \Im\{X[k]\}^2}
$$

**Equation (6):** Magnitude of the complex FFT output.

$$
|X_{\text{norm}}[k]| = \frac{|X[k]|}{N}
$$

**Equation (7):** Normalized FFT magnitude.

$$
0 \le f \le \frac{F_s}{2}
$$

**Equation (8):** Frequency range of the single-sided spectrum (Nyquist limit).

$$
x_{\text{dc}}[n] = x[n] - \frac{1}{N} \sum_{n=0}^{N-1} x[n]
$$

**Equation (9):** DC offset removal from the time-domain signal.






