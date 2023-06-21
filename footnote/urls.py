from . import views
from django.urls import path 

urlpatterns = [
    path('', views.IdeaList.as_view(), name='home'),  # UPDATE home to footnote as home app is called footnote
    path('<slug:slug>/', views.IdeaDetail.as_view(), name='idea_detail'),
    path('like/<slug:slug>', views.IdeaLike.as_view(), name='idea_like'),
]
