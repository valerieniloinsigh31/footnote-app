from django.urls import path
from . import views

app_name = 'medley'

urlpatterns = [
    path('', views.medley, name='medley'),
    path('', views.random_footnote, name='random_footnote'),
]
