from . import views #ALL VIEWS SHOULD BE IMPORTED FROM WITHIN APP
from django.urls import path
#from footnote.views import AddIdea, EditIdea #THIS MAY NOT BE NEEDED

urlpatterns = [
    path('add_idea', views.AddIdea.as_view(), name='add_idea'), # Put this url first so would not check in IdeaDetail
    path('', views.IdeaList.as_view(), name='home'),  # Consider updating home
    path('edit_idea/<slug:slug>', views.EditIdea.as_view(), name='edit_idea'), # ...slug or iid
    path('delete_idea/<slug:slug>', views.DeleteIdea.as_view(), name='delete_idea'), # Does view impact name...consider order...after idea_detail?
    path('<slug:slug>/', views.IdeaDetail.as_view(), name='idea_detail'),
    path('like/<slug:slug>', views.IdeaLike.as_view(), name='idea_like'),
]
