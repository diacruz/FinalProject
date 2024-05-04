from django.contrib import admin
from .models import Patient, MedicalRecord, Appointment, Event, Command

@admin.register(Patient)
class PatientAdmin(admin.ModelAdmin):
    list_display = ('name', 'date_of_birth',)
    search_fields = ('name',)

@admin.register(MedicalRecord)
class MedicalRecordAdmin(admin.ModelAdmin):
    list_display = ('patient', 'diagnosis', 'created_at',)
    list_filter = ('created_at',)
    search_fields = ('patient__name',)

@admin.register(Appointment)
class AppointmentAdmin(admin.ModelAdmin):
    list_display = ('patient', 'date_time', 'purpose', 'is_cancelled',)
    list_filter = ('date_time', 'is_cancelled',)
    search_fields = ('patient__name', 'purpose',)

@admin.register(Event)
class EventAdmin(admin.ModelAdmin):
    list_display = ('name', 'occurred_at',)
    list_filter = ('occurred_at',)
    search_fields = ('name',)

@admin.register(Command)
class CommandAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)
