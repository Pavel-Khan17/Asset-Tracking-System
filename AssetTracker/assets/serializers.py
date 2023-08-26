from rest_framework import serializers
from .models import *

# serialisers to clean and formate data 
class CompanySerializer(serializers.ModelSerializer):
    employe = serializers.StringRelatedField(many=True)
    class Meta:
        model = CompanyModel
        fields = '__all__'

class EmployeeSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeModel
        fields = '__all__'

class AssetsSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsModel
        fields = '__all__'

class AssetsLogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = AssetsLog
        fields = '__all__'

class AssetsLogGetSerializer(serializers.ModelSerializer):
    asset = serializers.StringRelatedField()
    employee = serializers.StringRelatedField()
    class Meta:
        model = AssetsLog
        fields = '__all__'
