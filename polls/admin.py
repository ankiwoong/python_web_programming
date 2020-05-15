from django.contrib import admin

from polls.models import Question, Choice


# StackedInline 방식
# class ChoiceInline(admin.StackedInline):
#     model = Choice
#     extra = 2

# TabularInline 방식
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]                            # Choice 모델 클래스 같이 보기
    list_display = ('question_text', 'pub_date')        # 레코드 리스트 컬럼 지정
    list_filter = ['pub_date']                          # 필터 사이드 바 추가


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
