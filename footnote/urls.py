from . import views
from django.urls import path 

urlpatterns = [
    path('', views.IdeaList.as_view(), name='home'),
    path('<slug:slug>/', views.IdeaDetail.as_view(), name='idea_detail'),
#   path('', views.FootNoteList.as_view(), name='medley'),
    path('like/<slug:slug>', views.IdeaLike.as_view(), name='idea_like'),
    path('like/<slug:slug>', views.FootnoteLike.as_view(), name='footnote_like'),
]
