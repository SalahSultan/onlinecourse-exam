from django.contrib import admin
from .models import Course, Lesson, Question, Choice, Submission
from django.contrib.auth.models import User

# Inline for Choices (shown inside Question)
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2  # number of empty choices to show
    min_num = 1
    max_num = 10

# Inline for Questions (shown inside Lesson)
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1
    min_num = 1
    max_num = 10

# Admin for Questions (editable Choices inside)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'lesson', 'grade')
    inlines = [ChoiceInline]

# Admin for Lessons (editable Questions inside)
class LessonAdmin(admin.ModelAdmin):
    list_display = ('title', 'course', 'order')
    inlines = [QuestionInline]

# Admin for Courses
class CourseAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'created_at')

# Register models with admin
admin.site.register(Course, CourseAdmin)
admin.site.register(Lesson, LessonAdmin)
admin.site.register(Question, QuestionAdmin)
admin.site.register(Choice)
admin.site.register(Submission)