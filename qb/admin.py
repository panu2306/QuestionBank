from django.contrib import admin
from django.urls import path 
from django.shortcuts import render

from .models import Question, Choice, Language

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2
    max_num = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'question_name', 'lang', 'pub_date')
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
        return render(request, 'multilingual.html', context=None)
    #change_form_template = 'admin/multilingual.html'




class LanguageAdmin(admin.ModelAdmin):
    list_display = ('lang_name', 'lang_code')

admin.site.register(Language, LanguageAdmin)
