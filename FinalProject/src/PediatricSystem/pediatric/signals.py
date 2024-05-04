import csv
from pathlib import Path
from random import randint

from asgiref.sync import async_to_sync
from channels.layers import get_channel_layer

from django.core.files import File
from django.db.models.signals import post_save

from .consumers import SimplePatientConsumer
from .models import Patient

channel_layer = get_channel_layer()


# making sense of this example:
# - save_bookmark is the receiver function
# - Bookmark is the sender and post_save is the signal.
# - Use Case: Everytime a Bookmark is saved, the save_profile function will be executed.
def log_patient_to_csv(sender, instance, **kwargs):
    print("Patient signal: CSV")

    file = Path(__file__).parent.parent / "pedarch" / "domain" / "created_log.csv"
    print(f"Writing to {file}")

    # the with statement takes advantate of the context manager protocol: https://realpython.com/python-with-statement/#the-with-statement-approach
    # for reference, here is how open() works: https://docs.python.org/3/library/functions.html#open
    with open(file, "a+", newline="") as csvfile:
        logfile = File(csvfile)
        logwriter = csv.writer(
            logfile,
            delimiter=",",
        )
        logwriter.writerow(
            [
                    instance.id,
                    instance.name,
                    instance.date_of_birth,
                    instance.medical_history,
            ]
        )




# connect the signal to this receiver
post_save.connect(log_patient_to_csv, sender=Patient)

