from django.views import generic
from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice, Standard, Subject
from .forms import UserForm, UserProfileInfoForm

# Create your views here.

def index(request):
    context = {}
    standard_list = Standard.objects.all()
    context['standard_list'] = standard_list
    return render(request, 'qb/index.html', context=context)

def register(request):

    registered   = False
    
    if(request.method == 'POST'):
        user_form = UserForm(data=request.POST)
        profile_form = UserProfileInfoForm(data=request.POST)

        if(user_form.is_valid and profile_form.is_valid):
            user = user_form.save()
            user.set_password(user.password)
            user.save()

            profile = profile_form.save(commit=False)
            profile.user = user

            if('profile_pic' in request.FILES):
                profile.profile_pic = request.FILES['profile_pic']
            
            profile.save()

            registered = True 
        else:
            print(user_form.errors, profile_form.errors)
    else:
        user_form = UserForm()
        profile_form = UserProfileInfoForm()
    
    return render(request, 'qb/registration.html', context={'profile_form': profile_form, 'user_form': user_form, 'registered': registered})

class QuestionListView(generic.ListView):
    model = Question
    context_object_name = 'question_list'

def question_detail(request, id):
    context = {}
    question_text = Question.objects.get(question_id=id)
    choices = Choice.objects.filter(question__question_name=question_text)
    context['question_text'] = question_text
    context['choices'] = choices
    return render(request, 'qb/question_details.html', context=context)

class AboutView(generic.TemplateView):
    template_name = 'qb/about.html'
















