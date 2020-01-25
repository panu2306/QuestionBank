from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice
from .forms import NameForm

# Create your views here.
def index(request):
    questions = Question.objects.all()
    choices = Choice.objects.all()

    context = {
        'questions':questions,
        'choices':choices,
    }
    return render(request, 'qb/index.html', context=context)

def try_form(request):
    if request.method == 'POST':
        form = NameForm(request.POST)
        if form.is_valid():
            return render(request, 'qb/thanks.html', context=None)
    else:
        form = NameForm()
    return render(request, 'qb/try_form.html', context={'form': form})

def acknowledge(request):
    return HttpResponse("Form Submitted Successfully!!!"    )