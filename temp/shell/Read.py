from polls.models import Question, Choice
from django.utils import timezone

Question.objects.all()

Question.objects.filter(question_text__startswith='What'
                        ).exclude(
    pub_date__gte=datetime.date.today()
).filter(pub_date__gte=datetime(2020, 5, 15)
         )

one_entry = Question.objects.get(pk=1)

Question.objects.all()[:5]
Question.objects.all()[5:10]
Question.objects.all()[:10:2]
