from django.shortcuts import render, get_object_or_404, redirect
from .models import Course, Lesson, Question, Choice, Submission
from django.contrib.auth.decorators import login_required

@login_required
def submit(request, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    user = request.user

    if request.method == 'POST':
        # Get all selected choice IDs from POST
        selected_choices = request.POST.getlist('choice')

        # Create a submission
        submission = Submission.objects.create(user=user, lesson=lesson)
        submission.choices.set(selected_choices)
        submission.save()

        # Redirect to exam result page
        return redirect('show_exam_result', submission_id=submission.id)

    # If GET request, show lesson questions and choices
    questions = lesson.questions.all()
    context = {
        'lesson': lesson,
        'questions': questions
    }
    return render(request, 'onlinecourse/lesson_exam.html', context)

@login_required
def show_exam_result(request, submission_id):
    submission = get_object_or_404(Submission, id=submission_id)
    lesson = submission.lesson
    questions = lesson.questions.all()
    total_grade = 0
    obtained_grade = 0
    results = []

    for question in questions:
        total_grade += question.grade
        selected = submission.choices.filter(question=question)
        correct = question.choices.filter(is_correct=True)

        # Check if all correct choices were selected and no wrong choice
        if set(selected) == set(correct):
            obtained_grade += question.grade
            results.append({
                'question': question.text,
                'correct': True,
                'selected': selected
            })
        else:
            results.append({
                'question': question.text,
                'correct': False,
                'selected': selected
            })

    score_percentage = round((obtained_grade / total_grade) * 100, 2) if total_grade > 0 else 0

    context = {
        'submission': submission,
        'results': results,
        'score_percentage': score_percentage,
        'total_grade': total_grade,
        'obtained_grade': obtained_grade
    }
    return render(request, 'onlinecourse/exam_result.html', context)