from rest_framework import serializers
from .models import studentmodel, deptmodel


class StudentmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = studentmodel
        fields = ('name','age', 'email', 'phone')

class DeptmodelSerializer(serializers.ModelSerializer):
    class Meta:
        model = deptmodel
        fields = "__all__"






