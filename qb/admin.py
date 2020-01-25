from django.contrib import admin
from .models import Question, Choice, Language, QuestionsInMultipleLanguage

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2
    max_num = 4

@admin.register(Question)
class QuestionAdmin(admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display = ('question_text', )
    fields = ('lang', 'question_text', 'pub_date')
    list_filter = ('lang', )
    search_fields = ('question_text', 'lang')
    filter_vertical = ('lang', )
    date_hierarchy = 'pub_date'
    """
    fieldsets = ((None, {
                    'fields': ('lang', )
                }),
                 ('Advanced Option', {
                    'classes': ('collapse',),
                    'fields': ('question_text', 'pub_date',),
                }),
            )
    """
class LanguageAdmin(admin.ModelAdmin):
    list_display = ('lang_name', 'lang_code')

admin.site.register(Language, LanguageAdmin)
admin.site.register(QuestionsInMultipleLanguage)
