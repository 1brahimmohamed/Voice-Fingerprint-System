import pickle

import librosa
import numpy as np
from pydub import AudioSegment
import os

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect
from django.http import HttpResponse
from scipy.io.wavfile import read
import python_speech_features as mfcc
from sklearn import preprocessing

from . import model
from . import model2

speakers_models_path = "D:/My PC/Projects/DSP/Voice-Recognition-System/vrs-server/apis/models20/"
speakers_models_files = os.listdir(speakers_models_path)
speakers_models = [pickle.load(open(speakers_models_path + f_name, 'rb')) for f_name in speakers_models_files]

words_models_path = "D:/My PC/Projects/DSP/Voice-Recognition-System/vrs-server/apis/models/words/"
words_models_files = os.listdir(words_models_path)
words_models = [pickle.load(open(words_models_path + f_name, 'rb')) for f_name in words_models_files]

speakers = ['Amr', 'Ibrahim', 'Mariam', 'Momen', 'Other']
words = ['book', 'close', 'open', 'window']


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
    return combined


def convert_to_Wav(mp3_file):
    global i
    dir_ = './apis/Website Data/amr-other'
    record_names = list(os.listdir(dir_))

    max = 0
    for name in record_names:
        if max < int(name.split('.')[0]):
            max = int(name.split('.')[0])

    dist = './apis/Website Data/amr-other/' + str(max + 1) + '.wav'

    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(dist, format="wav")

    return dist


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
        print(request.FILES['file'])
        path = convert_to_Wav(mp3)

        sr, audio = read(path)
        vector = extract_features(audio, sr)

        log_likelihood_speakers = np.zeros(len(speakers_models))
        log_likelihood_words = np.zeros(len(words_models))

        for i in range(len(speakers_models)):
            gmm = speakers_models[i]  # checking with each model one by one
            scores = np.array(gmm.score(vector))
            log_likelihood_speakers[i] = scores.sum()

        prediction_speaker = np.argmax(log_likelihood_speakers)

        for j in range(len(words_models)):
            gmm = words_models[j]  # checking with each model one by one
            scores = np.array(gmm.score(vector))
            log_likelihood_words[j] = scores.sum()

        prediction_words = np.argmax(log_likelihood_words)

        print(log_likelihood_speakers)
        print(log_likelihood_words)

        # flag = False
        # flag_out_put = log_likelihood - max(log_likelihood)
        #
        # for i in range(len(flag_out_put)):
        #     if flag_out_put[i] == 0:
        #         continue
        #     if flag_out_put[i] > -0.07:
        #         flag = True
        #     if max(log_likelihood) - min(log_likelihood) < 0.5:
        #         flag = True
        #
        # if flag:
        #     prediction = 4

        return HttpResponse([speakers[prediction_speaker], words[prediction_words]])

# def choose_winner(similarity_score, prediction, threshold=100):
#     similarity_score = np.sort(similarity_score)
#     max_diff = similarity_score[3] - similarity_score[2]
#
#     if max_diff < threshold:
#         return 4
#     else:
#         return prediction
