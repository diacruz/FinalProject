from django.urls import include, path
from rest_framework import routers

from . import views

router = routers.DefaultRouter()
router.register(r"patients", views.PatientViewSet)
router.register(r"medical-records", views.MedicalRecordViewSet)
router.register(r"appointments", views.AppointmentViewSet)

app_name = "pediatric"

urlpatterns = [
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
    path("", include(router.urls)),
]

# Add the router's URLs to the urlpatterns
urlpatterns += router.urls
