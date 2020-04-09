from django.shortcuts import render
from django.http import HttpResponse
from .models import Question, Choice, Standard, Subject
from .forms import UserForm, UserProfileInfoForm

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
    return render(request, 'qb/index.html', context= None)

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