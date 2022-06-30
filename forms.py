from django import forms
from .models import studentmodel, deptmodel


class studentform(forms.ModelForm):
    class Meta:
        model = studentmodel
        fields = "__all__"

class  deptform(forms.ModelForm):
    class Meta:
        model= deptmodel
        fields = "__all__"



#
# class studentform(forms.ModelForm):
#     id=forms.IntegerField()
#     name=forms.CharField(max_length=30)
#     age=forms.IntegerField()
#     email=forms.EmailField(max_length=30)
#     phone=forms.IntegerField()