from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice, Standard, Subject

# Create your views here.
# def index(request):
#     questions = Question.objects.all()
#     choices = Choice.objects.all()

#     context = {
#         'questions':questions,
#         'choices':choices,
#     }
#     return render(request, 'qb/index.html', context=context)

def index(request):
    standard_list = Standard.objects.all()
    print(standard_list)
    return render(request, 'qb/index.html', context= {'standard_list': standard_list})

def acknowledge(request):
    return HttpResponse("Form Submitted Successfully!!!")