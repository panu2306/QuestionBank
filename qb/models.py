from django.db import models
from django.utils import timezone

# Create your models here.

class Language(models.Model):
    lang_name = models.CharField(max_length=64)
    lang_code = models.CharField(max_length=2)

    def __str__(self):
        return self.lang_name
    

class Question(models.Model):
    question_text = models.CharField(max_length=264)
    lang = models.ManyToManyField(Language)
    pub_date = models.DateTimeField('date_published')

    def __str__(self):
        return self.question_text 

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    choice_text = models.CharField(max_length=64)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.choice_text

class QuestionsInMultipleLanguage(models.Model):
    question = models.ForeignKey(Question, on_delete=models.PROTECT)
    question_text = models.CharField(max_length=264)
    question_language = models.ForeignKey(Language, on_delete=models.PROTECT)

    def __str__(self):
        return f"{self.question_text} - {self.question_language}"
    



