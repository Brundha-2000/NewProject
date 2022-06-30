from django.contrib import admin
# from django.contrib.auth.models import Permission, Group
#
# from django.contrib.contenttypes.models import ContentType
# from rest_framework.authtoken.admin import User
# # from django.contrib.auth.models import User
# user = User.objects.create_user('ashwini ','ashwini@xyz.com','sn@pswrd')
# user.last_name = '  S R'
# user.save()
# from rest_framework.authtoken.admin import User
from import_export.admin import  ImportExportModelAdmin

from .models import studentmodel,deptmodel


# user = User.objects.create_user('Hrashitha_Mohan', 'brundha.j@slkgeoup.com', 'Slksoft@123')
# user.first_name = 'Asiya'
# user.last_name = 'L C'
# user.save()
# from django.contrib.auth.models import User
# u = User.objects.create_user(username='ramya')
# u.has_perm('auth.change_user')

# new_group, created = Group.objects.get_or_create(name='student1') #creating new group
# user = User.objects.get(username="Hrashitha_Mohan") # get Some User.
# user.groups.add(new_group)

# user = User.objects.get(username="ashwini") # get Some User.
# user.groups.add(new_group)

# # group = Group(name="Author")
# # group.save()
# # user = User.objects.get(username="Johndoe") # get Some User.
# # user.groups.add(group)

# user = User.objects.get(username = 'ahswini')
# user.groups.add(new_group)

# ct = ContentType.objects.get_for_model(studentmodel)   #giving permissions to group
# permission = Permission.objects.create(codename ='can_go_haridwar',
#                                         name ='Can go to Haridwar',
#                                                 content_type = ct)
# new_group.permissions.add(permission)

# Register your models here.


class studentadmin(ImportExportModelAdmin,admin.ModelAdmin):
    list_display = ['id','name','age','email','phone']
    search_fields = ['name']

    def has_add_permission(self, request):
        return True

class deptadmin(admin.ModelAdmin):
    list_display = ['deptname','facultyname']

def delete(self,request,obj=None):
    return True
admin.site.register(studentmodel,studentadmin)
admin.site.register(deptmodel,deptadmin)

