from django.utils import timezone
from polls.models import Question, Choice

# 모든 레코드가 아니라, 조건에 맞는 레코드를 조회하는 기능들입니다.
# 조건 표현에는 filter() 함수 및 키워드 인자를 사용합니다.
# startswith와 같은 연산자를 붙일 때는 __(밑줄 2개)를 사용합니다.
Question.objects.filter(id=6)
'''
<QuerySet [<Question: What is your hobby?>]>
'''
Question.objects.filter(question_text__startswith='What')
'''
<QuerySet [<Question: What is your hobby?>, <Question: What's new ?>]>
'''

# 올해 생성된 질문을 조회해 봅시다.
current_year = timezone.now().year
Question.objects.filter(pub_date__year=current_year)
'''
<QuerySet [<Question: What is your hobby?>, <Question: Who do you like best?>, <Question: Where do you live?>, <Question: What's new ?>]>
'''

# id 값을 잘못 지정하면 익셉션이 발생합니다.
Question.objects.get(id=3)
'''
Traceback (most recent call last):
  File "<console>", line 1, in <module>
  File "C:\python_web_programming\venv\lib\site-packages\django\db\models\manager.py", line 82, in manager_method
    return getattr(self.get_queryset(), name)(*args, **kwargs)
  File "C:\python_web_programming\venv\lib\site-packages\django\db\models\query.py", line 417, in get
    self.model._meta.object_name
polls.models.Question.DoesNotExist: Question matching query does not exist.
'''

# 주키(Primary Key)로 조회하는 것은 흔히 사용하는 조회 명령입니다.
# Question.objects.get(id=6) 명령과 동일합니다.
Question.objects.get(pk=6)
'''
<Question: What is your hobby?>
'''

# 지금부터는 Choice 모델에 관련된 명령들입니다.
# Question과 Choice 테이블의 관계는 1:N의 관계로, 외래키(Foreign Key)로 정의되어 있습니다.
# 이런 경우 장고는 choice_set API를 제공합니다.
# 즉, choice -> Question 방향에는 question 속성을,
# Question -> Choice 방향으로는 choice_set 속성을 사용합니다.

# 우선, Question 테이블의 레코드 하나를 지정합니다.
q = Question.objects.get(pk=7)

# 이 질문 레코드에 연결된 답변 항목을 모두 조회합니다.
q.choice_set.all()
'''
<QuerySet []>
'''

# 질문의 답변 항목 3개를 생성해보겠습니다.
# create() 함수를 호출하면 Choice 객체를 생성해서 데이터베이스에 저장하고,
# choice_set 리스트에 추가한 다음 생성된 객체를 반환합니다.
q.choice_set.create(choice_text='Sleeping', votes=0)
'''
<Choice: Sleeping>
'''
q.choice_set.create(choice_text='Eating', votes=0)
'''
<Choice: Eating>
'''
c = q.choice_set.create(choice_text='Playing', votes=0)

# Choice 객체에서 자신과 연결된 Question 객체를 조회할 수 있습니다.
c.question
'''
<Question: Who do you like best?>
'''

# 반대 방향으로, Question 객체 역시 자신과 연결된 Choice 객체를 조회할 수 있습니다.
q.choice_set.all()
'''
<QuerySet [<Choice: Sleeping>, <Choice: Eating>, <Choice: Playing>]>
'''
q.choice_set.count()
'''
3
'''

# 밑줄 2개(__)를 사용하여 객체 간의 관계를 표현할 수 있습니다.
# pub_date 속성이 올해인 Question 객체에 연결된 Choice 객체를 모두 조회하는 명령입니다.
# 'current_year' 변수는 앞에서 정의한 바 있습니다.
Choice.objects.filter(question__pub_date__year=current_year)
'''
<QuerySet [<Choice: Reading>, <Choice: Soccer>, <Choice: Climbing>, <Choice: Seoul>, <Choice: Daejeon>, <Choice: Jeju>, <Choice: Sleeping>, <Choice: Eating>, <Choice: Playing>]>
'''

# choice_set 중에서 한 개의 답변 항목을 삭제할 수 있습니다.
c = q.choice_set.filter(choice_text__startswith='Sleeping')
c.delete()
'''
(1, {'polls.Choice': 1})
'''
