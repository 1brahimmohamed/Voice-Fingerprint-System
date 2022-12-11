from django.urls import path
from . import views

urlpatterns = [
    path("predict", views.save_audios, name='prediction'),
]
