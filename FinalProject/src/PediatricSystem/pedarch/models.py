from django.db import models

from django.db import models
from datetime import datetime

#represents a patient with attributes like name, date of birth, and medical history
class Patient(models.Model):
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    medical_history = models.TextField(blank=True)

    def __str__(self):
        return self.name
#stores medical records associated with a patient, including diagnosis, treatment plan, and medications
class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    medications = models.TextField()
    created_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return f"Medical Record for {self.patient.name}"
#manages patient appointments with attributes like date and purpose
class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    purpose = models.TextField()
    is_cancelled = models.BooleanField(default=False)

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.date_time}"
#represents events that occur within the system, such as appointment scheduling or medical procedures.\
class Event(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    occurred_at = models.DateTimeField(default=datetime.now)

    def __str__(self):
        return self.name
#defines commands that trigger specific actions within the system
class Command(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()

    def __str__(self):
        return self.name

