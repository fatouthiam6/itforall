from django import template
from django.shortcuts import render, redirect
from exercise.models import Exercise


def index(request):
    exercise = Exercise.objects.all().first()
    return redirect("exercise:show_exercise", exercise.pk)


def correct_exercise(request, id):
    exercise = Exercise.objects.get(pk=id)
    if request.POST['answer'] == exercise.correct_answer:
        return redirect("exercise:corrected_exercise", id, 'true')
    else:
        return redirect("exercise:corrected_exercise", id, 'false')


def corrected_exercise(request, id, correct):
    is_correct = correct == 'true'
    exercise = Exercise.objects.get(pk=id)
    next_id = exercise.id + 1
    return render(request=request,
                  template_name='exercise/exercise.html',
                  context={
                      'exo': exercise,
                      'is_correct': is_correct,
                      'next_id': next_id
                  }
                  )


def show_exercise(request, id):
    exercise = Exercise.objects.get(pk=id)
    next_id = exercise.id + 1
    return render(
        request=request,
        template_name='exercise/exercise.html',
        context={
            'exo': exercise,
            'next_id': next_id
        }
    )
