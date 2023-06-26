from django.urls import path
from . import views

app_name = 'medley'

urlpatterns = [
    path('', views.medley, name='medley'),
    path('', views.footnote_medley, name='footnote_medley'),
]
