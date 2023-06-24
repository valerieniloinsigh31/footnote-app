from . import views
from django.urls import path

urlpatterns = [
    path('', views.IdeaList.as_view(), name='home'),  # Consider updating home
    path('<slug:slug>/', views.IdeaDetail.as_view(), name='idea_detail'),
    path('like/<slug:slug>', views.IdeaLike.as_view(), name='idea_like'),
    path('like/', views.FootNoteLike.as_view(), name='footnote_like'), #What id can be used for footnotes-no slug
    path('delete/', views.FootNoteDelete.as_view(), name='footnote_delete'), #What id can be used for footnotes-no slug
]
