from django.shortcuts import render

from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from .models import Patient, MedicalRecord, Appointment

# retrieves all patients from the database and renders them in the index template
def index(request):
    patients = Patient.objects.all()
    return render(request, 'management/index.html', {'patients': patients})

#retrieves details of a specific patient, including their medical records and appointments, and renders them in the patient detail template
def patient_detail(request, patient_id):
    patient = get_object_or_404(Patient, pk=patient_id)
    medical_records = MedicalRecord.objects.filter(patient=patient)
    appointments = Appointment.objects.filter(patient=patient)
    return render(request, 'management/patient_detail.html', {'patient': patient, 'medical_records': medical_records, 'appointments': appointments})

#Handles the creation of new appointments for a specific patient
def create_appointment(request, patient_id):
    if request.method == 'POST':
        patient = get_object_or_404(Patient, pk=patient_id)
        date_time = request.POST['date_time']
        purpose = request.POST['purpose']
        appointment = Appointment(patient=patient, date_time=date_time, purpose=purpose)
        appointment.save()
        return HttpResponse("Appointment created successfully!")
    else:
        return render(request, 'management/create_appointment.html', {'patient_id': patient_id})

