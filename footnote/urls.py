from . import views
from django.urls import path 

urlpatterns = [
    path('', views.IdeaList.as_view(), name='home'),
    path('<slug:slug/>', views.IdeaDetail.as_view(), name='idea_detail')
]