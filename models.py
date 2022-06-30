from django.contrib.auth.models import Group,Permission
from django.db import models
from rest_framework.reverse import reverse
from django.contrib.auth.models import User

# user = User.objects.create_user('Ashwini', 'ashwini@gmail.com', 'Welcome@123')
# user.last_name = '  S R'
# user.save()
#
#
# new_group, created = Group.objects.get_or_create(name='student')
#
# user = User.objects.get(username="ashwini") # get Some User.
# user.groups.add(new_group)
# # user = User.objects.get(username='ashwini')
class studentmodel(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    age = models.IntegerField()
    email = models.EmailField(max_length=30)
    phone = models.IntegerField()

    class Meta:
        db_table = "studentmodel"

class deptmodel(models.Model):
    deptname = models.CharField(max_length=100)
    facultyname = models.CharField(max_length=100)

    class Meta:
        db_table = "deptmodel"




def get_absolute_url(self):
    return reverse("show/", args=[str(self.id)])

def __str__(self):
    return 'id: {} , name: {},age: {},email:{} and phone{}'.format(self.id, self.name,self.age,self.email,self.phone)

