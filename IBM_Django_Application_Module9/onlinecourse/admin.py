from django.contrib import admin
from .models import Instructor, Learner, Course, Lesson, Question, Choice, Submission

# Inline for Question in Lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Inline for Choice in Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Admin for Lesson
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Admin for Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Admin for Course
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonAdmin]

# Register all seven models
admin.site.register(Instructor)
admin.site.register(Learner)
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)