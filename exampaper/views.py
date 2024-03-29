from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth import authenticate
from .models import Quiz, Question

# Create your views here.


def frontpage(request):
    return render(request, 'exampaper/frontpage.html')

def home(request):
    quiz = Quiz.objects.all()
    question =  Question.objects.all()
    quiz_questions = zip(quiz, question)
    context = {
        'quiz_questions' : quiz_questions
    }
    return render(request, 'exampaper/home.html', context)