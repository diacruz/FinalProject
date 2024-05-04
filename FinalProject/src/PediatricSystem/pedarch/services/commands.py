"""
This module utilizes the command pattern - https://en.wikipedia.org/wiki/Command_pattern - to 
specify and implement the business logic layer
"""
import sys
from abc import ABC, abstractmethod
from datetime import datetime
from injector import Injector, inject
import pytz

import requests
from django.db import transaction
from datetime import datetime

from pediatric.models import Patient, Appointment, MedicalRecord


class Command(ABC):
    @abstractmethod
    def execute(self, data):
        raise NotImplementedError("A command must implement the execute method")


class PythonTimeStampProvider:
    def __init__(self):
        self.now = datetime.now(pytz.UTC).isoformat()


def schedule_appointment(patient_id, date_time, purpose):
    """
    Command to schedule a new appointment for a patient.
    """
    try:
        appointment = Appointment.objects.create(patient_id=patient_id, date_time=date_time, purpose=purpose)
        return True, f"Appointment for {appointment.patient.name} scheduled successfully."
    except Exception as e:
        return False, f"Failed to schedule appointment: {str(e)}"

def cancel_appointment(appointment_id):
    """
    Command to cancel an existing appointment.
    """
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
        appointment.is_cancelled = True
        appointment.save()
        return True, "Appointment cancelled successfully."
    except Exception as e:
        return False, f"Failed to cancel appointment: {str(e)}"

def reschedule_appointment(appointment_id, new_date_time):
    """
    Command to reschedule an existing appointment.
    """
    try:
        appointment = Appointment.objects.get(pk=appointment_id)
        appointment.date_time = new_date_time
        appointment.save()
        return True, "Appointment rescheduled successfully."
    except Exception as e:
        return False, f"Failed to reschedule appointment: {str(e)}"
    

class AddPatientCommand:
    def execute(self, patient_data):
        """
        Adds a new patient to the system.

        Args:
        - patient_data (DomainPatient): Data of the patient to be added.

        Returns:
        - None
        """
        # Extract data from DomainPatient object
        patient = Patient(
            name=patient_data.name,
            date_of_birth=patient_data.date_of_birth,
            gender=patient_data.gender,
            address=patient_data.address,
            phone_number=patient_data.phone_number,
            date_added=patient_data.date_added,
        )
        
        # Save the patient object to the database
        patient.save()



       


# class AddBookmarkCommand(Command):
#     """
#     Using the django orm and transactions to add a bookmark
#     """

#     @inject
#     def __init__(self, now: PythonTimeStampProvider = PythonTimeStampProvider()):
#         self.now = now

#     def execute(self, data: DomainBookmark, timestamp=None):
#         bookmark = Bookmark(data.id, data.title, data.url, data.notes, timestamp)
#         bookmark.timestamp = self.now

#         # again, we skip the ouw with django's transaction management
#         with transaction.atomic():
#             bookmark.save()


# class ListBookmarksCommand(Command):
#     """
#     swapping in Django ORM for the database manager
#     """

#     def __init__(self, order_by="date_added"):
#         self.order_by = order_by

#     def execute(self, data=None):
#         return Bookmark.objects.all().order_by(self.order_by)


# class DeleteBookmarkCommand(Command):
#     """
#     Using the django ORM to delete a bookmark
#     """

#     def execute(self, data: DomainBookmark):
#         bookmark = Bookmark.objects.get(url=data.url)
#         with transaction.atomic():
#             bookmark.delete()


# class EditBookmarkCommand(Command):
#     """
#     Using the django ORM to update a bookmark
#     """

#     def execute(self, data: DomainBookmark):
#         bookmark = Bookmark.update_from_domain(data)
#         with transaction.atomic():
#             bookmark.save()
