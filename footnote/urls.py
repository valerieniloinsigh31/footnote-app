from . import views
from django.urls import path 
from .views import writer
from .views import MedleyListView

urlpatterns = [
    path('', views.IdeaList.as_view(), name='home'),
    path('<slug:slug>/', views.IdeaDetail.as_view(), name='idea_detail'),
    path('/writer', MedleyListView.as_view(medley_detail), name='medley'),
    path('like/<slug:slug>', views.IdeaLike.as_view(), name='idea_like'),
    path('like/<slug:slug>', views.FootnoteLike.as_view(), name='footnote_like'),
]
