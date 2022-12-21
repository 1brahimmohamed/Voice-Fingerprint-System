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

# Loading Speakers Models
speakers_models_path = "D:/My PC/Projects/DSP/Voice-Recognition-System/vrs-server/apis/models/speakers/"
speakers_models_files = os.listdir(speakers_models_path)
speakers_models = [pickle.load(open(speakers_models_path + f_name, 'rb')) for f_name in speakers_models_files]

# Loading Words Models
words_models_path = "D:/My PC/Projects/DSP/Voice-Recognition-System/vrs-server/apis/models/words/"
words_models_files = os.listdir(words_models_path)
words_models = [pickle.load(open(words_models_path + f_name, 'rb')) for f_name in words_models_files]

# Read-only Arrays for easy accessing
speakers = ['Amr', 'Ibrahim', 'Mariam', 'Momen', 'others']
words = ['other', 'other', 'others', 'open', 'other']

# static 3D Plot data reading
df = pd.read_csv("apis/3d_2.csv")
amr_3d = [list(df["x_amr"]), list(df["y_amr"]), list(df["z_amr"])]
ibrahim_3d = [list(df["x_ibrahim"]), list(df["y_ibrahim"]), list(df["z_ibrahim"])]
momen_3d = [list(df["x_momen"]), list(df["y_momen"]), list(df["z_momen"])]
mariam_3d = [list(df["x_mariam"]), list(df["y_mariam"]), list(df["z_mariam"])]
plot_3d = [amr_3d, ibrahim_3d, momen_3d, mariam_3d]


# ----------------------- Feature Extraction Functions ----------------------- #

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


# ----------------------- Audio Operations Functions ----------------------- #

def convert_to_Wav(mp3_file):
    dist = './apis/operating.wav'
    sound = AudioSegment.from_mp3(mp3_file)
    sound.export(dist, format="wav")

    return dist


# ----------------------- Plotting Data Functions ----------------------- #


def get_3D_plot_point(path):
    audio, sr = librosa.load(path)
    mfcc_point = librosa.feature.mfcc(y=audio)

    mfcc_point_5 = mfcc_point[5].mean()
    mfcc_point_6 = mfcc_point[6].mean()
    mfcc_point_7 = mfcc_point[7].mean()

    return [float(mfcc_point_5), float(mfcc_point_6), float(mfcc_point_7)]


def get_scatter_plot_data(mfcc_plotted):
    vector_df = pd.DataFrame(mfcc_plotted)
    scattered_data = list(vector_df.mean(axis=0))

    return scattered_data


def get_pie_chart_data(log_likelihood_speakers):
    p_speakers = 10 ** log_likelihood_speakers
    pie_chart_values = list((p_speakers / sum(p_speakers)) * 100)

    return pie_chart_values


# ----------------------- Endpoints Functions ----------------------- #

@csrf_protect
@csrf_exempt
def save_audios(request):
    mp3 = request.FILES['file']
    convert_to_Wav(mp3)
    return HttpResponse('Audio Saved')


@csrf_protect
@csrf_exempt
def new_predict(request):
    if request.method == 'POST':

        # get mp3 file from the request
        mp3 = request.FILES['file']

        # convert mp3 to wav
        path = convert_to_Wav(mp3)

        # read the converted wav file from the returned path
        sr, audio = read(path)

        # extract features
        vector, mfcc_plotted = extract_features(audio, sr)

        # initialized 2 arrays with zeros
        log_likelihood_speakers = np.zeros(len(speakers_models))
        log_likelihood_words = np.zeros(len(words_models))

        # test input with the speaker models and the words mode
        for i in range(len(speakers_models)):
            gmm = speakers_models[i]  # checking with each model one by one
            scores = np.array(gmm.score(vector))  # get the score
            log_likelihood_speakers[i] = scores.sum()  # add model score to the array

        for j in range(len(words_models)):
            gmm = words_models[j]
            scores = np.array(gmm.score(vector))
            log_likelihood_words[j] = scores.sum()

        # the prediction of the words is the maximum score from the words array
        prediction_words = np.argmax(log_likelihood_words)

        # others detection with threshold
        normalized_possibility = max(log_likelihood_speakers) - log_likelihood_speakers
        not_others_flag = True

        for k in range(len(normalized_possibility)):
            if log_likelihood_speakers[k] == max(log_likelihood_speakers):
                continue

            if abs(normalized_possibility[k]) < 0.28:
                not_others_flag = False

        if not_others_flag:
            prediction_speaker = np.argmax(log_likelihood_speakers)

        else:
            prediction_speaker = 4

        # Plotting data
        point_3d = get_3D_plot_point(path)  # 3D Plot Point
        scattered_data = get_scatter_plot_data(mfcc_plotted)  # Scatter Plot
        pie_chart_data = get_pie_chart_data(log_likelihood_speakers)  # Pie chart

        # response data
        word = words[prediction_words]

        if speakers[prediction_speaker] == "Mariam":
            if log_likelihood_speakers[prediction_speaker] > log_likelihood_words[prediction_words]:
                word = 'open'
            else:
                word = 'others'

        return JsonResponse(
            {
                'speaker': speakers[prediction_speaker],
                'word': word,
                'pieChart': pie_chart_data,
                'scatterChart': scattered_data,
                'plot3D': plot_3d,
                'prePoint': point_3d
            }
        )
