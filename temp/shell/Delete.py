from polls.models import Question, Choice
from django.utils import timezone

Question.objects.filter(pub_date__year=2020).delete()

Question.objects.all().delete()

Question.objects.delete()
