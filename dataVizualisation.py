#!/bin/env python3

import numpy as np
import matplotlib.pyplot as plt

import librosa
import librosa.display
from IPython.display import Audio


y, sr = librosa.load(librosa.ex("choice"))


def showPlot(data, title):
    plt.title(title)
    plt.ylabel("Amplitude")
    plt.plot(data)
    plt.show()


def fourierTransform():
    D = librosa.stft(y)
    S_db = librosa.amplitude_to_db(np.abs(D), ref=np.max)
    fig, ax = plt.subplots()
    img = librosa.display.specshow(S_db, x_axis="time", y_axis="linear", ax=ax)
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    plt.title("Fourier transform")
    plt.show()


def melSpectrogram():
    fig, ax = plt.subplots()
    M = librosa.feature.melspectrogram(y=y, sr=sr)
    M_db = librosa.power_to_db(M, ref=np.max)
    img = librosa.display.specshow(M_db, y_axis="mel", x_axis="time", ax=ax)
    ax.set(title="Mel spectrogram display")
    fig.colorbar(img, ax=ax, format="%+2.f dB")
    plt.title("Mel spectrogram")
    plt.show()


def addNoise():
    noise = np.random.randn(len(y))
    data_noise = y + 0.005 * noise
    showPlot(data_noise, "adding noise")


def shift():
    showPlot(np.roll(y, 1600), "shifting audio")


def stretchFast():
    y_fast = librosa.effects.time_stretch(y, 2.0)
    showPlot(y_fast, "stretching faster")


def stretchSlow():
    y_slow = librosa.effects.time_stretch(y, 0.5)
    showPlot(y_slow, "stretching slower")


showPlot(y, "Normal data")
fourierTransform()
melSpectrogram()
addNoise()
shift()
stretchFast()
stretchSlow()


# Working with audio

# PRESENTATION
# Telling whats data augmentation (small def) 1-2min ; talking about the hertz frequency
# Telling what kind of library we used and we recommend for what specific things (librosa data augmentation/visualisation and torchaudio to feed it to the NN) 2-3min
# Theory explaining mel spectrogram how it works and why do we need it, how to resize it and the important parameter to tune 3-5min
# Hertz vs Mel scale 1min (find some difference)
# Showing the notebook (2 parts: first one librosa and second one torch audio) 2-3min
# Conclusion ?
