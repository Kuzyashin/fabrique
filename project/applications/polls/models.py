from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

# Create your models here.


class Poll(models.Model):
    name = models.CharField(
        max_length=80,
        unique=True
    )
    start_datetime = models.DateTimeField()

    finish_datetime = models.DateTimeField()

    description = models.TextField(
        null=True, blank=True
    )

    @property
    def is_active(self):
        return all([self.start_datetime < timezone.now(), self.finish_datetime > timezone.now()])

    def __str__(self):
        return f'{self.name} -' \
               f' {self.start_datetime.strftime("%Y-%m-%d %H:%M")} - {self.finish_datetime.strftime("%Y-%m-%d %H:%M")}'


class PollQuestion(models.Model):
    TEXT = 'text'
    SINGLE = 'single'
    MULTIPLE = 'multiple'
    QUESTION_TYPES = (
        (TEXT, 'Text Answer'),
        (SINGLE, 'Single choice'),
        (MULTIPLE, 'Multiple choice')
    )

    poll = models.ForeignKey(
        Poll, models.CASCADE,
        null=True, blank=True,
        related_name='poll_questions'
    )
    question_text = models.TextField()

    question_type = models.CharField(
        choices=QUESTION_TYPES,
        max_length=8,
        default='text'
    )

    def __str__(self):
        return f'{self.poll.name}  - {self.question_type} - {self.question_text[:20]}'


class QuestionAnswer(models.Model):
    question = models.ForeignKey(
        PollQuestion, models.CASCADE,
        null=True, blank=True,
        related_name='question_answers'
    )
    text = models.TextField(
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.question} - {self.text[:20]}'


class PollAnswer(models.Model):
    user = models.ForeignKey(
        User, models.CASCADE,
        null=True, blank=True
    )
    question = models.ForeignKey(
        PollQuestion, models.CASCADE,
        null=True, blank=True
    )
    answer_text = models.TextField(
        null=True, blank=True
    )
    answer_choice = models.ManyToManyField(
        QuestionAnswer,
        null=True, blank=True,
    )
    created_at = models.DateTimeField(
        null=True, blank=True
    )

    def __str__(self):
        return f'{self.question} - {self.user or "anon user"}'
