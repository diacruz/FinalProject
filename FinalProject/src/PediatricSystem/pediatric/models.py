from django.db import models
from pygments.lexers import get_all_lexers
from pygments.styles import get_all_styles
from pygments.lexers import get_lexer_by_name
from pygments.formatters.html import HtmlFormatter
from pygments import highlight
from pedarch.domain.model import DomainPatient


# pygments stuff
LEXERS = [item for item in get_all_lexers() if item[1]]
LANGUAGE_CHOICES = sorted([(item[1][0], item[0]) for item in LEXERS])
STYLE_CHOICES = sorted([(item, item) for item in get_all_styles()])

class Patient(models.Model):
    id = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=100)
    date_of_birth = models.DateField()
    medical_history = models.TextField()

    def __str__(self):
        return self.name

    @staticmethod
    def update_from_domain(domain_patient: DomainPatient):
        """
        Update or create a Patient instance from a DomainPatient instance.
        """
        try:
            patient = Patient.objects.get(id=domain_patient.id)
        except Patient.DoesNotExist:
            patient = Patient(id=domain_patient.id)

        patient.name = domain_patient.name
        patient.date_of_birth = domain_patient.date_of_birth
        patient.medical_history = domain_patient.medical_history
        patient.save()

    def to_domain(self) -> DomainPatient:
        """
        Convert a Patient instance to a DomainPatient instance.
        """
        return DomainPatient(
            id=self.id,
            name=self.name,
            date_of_birth=self.date_of_birth,
            medical_history=self.medical_history,
        )

class MedicalRecord(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    diagnosis = models.TextField()
    treatment_plan = models.TextField()
    medications = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Medical Record for {self.patient.name}"

class Appointment(models.Model):
    patient = models.ForeignKey(Patient, on_delete=models.CASCADE)
    date_time = models.DateTimeField()
    purpose = models.TextField()
    is_cancelled = models.BooleanField(default=False)


class Snippet(models.Model):
    created = models.DateTimeField(auto_now_add=True)
    title = models.CharField(max_length=100, blank=True, default="")
    code = models.TextField()
    linenos = models.BooleanField(default=False)
    language = models.CharField(
        choices=LANGUAGE_CHOICES, default="python", max_length=100
    )
    style = models.CharField(choices=STYLE_CHOICES, default="friendly", max_length=100)
    owner = models.ForeignKey(
        "auth.User", related_name="snippets", on_delete=models.CASCADE
    )
    highlighted = models.TextField()

    

    def __str__(self):
        return f"Appointment for {self.patient.name} on {self.date_time}"
    
    


