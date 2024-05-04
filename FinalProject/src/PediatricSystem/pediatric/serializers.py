from rest_framework import serializers
from .models import Patient, MedicalRecord, Appointment
from rest_framework import serializers
from .models import Snippet


class PatientSerializer(serializers.ModelSerializer):
    class Meta:
        model = Patient
        fields = ("id", "name", "date_of_birth", "medical_history")


class MedicalRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = MedicalRecord
        fields = ("id", "patient", "diagnosis", "treatment_plan", "medications", "created_at")


class AppointmentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Appointment
        fields = ("id", "patient", "date_time", "purpose", "is_cancelled")

   

class SnippetSerializer(serializers.ModelSerializer):
    class Meta:
        model = Snippet
        fields = ['id', 'title', 'code', 'language', 'created_at']

