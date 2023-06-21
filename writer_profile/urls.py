from django.urls import path
from . import views

app_name = 'writer_profile'

urlpatterns = [
    path('', views.writerprofile, name='writerprofile'),
    path('', views.footnote_history,name='footnote_content')
    # path('footnote_history/<footnote_number>/',
    #     views.footnote_history, name='footnote_history'), At the moment, no need

]