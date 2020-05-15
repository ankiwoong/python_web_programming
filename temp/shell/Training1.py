# 우리가 정의한 모델을 사용하기 위해 임포트합니다.
from polls.models import Question, Choice

# 날짜를 입력하기 위해 timezone 모듈을 임포트합니다.
# settings.py 모듈에 TZ(TimeZone) 셋팅이 바르게 되어있어야 합니다.
# datetime.datetime.now()보다는 timezone.now() 사용을 추천합니다.
from django.utils import timezone

# 현재 각 테이블에 들어있는 레코드를 확인합니다.
# Question 레코드 3개가 보입니다.
Question.objects.all()
'''
<QuerySet [<Question: What is your hobby?>, <Question: Who do you like best?>, <Question: Where do you live?>]>
'''

# Choiece 레코드가 6개 보입니다.
Choice.objects.all()
'''
<QuerySet [<Choice: Reading>, <Choice: Soccer>, <Choice: Climbing>, <Choice: Seoul>, <Choice: Daejeon>, <Choice: Jeju>]>
'''

# 추가로 레코드 하나를 생성하겠습니다.
q = Question(question_text="What's up?", pub_date=timezone.now())

# 데이터베이스에 저장을 위해 save() 함수를 호출합니다.
q.save()

# id 속성이 자동을 생성된 것을 확인합니다.
q.id
'''
9
'''

# 속성에 접근할 때는 파이썬 문법 그대로 '.'을 사용합니다.
q.question_text
'''
"What's up?"
'''
q.pub_date
'''
datetime.datetime(2020, 5, 15, 12, 38, 16, 448391, tzinfo=<UTC>)
'''

# 기존의 속성값을 변경하고 데이터베이스에 저장합니다.
q.question_text = "What's new ?"
q.save()

# 테이블의 모든 레코드를 조회합니다.
Question.objects.all()
'''
<QuerySet [<Question: What is your hobby?>, <Question: Who do you like best?>, <Question: Where do you live?>, <Question: What's new ?>]>
'''

# 만일 레코드 제목이 [<Question: Question object>]처럼 나온다면,
# models.py 모듈에 __str()__ 메소드를 확인하기 바랍니다.

# 파이썬 쉘을 빠져 나오기 위해서는, exit() 또는 Ctrl+Z(리눅스에서는 Ctrl+D)를 입력합니다.
exit()
