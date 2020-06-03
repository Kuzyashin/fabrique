from rest_framework.exceptions import ValidationError

from .models import *
from rest_framework import serializers


class PollSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = [
            'name',
            'start_datetime',
            'finish_datetime',
            'description'
        ]


class PollUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Poll
        fields = [
            'name',
            'finish_datetime',
            'description'
        ]


class PollQuestionSerializer(serializers.ModelSerializer):

    class Meta:
        model = PollQuestion
        fields = '__all__'


class QuestionAnswerSerializer(serializers.ModelSerializer):

    class Meta:
        model = QuestionAnswer
        fields = '__all__'


class PollQuestionListSerializer(serializers.ModelSerializer):
    question_answers = QuestionAnswerSerializer(many=True, read_only=True)

    class Meta:
        model = PollQuestion
        fields = '__all__'


class PollRetrieveSerializer(serializers.ModelSerializer):
    poll_questions = PollQuestionListSerializer(many=True, read_only=True)

    class Meta:
        model = Poll
        fields = [
            'name',
            'start_datetime',
            'finish_datetime',
            'description',
            'poll_questions'
        ]
        read_only_fields = [
            'name',
            'start_datetime',
            'finish_datetime',
            'description',
            'poll_questions'
        ]


class PollAnswerSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        question = validated_data['question']
        request = self.context['request']
        if question.question_type == 'text':
            poll_answer = PollAnswer.objects.create(
                answer_text=validated_data['answer_text'],
                question=question,
                created_at=timezone.now(),
                user=request.user
            )
        elif question.question_type == 'single':
            if len(validated_data['answer_choice']) > 1:
                raise ValidationError('Only one choice allowed')
            else:
                poll_answer = PollAnswer.objects.create(
                    question=question,
                    created_at=timezone.now(),
                    user=request.user
                )
                poll_answer.answer_choice.add(*validated_data['answer_choice'])
        else:
            poll_answer = PollAnswer.objects.create(
                question=question,
                created_at=timezone.now(),
                user=request.user
            )
            poll_answer.answer_choice.set(validated_data['answer_choice'])
        return poll_answer

    class Meta:
        model = PollAnswer
        fields = [
            'user',
            'question',
            'answer_text',
            'answer_choice',
            'created_at'
        ]
        read_only_fields = [
            'user',
            'created_at'
        ]
