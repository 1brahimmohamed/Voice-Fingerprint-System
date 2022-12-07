#!/usr/bin/env python
# coding: utf-8

# packages

import numpy as np
import librosa
import os
import pandas as pd

from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
from sklearn import preprocessing
from sklearn.model_selection import train_test_split

# ---------------------------- Helper Functions --------------------------- #

# function to create dataframe with the needed features for the header
def create_dataframe():
    # dataframe header
    header = 'filename rmse zero_crossing_rate'
    # insert the 21 mfcc feature column headers
    for i in range(1, 21):
        header += f' mfcc{i}'
    header += ' label'  # the label header
    header = header.split()  # make the header string -> array
    features_df = pd.DataFrame(columns=header)  # create the dataframe
    return features_df


# function to extract features from folder of sounds and turn it into dataframe

def extractWavFeatures(soundFilesFolder):
    # create the dataframe with the needed headers
    features_df = create_dataframe()

    for filename in os.listdir(soundFilesFolder):
        number = f'{soundFilesFolder}/{filename}'
        audio, sr = librosa.load(number, mono=True, duration=3)

        # remove leading and trailing silence
        audio, index = librosa.effects.trim(audio)
        rmse = librosa.feature.rms(y=audio)
        zcr = librosa.feature.zero_crossing_rate(audio)
        mfcc = librosa.feature.mfcc(y=audio, sr=sr)
        # dataframe row
        row_data = f'{filename} {np.mean(rmse)} {np.mean(zcr)}'

        # add mfcc features
        for e in mfcc:
            row_data += f' {np.mean(e)}'

        # add the labels for the dataframe
        if 'ibrahim' in filename:
            row_data += f' {1}'
        elif 'Amr' in filename:
            row_data += f' {2}'
        elif 'mariam' in filename:
            row_data += f' {3}'
        elif 'momen' in filename:
            row_data += f' {4}'
        else:
            row_data += f' {0}'

        # append the row to the dataframe
        features_df.loc[len(features_df)] = row_data.split()
    return features_df


def predict(x):
    scaled = min_max_scaler.transform(x)
    return nb_model.predict(scaled)

# ---------------------------- Model Creation --------------------------- #


team_df = extractWavFeatures("apis/modeldata/mydata")
others_df = extractWavFeatures('apis/modeldata/otherdata')
train_df = pd.concat([team_df, others_df])

# drop the unnecessary(label and filename) columns
X = train_df.drop(columns=['label', 'filename'], axis=1)
# get the label in new df
y = train_df['label']

cols = X.columns
min_max_scaler = preprocessing.MinMaxScaler()
np_scaled = min_max_scaler.fit_transform(X)

# new data frame with the new scaled data.
X = pd.DataFrame(np_scaled, columns=cols)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42, shuffle=True)

nb_model = GaussianNB()
nb_model.fit(X_train, y_train)

predictions_nb = nb_model.predict(X_train)
X_train_prediction_nb = nb_model.predict(X_train)
accuracy_score(X_train_prediction_nb, y_train)

X_test_prediction_nb = nb_model.predict(X_test)
new_score = accuracy_score(X_test_prediction_nb, y_test)
print("accuracy is:")
print(accuracy_score(X_test_prediction_nb, y_test))

