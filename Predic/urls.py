from django.urls import path, include
from . import views




urlpatterns = [
    path('', views.predict, name='prediction_of_patient'),
    path('Predict/', views.predict_success, name='forms'),
    path('results/', views.show_results, name='results'),
]
