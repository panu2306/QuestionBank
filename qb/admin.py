from django.contrib import admin
from .models import Question, Choice, Language

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2
    max_num = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    list_display = ('question_id', 'question_name', 'lang', 'pub_date')
    list_display_links = ('question_name', )
    list_editable = ('lang', )
    inlines = [
        ChoiceInLine,
    ]
    list_filter = ('question_id', 'lang',)
    
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('lang_name', 'lang_code')

admin.site.register(Language, LanguageAdmin)
