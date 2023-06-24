from . import views #ALL VIEWS SHOULD BE IMPORTED FROM WITHIN APP
from django.urls import path

urlpatterns = [
    path('add_idea/', views.AddIdea.as_view(), name='add_idea'), #Put this url first so would not check in IdeaDetail
    path('', views.IdeaList.as_view(), name='home'),  # Consider updating home
    path('<slug:slug>/', views.IdeaDetail.as_view(), name='idea_detail'),
    path('like/<slug:slug>', views.IdeaLike.as_view(), name='idea_like'),
   # path('edit/<slug:slug>', views.IdeaEdit.as_view(), name='idea_edit'),
   # path('delete/<slug:slug>', views.IdeaDelete.as_view(), name='idea_delete'),
   # path('like/<footnote_id>', views.FootNoteLike.as_view(), name='footnote_like'), #What id can be used for footnotes-no slug
   # path('delete/<footnote_id>', views.FootNoteDelete.as_view(), name='footnote_delete'), #What id can be used for footnotes-no slug
]
