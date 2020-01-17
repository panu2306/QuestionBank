from django.db import models
from localized_fields.fields import LocalizedField, LocalizedCharField
from django.utils import translation

# Create your models here.
    
class Question(models.Model):
    question_text = LocalizedField(required=True)
    pub_date = models.DateTimeField('date_published')
    
    def __str__(self):
        return str(self.question_text)
    
    

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = LocalizedCharField(required=True)

    def __str__(self):
        return str(self.choice_text)
