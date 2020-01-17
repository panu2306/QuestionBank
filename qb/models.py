from django.db import models

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
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=64)
    lang = models.ManyToManyField(Language)

    def __str__(self):
        return self.choice_text

    


