from django.contrib import admin
from .models import Course, Lesson, Instructor, Question, Choice # plus others

# ChoiceInline implementation
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 4

# QuestionInline implementation
class QuestionInline(admin.StackedInline):
    model = Question
    extra = 2

# QuestionAdmin implementation
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# LessonAdmin implementation
class LessonAdmin(admin.ModelAdmin):
    list_display = ['title']

# Registering the classes
admin.site.register(Question, QuestionAdmin)
admin.site.register(Lesson, LessonAdmin)
# ... register Course, Instructor, etc.
