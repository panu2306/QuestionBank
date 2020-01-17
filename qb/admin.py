from django.contrib import admin
from .models import Question, Choice

from localized_fields.admin import LocalizedFieldsAdminMixin

# Register your models here.

class ChoiceInLine(admin.TabularInline):
    model = Choice
    extra = 2
    max_num = 4

class QuestionAdmin(LocalizedFieldsAdminMixin, admin.ModelAdmin):
    inlines = [ChoiceInLine]
    list_display = ('question_text', )
    fields = ('question_text', 'pub_date')
    search_fields = ('question_text',)

admin.site.register(Question, QuestionAdmin)