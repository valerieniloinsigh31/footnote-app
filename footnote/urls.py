from . import views 
from django.urls import path
#from footnote.views import AddIdea, EditIdea #THIS MAY NOT BE NEEDED

urlpatterns = [
    path('<slug:slug>/delete_footnote/<int:footnote_id>', views.footnote_delete, name='footnote_delete'),
    path('add_idea', views.AddIdea.as_view(), name='add_idea'), # Put this url first so would not check in IdeaDetail
    path('', views.IdeaList.as_view(), name='home'),  # Consider updating home
#     path('edit_idea/', views.EditIdea.as_view(), name='edit_idea'), # ...slug or iid 
    path('<slug:slug>/', views.IdeaDetail.as_view(), name='idea_detail'),
    path('like/<slug:slug>', views.IdeaLike.as_view(), name='idea_like'),
]
