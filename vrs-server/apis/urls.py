from django.urls import path
from . import views


# APIs Application Routes

urlpatterns = [
    path("record", views.save_audios, name='save'),
    path("predictnew", views.new_predict, name='new predict'),
]
