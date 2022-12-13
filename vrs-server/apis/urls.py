from django.urls import path
from . import views

urlpatterns = [
    path("predict", views.predict, name='prediction'),
    path("record", views.save_audios, name='save'),
    path("predictnew", views.new_predict, name='new predict'),
]
