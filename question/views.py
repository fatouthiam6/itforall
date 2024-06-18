from django.shortcuts import render

from question.models import Question


def index(request):
    return generate_questions(request)


def generate_questions(request):
    if request.method == 'GET':
        questions = Question.objects.all()
        return render(
            request=request,
            template_name='quiz/quiz.html',
            context={
                'questions': questions
            }
        )


def check_results(request):
    if request.method == 'POST':
        print(request.POST)
        answers = request.POST
        questions = Question.objects.all()
        true_answer = []
        wrong_answer = []
        score = 0
        for question in questions:
            print(question.correct_answer)
            if question.correct_answer == answers[str(question.id)]:
                true_answer.append(question.id)
                score += 1
            else:
                wrong_answer.append(answers[str(question.id)])

        return render(request=request, template_name="quiz/quiz.html", context={
            'answers': answers,
            'questions': questions,
            'score': score,
            'true_answer': true_answer,
            'wrong_answer': wrong_answer
        })
