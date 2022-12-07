import os.path
import pickle

import librosa
import numpy as np
import joblib
from pydub import AudioSegment

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from django.shortcuts import render


@csrf_protect
@csrf_exempt
def predict(request):
    if request.method == 'POST':

        mp3 = request.FILES['file']
        print(request.FILES['file'])

        # CONVERSION
        # sound = AudioSegment.from_mp3(mp3)

        # PRE-PROCESSING #

        audio, sr = librosa.load(mp3, duration=2)

        rmse = librosa.feature.rms(y=audio)
        zcr = librosa.feature.zero_crossing_rate(audio)
        mfcc = librosa.feature.mfcc(y=audio, sr=sr)
        # dataframe row
        row_data = f'{np.mean(rmse)} {np.mean(zcr)}'

        # add mfcc features
        for e in mfcc:
            row_data += f' {np.mean(e)}'

        print(len(row_data.split()))
        # print(row_data.split())

        # RETURN OUTPUT TO FRONT #

        return HttpResponse([1, 2, 0, 5])
