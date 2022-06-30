from django.test import TestCase

# Create your tests here.

from .models import studentmodel
class StudentTestcase(TestCase):
    def setUp(self):
        studentmodel.objects.create(id='57',name='sahana',age='25',email='sahana@gmail.com',phone='8310114088')

    def test_student_test(self):
        name1=studentmodel.objects.get(id='57',name='sahana',age='25',email='sahana@gmail.com',phone='8310114088')
        self.assertEqual(name1.name)
