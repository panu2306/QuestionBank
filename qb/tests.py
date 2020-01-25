import datetime
from django.test import TestCase
from django.utils import timezone

from .models import Question, Language, Choice

# Create your tests here.
class ModelQuestionTest(TestCase):
    
    
    """
        To check mentined field names are same as in the database.
    """
    def test_field_names(self):
        field_names = [
            field.name for field in Question._meta.get_fields()
            ]
        expected_field_names = ["choice", "id", "question_text", "pub_date", "lang"]
        self.assertEqual(expected_field_names, field_names)
