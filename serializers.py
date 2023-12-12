from rest_framework import serializers
from rest_framework.serializers import ModelSerializer

class EmployeeSerializer(serializers.ModelSerializer):
    name = serializers.ModelSerializer()
    email = serializers.EmailField()
    company = serializers.CharField()
    from_date = serializers.DateField()
    qualification = serializers.CharField()
    age = serializers.IntegerField()
    gender = serializers.CharField()
    contact = serializers.IntegerField()
    address = serializers.CharField()


