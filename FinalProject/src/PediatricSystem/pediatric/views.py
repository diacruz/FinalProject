from django.contrib.auth.models import User
from rest_framework import generics, permissions, renderers, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from .models import Patient, MedicalRecord, Appointment, Snippet
from .permissions import IsOwnerOrReadOnly
from .serializers import PatientSerializer, MedicalRecordSerializer, AppointmentSerializer, SnippetSerializer
from rest_framework import serializers
from .models import Snippet

# Create your views here.
class PatientViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows patients to be viewed or edited.
    """

    queryset = Patient.objects.all()
    serializer_class = PatientSerializer


class MedicalRecordViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows medical records to be viewed or edited.
    """

    queryset = MedicalRecord.objects.all()
    serializer_class = MedicalRecordSerializer


class AppointmentViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows appointments to be viewed or edited.
    """

    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer


class SnippetViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows snippets to be viewed or edited.
    """

    queryset = Snippet.objects.all()
    serializer_class = SnippetSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly, IsOwnerOrReadOnly]

    @action(detail=True, renderer_classes=[renderers.StaticHTMLRenderer])
    def highlight(self, request, *args, **kwargs):
        snippet = self.get_object()
        return Response(snippet.highlighted)

    def perform_create(self, serializer):
        serializer.save(owner=self.request.user)
