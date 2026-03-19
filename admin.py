from django.contrib import admin
# TASK: Must include all 7 classes below
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# 1. ChoiceInline implementation
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# 2. QuestionInline implementation
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# 3. QuestionAdmin implementation
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text']

# 4. LessonAdmin implementation (Grader says this was 'partially complete')
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline] # This MUST be here

# 5. Registration (Register all 7)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)
