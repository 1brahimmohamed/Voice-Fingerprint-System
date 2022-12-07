import librosa
import numpy as np
from pydub import AudioSegment

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse

from . import model


@csrf_protect
@csrf_exempt
def predict(request):
    if request.method == 'POST':

        mp3 = request.FILES['file']
        print(request.FILES['file'])

        # PRE-PROCESSING (feature extraction) #

        audio, sr = librosa.load(path, duration=3)

        audio, index = librosa.effects.trim(audio)
        rms = librosa.feature.rms(y=audio)
        zcr = librosa.feature.zero_crossing_rate(audio)
        mfcc = librosa.feature.mfcc(y=audio, sr=sr)
        # dataframe rowgit
        row_data = f'{np.mean(rms)} {np.mean(zcr)}'

        # add mfcc features
        for feat in mfcc:
            row_data += f' {np.mean(feat)}'

        # RETURN OUTPUT TO FRONT #
        prediction = model.predict([row_data.split()])
        return HttpResponse([prediction])


