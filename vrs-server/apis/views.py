import json
import pickle

import librosa
import numpy as np
import pandas as pd
from pydub import AudioSegment
import os

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse, JsonResponse
from scipy.io.wavfile import read
import python_speech_features as mfcc
from sklearn import preprocessing

# from . import model
# from . import model2

speakers_models_path = "D:/My PC/Projects/DSP/Voice-Recognition-System/vrs-server/apis/models/speakers/"
speakers_models_files = os.listdir(speakers_models_path)
speakers_models = [pickle.load(open(speakers_models_path + f_name, 'rb')) for f_name in speakers_models_files]

words_models_path = "D:/My PC/Projects/DSP/Voice-Recognition-System/vrs-server/apis/models/words/"
words_models_files = os.listdir(words_models_path)
words_models = [pickle.load(open(words_models_path + f_name, 'rb')) for f_name in words_models_files]

speakers = ['Amr', 'Ibrahim', 'Mariam', 'Momen', 'others']
words = ['other', 'other', 'others', 'open', 'other']

df = pd.read_csv("apis/3d_2.csv")
amr_3d = [list(df["x_amr"]), list(df["y_amr"]), list(df["z_amr"])]
ibrahim_3d = [list(df["x_ibrahim"]), list(df["y_ibrahim"]), list(df["z_ibrahim"])]
momen_3d = [list(df["x_momen"]), list(df["y_momen"]), list(df["z_momen"])]
mariam_3d = [list(df["x_mariam"]), list(df["y_mariam"]), list(df["z_mariam"])]
plot_3d = [amr_3d, ibrahim_3d, momen_3d, mariam_3d]


def calculate_delta(array):
    rows, cols = array.shape
    deltas = np.zeros((rows, 20))
    N = 2
    for i in range(rows):
        index = []
        j = 1
        while j <= N:
            if i - j < 0:
                first = 0
            else:
                first = i - j
            if i + j > rows - 1:
                second = rows - 1
            else:
                second = i + j
            index.append((second, first))
            j += 1
        deltas[i] = (array[index[0][0]] - array[index[0][1]] + (2 * (array[index[1][0]] - array[index[1][1]]))) / 10
    return deltas


def extract_features(audio, rate):
    mfcc_feature = mfcc.mfcc(audio, rate, 0.025, 0.01, 20, nfft=1200, appendEnergy=True)
    mfcc_feature = preprocessing.scale(mfcc_feature)
    delta = calculate_delta(mfcc_feature)
    combined = np.hstack((mfcc_feature, delta))
    return combined, mfcc_feature


# def convert_to_Wav(mp3_file):
#     global i
#     dir_ = './apis/Website Data/amr-other'
#     record_names = list(os.listdir(dir_))
#
#     max = 0
#     for name in record_names:
#         if max < int(name.split('.')[0]):
#             max = int(name.split('.')[0])
#
#     dist = './apis/Website Data/amr-other/' + str(max + 1) + '.wav'
#
#     sound = AudioSegment.from_mp3(mp3_file)
#     sound.export(dist, format="wav")
#
#     return dist


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


def convert_to_Wav(mp3_file):
    dist = './apis/opertating.wav'
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(dist, format="wav")

    return dist

i = 0


@csrf_protect
@csrf_exempt
def save_audios(request):
    mp3 = request.FILES['file']
    path = convert_to_Wav(mp3)
    return HttpResponse([0])


@csrf_protect
@csrf_exempt
def new_predict(request):
    if request.method == 'POST':

        mp3 = request.FILES['file']
        path = convert_to_Wav(mp3)

        sr, audio = read(path)
        vector, mfcc_plotted = extract_features(audio, sr)

        log_likelihood_speakers = np.zeros(len(speakers_models))

        log_likelihood_words = np.zeros(len(words_models))

        point, sr = librosa.load(path)
        mfcc_point = librosa.feature.mfcc(y=point)

        point_5 = mfcc_point[5].mean()
        point_6 = mfcc_point[6].mean()
        point_7 = mfcc_point[7].mean()

        my_point = [float(point_5), float(point_6), float(point_7)]

        for i in range(len(speakers_models)):
            gmm = speakers_models[i]  # checking with each model one by one
            scores = np.array(gmm.score(vector))
            log_likelihood_speakers[i] = scores.sum()

        for j in range(len(words_models)):
            gmm = words_models[j]  # checking with each model one by one
            scores = np.array(gmm.score(vector))
            log_likelihood_words[j] = scores.sum()

        prediction_words = np.argmax(log_likelihood_words)

        print('speakers:', log_likelihood_speakers)
        print('words: ', log_likelihood_words)


        vector_df = pd.DataFrame(mfcc_plotted)
        scattered_data = list(vector_df.mean(axis=0))

        p_speakers = 10 ** log_likelihood_speakers
        pie_chart_values = list((p_speakers / sum(p_speakers)) * 100)


        normalized_possibility = max(log_likelihood_speakers) - log_likelihood_speakers
        not_others_flag = True

        for i in range(len(normalized_possibility)):

            if log_likelihood_speakers[i] == max(log_likelihood_speakers):
                continue

            if abs(normalized_possibility[i]) < 0.28:
                not_others_flag = False

        if not_others_flag:
            prediction_speaker = np.argmax(log_likelihood_speakers)

        else:
            prediction_speaker = 4
            print('thersould')

        if speakers[prediction_speaker] == "Mariam":
            if log_likelihood_speakers[prediction_speaker] > log_likelihood_words[prediction_words]:
                return JsonResponse(
                    {
                        'speaker': speakers[prediction_speaker],
                        'word': 'open',
                        'pieChart': pie_chart_values,
                        'scatterChart': scattered_data,
                        'plot3D': plot_3d,
                        'prePoint': my_point
                    }
                )
            else:
                return JsonResponse(
                    {
                        'speaker': speakers[prediction_speaker],
                        'word': 'others',
                        'pieChart': pie_chart_values,
                        'scatterChart': scattered_data,
                        'plot3D': plot_3d,
                        'prePoint': my_point
                    }
                )

        return JsonResponse(
            {
                'speaker': speakers[prediction_speaker],
                'word': words[prediction_words],
                'pieChart': pie_chart_values,
                'scatterChart': scattered_data,
                'plot3D': plot_3d,
                'prePoint': my_point
            }
        )
