from django.utils import timezone
from django.utils.decorators import method_decorator
from rest_framework.permissions import AllowAny
from rest_framework import viewsets
from .models import Poll, PollQuestion, QuestionAnswer, PollAnswer
from .permissions import IsSuperUser
from .serializers import (PollSerializer, PollUpdateSerializer, PollQuestionSerializer,
                          QuestionAnswerSerializer, PollQuestionListSerializer, PollRetrieveSerializer,
                          PollAnswerSerializer)
from .swagger import (polls_list_schema, polls_retrieve_schema, polls_create_schema, polls_update_schema,
                      poll_question_list_schema, poll_question_retrieve_schema, poll_question_create_schema,
                      poll_question_update_schema, question_answer_list_schema, question_answer_retrieve_schema,
                      question_answer_create_schema, question_answer_update_schema, poll_answer_list_schema,
                      poll_answer_retrieve_schema, poll_answer_create_schema, polls_delete_schema,
                      poll_question_delete_schema, question_answer_delete_schema,
                      )

UNSAFE_METHODS = ['create', 'update', 'delete']


@method_decorator(name='list', decorator=polls_list_schema())
@method_decorator(name='retrieve', decorator=polls_retrieve_schema())
@method_decorator(name='create', decorator=polls_create_schema())
@method_decorator(name='update', decorator=polls_update_schema())
@method_decorator(name='update', decorator=polls_delete_schema())
@method_decorator(name='partial_update', decorator=polls_update_schema())
class PollViewSet(viewsets.GenericViewSet,
                  viewsets.mixins.ListModelMixin,
                  viewsets.mixins.CreateModelMixin,
                  viewsets.mixins.UpdateModelMixin,
                  viewsets.mixins.DestroyModelMixin,
                  viewsets.mixins.RetrieveModelMixin):

    def get_permissions(self):
        if self.action in UNSAFE_METHODS:
            return (IsSuperUser(), )
        return (AllowAny(), )

    def get_queryset(self):
        if self.request.user.is_superuser:
            return Poll.objects.all()
        return Poll.objects.filter(start_datetime__gte=timezone.now(), finish_datetime__lte=timezone.now())

    def get_serializer_class(self):
        if self.action in ['list', 'create']:
            return PollSerializer
        elif self.action == 'retrieve':
            return PollRetrieveSerializer
        elif self.action == 'update':
            return PollUpdateSerializer


@method_decorator(name='list', decorator=poll_question_list_schema())
@method_decorator(name='retrieve', decorator=poll_question_retrieve_schema())
@method_decorator(name='create', decorator=poll_question_create_schema())
@method_decorator(name='update', decorator=poll_question_update_schema())
@method_decorator(name='update', decorator=poll_question_delete_schema())
@method_decorator(name='partial_update', decorator=poll_question_update_schema())
class PollQuestionViewSet(viewsets.GenericViewSet,
                          viewsets.mixins.ListModelMixin,
                          viewsets.mixins.CreateModelMixin,
                          viewsets.mixins.UpdateModelMixin,
                          viewsets.mixins.DestroyModelMixin,
                          viewsets.mixins.RetrieveModelMixin):

    queryset = PollQuestion.objects.all()

    permission_classes = [IsSuperUser, ]

    def get_serializer_class(self):
        if self.action in UNSAFE_METHODS:
            return PollQuestionSerializer
        else:
            return PollQuestionListSerializer


@method_decorator(name='list', decorator=question_answer_list_schema())
@method_decorator(name='retrieve', decorator=question_answer_retrieve_schema())
@method_decorator(name='create', decorator=question_answer_create_schema())
@method_decorator(name='update', decorator=question_answer_update_schema())
@method_decorator(name='update', decorator=question_answer_delete_schema())
@method_decorator(name='partial_update', decorator=question_answer_update_schema())
class QuestionAnswerViewSet(viewsets.GenericViewSet,
                            viewsets.mixins.ListModelMixin,
                            viewsets.mixins.CreateModelMixin,
                            viewsets.mixins.UpdateModelMixin,
                            viewsets.mixins.DestroyModelMixin,
                            viewsets.mixins.RetrieveModelMixin):

    permission_classes = [IsSuperUser, ]

    queryset = QuestionAnswer.objects.all()
    serializer_class = QuestionAnswerSerializer


@method_decorator(name='list', decorator=poll_answer_list_schema())
@method_decorator(name='retrieve', decorator=poll_answer_retrieve_schema())
@method_decorator(name='create', decorator=poll_answer_create_schema())
class PollAnswerViewSet(viewsets.GenericViewSet,
                        viewsets.mixins.ListModelMixin,
                        viewsets.mixins.CreateModelMixin,
                        viewsets.mixins.RetrieveModelMixin):

    def get_permissions(self):
        if self.action in ['list', 'retrieve']:
            return (IsSuperUser(),)
        return (AllowAny(),)

    queryset = PollAnswer.objects.all()
    serializer_class = PollAnswerSerializer

    filterset_fields = ['user_id']
    search_fields = ['user_id']

