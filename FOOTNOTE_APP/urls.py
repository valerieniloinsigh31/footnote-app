from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'FOOTNOTE_APP'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('medley/', include('medley.urls')), 
    path("", include("footnote.urls"), name="footnote-urls"),      
    path('', include('writer_profile.urls')),
    path('accounts/', include('allauth.urls')),
    path('', views.FOOTNOTE_APP, name='FOOTNOTE_APP'),
]
