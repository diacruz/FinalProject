from django.db import transaction
from django.test import TestCase
from django.urls import reverse
from django.utils.timezone import localtime
from django.test import TestCase
from .models import Patient, MedicalRecord, Appointment
from django.test import TestCase
from django.utils.timezone import localtime
from .models import Patient
from .services.commands import AddPatientCommand
from .domain.model import DomainPatient


from pedarch.services.commands import (
   schedule_appointment,
   cancel_appointment,
   reschedule_appointment
)



class PatientModelTests(TestCase):
    def test_patient_creation(self):
        patient = Patient.objects.create(name="John Doe", date_of_birth="2000-01-01")
        self.assertEqual(patient.name, "John Doe")
        self.assertEqual(patient.date_of_birth, "2000-01-01")

class MedicalRecordModelTests(TestCase):
    def test_medical_record_creation(self):
        patient = Patient.objects.create(name="John Doe", date_of_birth="2000-01-01")
        medical_record = MedicalRecord.objects.create(patient=patient, diagnosis="Test Diagnosis", treatment_plan="Test Treatment Plan", medications="Test Medications")
        self.assertEqual(medical_record.patient, patient)
        self.assertEqual(medical_record.diagnosis, "Test Diagnosis")
        self.assertEqual(medical_record.treatment_plan, "Test Treatment Plan")
        self.assertEqual(medical_record.medications, "Test Medications")

class AppointmentModelTests(TestCase):
    def test_appointment_creation(self):
        patient = Patient.objects.create(name="John Doe", date_of_birth="2000-01-01")
        appointment = Appointment.objects.create(patient=patient, date_time="2022-01-01 10:00:00", purpose="Test Purpose")
        self.assertEqual(appointment.patient, patient)
        self.assertEqual(appointment.date_time, "2022-01-01 10:00:00")
        self.assertEqual(appointment.purpose, "Test Purpose")


class TestCommands(TestCase):
 def setUp(self):
        right_now = localtime().date()

        self.domain_patient_1 = DomainPatient(
            id=1,
            name="John Doe",
            date_of_birth="2000-01-01",
            gender="Male",
            address="123 Main St",
            phone_number="123-456-7890",
            date_added=right_now,
        )

        self.domain_patient_2 = DomainPatient(
            id=2,
            name="Jane Smith",
            date_of_birth="1995-05-15",
            gender="Female",
            address="456 Elm St",
            phone_number="987-654-3210",
            date_added=right_now,
        )

def test_command_add_patient(self):
        add_command = AddPatientCommand()
        add_command.execute(self.domain_patient_1)

        # Run checks
        # One patient object is inserted
        self.assertEqual(Patient.objects.count(), 1)

        # That object is the same as the one we inserted
        self.assertEqual(Patient.objects.get(id=1).name, self.domain_patient_1.name)
