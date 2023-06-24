from django.contrib import admin
from django.urls import path, include
from . import views

app_name = 'FOOTNOTE_APP'

urlpatterns = [
    path('admin/', admin.site.urls),
    path('summernote/', include('django_summernote.urls')),
    path('writer/', include('writer_profile.urls')),
    path('footnote/', include('footnote.urls')),  
    path('accounts/', include('allauth.urls')),
    path('', views.FOOTNOTE_APP, name='FOOTNOTE_APP'),
]
