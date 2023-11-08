from django.urls import path
from .views import index, done, update_feedback, FeedBackView, DoneView, FeedBackUpdateView, ListFeedBack, \
    DetailFeedBack

urlpatterns = [
    path('done', DoneView.as_view()),
    path('list', ListFeedBack.as_view()),
    path('detail/<int:id_fb>', DetailFeedBack.as_view(), name='feedback-detail'),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
]
