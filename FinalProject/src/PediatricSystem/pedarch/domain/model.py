from datetime import date

class DomainPatient:
    """
    Represents a patient in the Pediatric Management System.
    """

    def __init__(self, id, name, date_of_birth, medical_history):
        """
        Initialize the Patient instance.
        
        Args:
            id (int): The unique identifier of the patient.
            name (str): The name of the patient.
            date_of_birth (str): The date of birth of the patient.
            medical_history (str): The medical history of the patient.
        """
        self.id = id
        self.name = name
        self.date_of_birth = date_of_birth
        self.medical_history = medical_history

    def __str__(self):
        """
        Return a string representation of the Patient instance.
        """
        return f"Patient: {self.name}"





# class DomainBookmark:
#     """
#     Bookmark domain model. Note, this is much simpler than P&G's domain model.
#     """

#     def __init__(self, id, title, url, notes, date_added):
#         self.id = id
#         self.title = title
#         self.url = url
#         self.notes = notes
#         self.date_added = date_added

#     def __str__(self):
#         return f"{self.title}"
