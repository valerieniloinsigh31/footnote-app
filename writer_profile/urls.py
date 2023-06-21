from django.urls import path
from . import views

app_name = 'writer_profile'

urlpatterns = [
    path('', views.writerprofile, name='writerprofile'),
    path('', views.footnote_history, name='footnote_history'),
    path('edit/<footnote_id>', views.edit_footnote, name='edit'),
]

# path('', views.footnote_history/<footnote_content>, name='footnote_content')
    # path('footnote_history/<footnote_number>/',
    #     views.footnote_history, name='footnote_history'), At the moment, no need