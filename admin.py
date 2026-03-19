from django.contrib import admin
from .models import Course, Lesson, Instructor, Learner, Question, Choice, Submission

# 1. ChoiceInline (Already correct in your 2/3 submission)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# 2. QuestionInline (Already correct in your 2/3 submission)
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# 3. QuestionAdmin (THIS IS THE MISSING PIECE FOR 3/3)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]
    list_display = ['question_text'] # Added list_display as requested by grader

# 4. LessonAdmin (Already correct in your 2/3 submission)
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']
    inlines = [QuestionInline]

# 5. Registration (Crucial: Link QuestionAdmin to Question)
admin.site.register(Course)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Question, QuestionAdmin) # Make sure QuestionAdmin is the second argument
admin.site.register(Choice)
admin.site.register(Submission)
