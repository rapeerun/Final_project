from django.urls import path, include
from . import views


# app = "Predic"

urlpatterns = [
    path('', views.predict, name='prediction_of_patient'),
    path('Predic/', views.predict_success, name='forms'),
    path('results/', views.show_results, name='results'),
]
