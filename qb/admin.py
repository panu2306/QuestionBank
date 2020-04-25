from django.contrib import admin
from django.urls import path 
from django.shortcuts import render
from django import forms
from django.utils import timezone

from .models import Question, Choice, Language, Subject, Standard, UserProfileInfo

# Register your models here.

class QuestionAdminForm(forms.ModelForm):
    class Meta:
        model = Question
        fields = '__all__'
        widgets = {
            'question_name': forms.Textarea(attrs={'cols': 50, 'rows': 10}),
        }
        #localized_fields = ('question_name',)
    
    def clean(self):
        cleaned_data = super().clean()
        pub_date = cleaned_data.get('pub_date')
        now = timezone.now()
        if(pub_date > now):
            raise forms.ValidationError("You are entering the future date.")

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2
    max_num = 4 

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    form = QuestionAdminForm
    list_display = ('question_id', 'subject', 'question_name', 'lang', 'pub_date')
    list_display_links = ('question_id', )
    list_editable = ('lang', )
    inlines = [
        ChoiceInLine,
    ]
    list_filter = ('question_id', 'lang',)
    def get_urls(self):
        urls = super().get_urls()
        my_urls = [
            path('my_view/', self.admin_site.admin_view(self.my_view, cacheable=True)),
        ]
        return my_urls + urls
    def my_view(self, request):
        return render(request, 'admin/qb/multilingual.html', context=None)
        
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('lang_name', 'lang_code')

admin.site.register(Language, LanguageAdmin)
admin.site.register(Subject)
admin.site.register(Standard)
admin.site.register(UserProfileInfo)
