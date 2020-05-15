from polls.models import Question, Choice
from django.utils import timezone

q = Question(question_text="What's new?", pub_date=timezone.now())

q.save()
