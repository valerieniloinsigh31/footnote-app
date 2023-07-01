from . import views 
from django.urls import path
# from footnote.views import AddIdea, EditIdea #THIS MAY NOT BE NEEDED

urlpatterns = [
    path('', views.IdeaList.as_view(), name='home'), 
    path('add_idea/', views.AddIdea.as_view(), name='add_idea'),
    path('<slug:slug>/', views.IdeaDetail.as_view(), name='idea_detail'),
    path('like/<slug:slug>', views.IdeaLike.as_view(), name='idea_like'),
    path('<slug:slug>/delete_footnote/<int:footnote_id>', views.footnote_delete, name='footnote_delete'),
    path('<slug:slug>/edit_footnote/<int:footnote_id>', views.footnote_edit, name='footnote_edit'),
]
