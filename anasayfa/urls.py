from django.urls import path
from . import views

# http://127.0.0.1:8000/                 => index
# http://127.0.0.1:8000/egitmen_anasayfa => eğitmen anasayfası

urlpatterns = [
    path("", views.anasayfa, name="anasayfa"),
]
