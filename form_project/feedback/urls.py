from django.urls import path
from .views import index, done, update_feedback, FeedBackView, DoneView, FeedBackUpdateView

urlpatterns = [
    path('done', DoneView.as_view()),
    path('', FeedBackView.as_view()),
    path('<int:id_feedback>', FeedBackUpdateView.as_view()),
]
