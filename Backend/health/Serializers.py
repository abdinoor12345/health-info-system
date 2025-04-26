from rest_framework import serializers
from .models import HealthProgram, Client, Enrollment

class HealthProgramSerializer(serializers.ModelSerializer):
    class Meta:
        model = HealthProgram
        fields = ['id', 'name', 'description']

class ClientSerializer(serializers.ModelSerializer):
    programs = HealthProgramSerializer(many=True, read_only=True)

    class Meta:
        model = Client
        fields = ['id', 'first_name', 'last_name', 'gender', 'date_of_birth', 'contact_number', 'email', 'address', 'programs']

class EnrollmentSerializer(serializers.ModelSerializer):
    client = ClientSerializer(read_only=True)
    program = HealthProgramSerializer(read_only=True)
    
    class Meta:
        model = Enrollment
        fields = ['id', 'client', 'program', 'date_enrolled']
class EnrollmentCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Enrollment
        fields = ['client', 'program']
