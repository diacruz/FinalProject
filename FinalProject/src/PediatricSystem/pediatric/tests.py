from django.test import TestCase


from .models import Patient

from django.test import TestCase
from .models import Patient, MedicalRecord, Appointment


class PatientModelTestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.patient = Patient.objects.create(name="Test Patient", date_of_birth="2020-01-01")

    def test_patient_creation(self):
        # Test patient creation
        self.assertEqual(self.patient.name, "Test Patient")
        self.assertEqual(self.patient.date_of_birth, "2020-01-01")


class MedicalRecordModelTestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.patient = Patient.objects.create(name="Test Patient", date_of_birth="2020-01-01")
        self.medical_record = MedicalRecord.objects.create(patient=self.patient, diagnosis="Test Diagnosis")

    def test_medical_record_creation(self):
        # Test medical record creation
        self.assertEqual(self.medical_record.diagnosis, "Test Diagnosis")


class AppointmentModelTestCase(TestCase):
    def setUp(self):
        # Set up test data
        self.patient = Patient.objects.create(name="Test Patient", date_of_birth="2020-01-01")
        self.appointment = Appointment.objects.create(patient=self.patient, date_time="2024-05-01T09:00:00", purpose="Test Purpose")

    def test_appointment_creation(self):
        # Test appointment creation
        self.assertEqual(self.appointment.purpose, "Test Purpose")




