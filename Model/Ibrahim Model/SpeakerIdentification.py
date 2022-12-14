import os
import pickle
import warnings
import numpy as np
from sklearn import preprocessing
from scipy.io.wavfile import read
import python_speech_features as mfcc
from sklearn.mixture import GaussianMixture

warnings.filterwarnings("ignore")

speakers = ['Amr', 'Ibrahim', 'Mariam', 'Momen', 'Other']


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


def train_model():
    source = "D:/My PC/Projects/DSP/Voice-Recognition-System/vrs-server/apis/Website Data/Mo'men/"
    dest = "D:/My PC/Projects/Tamora/Speaker-Identification-Using-Machine-Learning/dist/"
    count = 1
    features = np.asarray(())
    for path in os.listdir(source):
        path = path.strip()

        sr, audio = read(source + path)

        vector = extract_features(audio, sr)

        if features.size == 0:
            features = vector
        else:
            features = np.vstack((features, vector))

        if count == 20:
            gmm = GaussianMixture(n_components=6, max_iter=200, covariance_type='diag', n_init=3)
            gmm.fit(features)

            # dumping the trained gaussian model
            picklefile = "Momen-model20" + ".gmm"
            pickle.dump(gmm, open(dest + picklefile, 'wb'))
            print('+ modeling completed for speaker:', picklefile, " with data point = ", features.shape)
            features = np.asarray(())
            count = 0

        count = count + 1


def test_model():
    source0 = "D:/My PC/Projects/DSP/Voice-Recognition-System/Model/test_data/"
    source1 = 'D:/My PC/Projects/DSP/Voice-Recognition-System/Model/Website Data/amr-others/'
    source2 = 'D:/My PC/Projects/DSP/Voice-Recognition-System/Model/Website Data/ibrahim-other/'
    source3 = 'D:/My PC/Projects/DSP/Voice-Recognition-System/Model/Website Data/momen-other/'
    # sources = [source1, source0, source2, source3]
    sources = [source0]

    modelpath = "D:/My PC/Projects/Tamora/Speaker-Identification-Using-Machine-Learning/dist/"

    gmm_files = os.listdir(modelpath)

    # Load the Gaussian gender Models

    models = [pickle.load(open(modelpath + fname, 'rb')) for fname in gmm_files]
    # thresholds = list()
    # Read the test directory and get the list of test audio files
    for source in sources:
        for path in os.listdir(source):

            path = path.strip()

            sr, audio = read(source + path)
            vector = extract_features(audio, sr)

            log_likelihood = np.zeros(len(models))

            for i in range(len(models)):
                gmm = models[i]  # checking with each model one by one
                scores = np.array(gmm.score(vector))
                log_likelihood[i] = scores.sum()

            winner = np.argmax(log_likelihood)
            print("\tdetected as - ", speakers[winner])


train_model()
# test_model()
