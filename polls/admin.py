from django.contrib import admin

from polls.models import Question, Choice


# StackedInline 방식
class ChoiceInline(admin.StackedInline):
    model = Choice
    extra = 2

# TabularInline 방식
# class ChoiceInline(admin.TabularInline):
#     model = Choice
#     extra = 2


class QuestionAdmin(admin.ModelAdmin):
    fieldsets = [
        ('Question Statement', {'fields': ['question_text']}),
        ('Date Information', {'fields': [
         'pub_date'], 'classes': ['collapse']}),
    ]
    inlines = [ChoiceInline]        # Choice 모델 클래스 같이 보기


admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
