import librosa
import soundfile as sf
import os
from IPython.display import Audio
import matplotlib.pyplot as plt
import numpy as np
from scipy import signal
import pandas as pd
from sklearn.preprocessing import MinMaxScaler
from sklearn.preprocessing import StandardScaler
from sklearn.impute import SimpleImputer
from sklearn.model_selection import train_test_split
from sklearn import svm
from sklearn.metrics import accuracy_score
from sklearn.neighbors import KNeighborsClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
from sklearn import preprocessing

df = pd.read_csv("apis/voice_catigorized2.csv")
#model_assess(xgbrf, "Cross Gradient Booster (Random Forest)")
#%%
y = df['result'] # result.
X = df.drop(columns = 'result', axis=1)

cols = X.columns
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(X)

# new data frame with the new scaled data.
X = pd.DataFrame(np_scaled, columns = cols)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42,shuffle = True)

#creating the model
model = LogisticRegression()
model.fit(X, y)


predictions = model.predict(X_train)
X_train_prediction = model.predict(X_train)
accuracy_score(X_train_prediction, y_train)

X_test_prediction = model.predict(X_test)
new_score = accuracy_score(X_test_prediction, y_test)
print("accuracy is:")
print(accuracy_score(X_test_prediction, y_test))
def get_result(file):
    audio, sr = librosa.load(file, duration=2)
    audio = librosa.effects.trim(audio)
    audio = audio[0]

    features = [librosa.feature.chroma_stft(y=audio, sr=sr).mean(), librosa.feature.chroma_stft(y=audio, sr=sr).var(),
                    librosa.feature.rms(y=audio).mean(), librosa.feature.rms(y=audio).var(), 
                    librosa.feature.spectral_centroid(y=audio).mean(),librosa.feature.spectral_centroid(y=audio).var(),
                    librosa.feature.spectral_bandwidth(y=audio).mean(),librosa.feature.spectral_bandwidth(y=audio).var(),
                    librosa.feature.spectral_rolloff(y=audio).mean(),librosa.feature.spectral_rolloff(y=audio).var()]
    mfcc = librosa.feature.mfcc(y=audio)
    mfcc_list = []
    for i in range(len(mfcc)):
        mfcc_list.append(mfcc[i].mean())
        mfcc_list.append(mfcc[i].var())
    features = features + mfcc_list
    scaled = min_max_scaler.transform([features])
    res = model.predict(scaled)
    print (res)
    return res[0]
