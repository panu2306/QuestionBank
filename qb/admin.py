from django.contrib import admin
from .models import Question, Choice

# Register your models here.
#admin.site.register(Question)
admin.site.register(Choice)
 
@admin.register(Question)
class VenueAdmin(admin.ModelAdmin):
    list_display = ('question_text', 'lang')
    #ordering = ('name',)
    # search_fields = ('name', 'address')