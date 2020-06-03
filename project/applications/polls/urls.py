from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import PollViewSet, PollQuestionViewSet, QuestionAnswerViewSet, PollAnswerViewSet

router = DefaultRouter()

router.register('polls', PollViewSet, basename='polls')
router.register('questions', PollQuestionViewSet, basename='questions')
router.register('question_answers', QuestionAnswerViewSet, basename='question_answers')
router.register('answers', PollAnswerViewSet, basename='answers')

urlpatterns = [
    path('', include(router.urls))
]
