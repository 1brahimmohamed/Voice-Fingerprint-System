from django.shortcuts import render
from django.http import HttpResponse
import joblib


def predict(request):
    if request.method == 'POST':
        # load model
        cls = joblib.load('')

        # Do PROCESSING HERE #

        # RETURN OUTPUT TO FRONT #
        return HttpResponse([1, 2, 0, 5])
