import librosa
import numpy as np
from pydub import AudioSegment
import json
from . import model2
from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
import os
from . import model



@csrf_protect
@csrf_exempt
def predict(request):
    if request.method == 'POST':

        mp3 = request.FILES['file']
        print(request.FILES['file'])

        path = convert_to_Wav(mp3)
        # PRE-PROCESSING (feature extraction) #

        audio, sr = librosa.load("./apis/operating.wav", duration=2)

        rms = librosa.feature.rms(y=audio)
        zcr = librosa.feature.zero_crossing_rate(audio)
        mfcc = librosa.feature.mfcc(y=audio, sr=sr)
        # dataframe row
        row_data = f'{np.mean(rms)} {np.mean(zcr)}'

        # add mfcc features
        for feat in mfcc:
            row_data += f' {np.mean(feat)}'

        # RETURN OUTPUT TO FRONT #
        prediction = model.predict([row_data.split()])
        prediction2 = model2.get_result("./apis/operating.wav")

        return HttpResponse([prediction, prediction2])


# def convert_to_Wav(mp3_file):
#     dist = 'operating.wav'
#     sound = AudioSegment.from_mp3(mp3_file)
#     sound.export(dist, format="wav")
#
#     return dist

i = 0
def convert_to_Wav(mp3_file):
    '''
    global i
    dir_ = './apis/webrecord5/'
    record_names = list(os.listdir(dir_))

    max = 0
    for name in record_names:
        if max < int(name.split('.')[0]):
            max = int(name.split('.')[0])


    dist = './apis/webrecord5/'+str(max+1)+'.wav'

    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(dist, format="wav")
    '''
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export("./apis/operating.wav", format="wav")

    return "operating.wav"
