from django.contrib import admin
from .models import Instructor, Learner, Course, Lesson, Question, Choice, Submission

# Inline for Choice in Question
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 2

# Inline for Question in Lesson
class QuestionInline(admin.TabularInline):
    model = Question
    extra = 1

# Inline for Lesson in Course
class LessonInline(admin.TabularInline):
    model = Lesson
    extra = 1

# Admin for Lesson
class LessonAdmin(admin.ModelAdmin):
    inlines = [QuestionInline]

# Admin for Question
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInline]

# Admin for Course
class CourseAdmin(admin.ModelAdmin):
    inlines = [LessonInline]

# Register Instructor and Learner normally
admin.site.register(Instructor)
admin.site.register(Learner)

# Register Course with inline Lessons
admin.site.register(Course, CourseAdmin)

# Register Lesson with inline Questions
admin.site.register(Lesson, LessonAdmin)

# Register Question with inline Choices
admin.site.register(Question, QuestionAdmin)

# Register Choice and Submission normally
admin.site.register(Choice)
admin.site.register(Submission)