from polls.models import Question, Choice
from django.utils import timezone

q.question_text = 'What is your favorite hobby ?'

q.save()

Question.objects.filter(pub_date__year=2020).update(
    question_text='Everything is the same')
