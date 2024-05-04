import asyncio
import datetime
import json

from channels.consumer import AsyncConsumer
from channels.generic.http import AsyncHttpConsumer

from .models import Patient


class SimplePatientConsumer(AsyncConsumer):
    async def print_patient(self, message):
        print(f"WORKER: Patient: {message['data']}")


class PatientConsumer(AsyncHttpConsumer):
    async def handle(self, body):
        # Get all patients
        patients = Patient.objects.all()
        # Serialize the patients
        data = json.dumps(
            [{"name": patient.name, "date_of_birth": patient.date_of_birth} for patient in patients]
        )
        # Send the serialized data as a JSON response
        await self.send_response(
            200, data, headers=[(b"Content-Type", b"application/json")]
        )

    # Server-send event https://developer.mozilla.org/en-US/docs/Web/API/Server-sent_events
    async def handle(self, body):
        await self.send_headers(
            headers=[
                (b"Cache-Control", b"no-cache"),
                (b"Content-Type", b"text/event-stream"),
                (b"Transfer-Encoding", b"chunked"),
            ]
        )
        while True:
            payload = "data: %s\n\n" % datetime.datetime.now().isoformat()
            await self.send_body(payload.encode("utf-8"), more_body=True)
            await asyncio.sleep(1)

    async def send_patient(self, patient):
        # Serialize the patient
        data = json.dumps({"name": patient.name, "date_of_birth": patient.date_of_birth})
        # Send the serialized data as a JSON response
        await self.channel_layer.send(
            "patients-add", {"type": "send.patient", "data": data}
        )
