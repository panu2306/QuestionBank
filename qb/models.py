from django.db import models
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User

# Create your models here.
class UserProfileInfo(models.Model):
    user = models.OneToOneField(User, on_delete=models.PROTECT)

    portfolio_site = models.URLField(blank=True)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.user.username

class Standard(models.Model):
    standard = models.CharField(max_length=64)

    def __str__(self):
        return self.standard

class Subject(models.Model):
    sub_name = models.CharField(max_length=64)
    standard = models.ManyToManyField(Standard)

    def __str__(self):
        return self.sub_name

class Language(models.Model):
    lang_name = models.CharField(max_length=64)
    lang_code = models.CharField(max_length=2)
    
    def __str__(self):
        return self.lang_name
    

class Question(models.Model):
    question_id = models.IntegerField()
    question_name = models.CharField(max_length=264)
    lang = models.ForeignKey(Language, on_delete=models.PROTECT)
    pub_date = models.DateTimeField('date_published')
    subject = models.ForeignKey('Subject', on_delete=models.PROTECT)

    class Meta:
        unique_together = ('question_id', 'lang',)

    def __str__(self):
        return self.question_name

class Choice(models.Model):
    question = models.ForeignKey(Question, on_delete=models.CASCADE)
    choice_text = models.CharField(max_length=64)
    lang = models.ForeignKey(Language, on_delete=models.PROTECT)

    def __str__(self):
        return self.choice_text

    def save(self, *args, **kwargs):
        # print(self.question.lang)
        # print(self.lang)
        if(self.lang != self.question.lang):
            print('Your choice', self.choice_text, 'is not valid.')
            raise ValidationError("Can't Save") 
        super(Choice, self).save(*args, **kwargs)    
    
