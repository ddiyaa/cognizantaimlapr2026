#create appointment model
import typing
from datetime import date, time
from doctor import Doctor
from patient import Patient 
class Appointment:
    def __init__(self, id: int, patient_id: int, doctor_id: int, date: str ,time:time):
        self.appointment_id = id
        self.patient_id = patient_id
        self.doctor_id = doctor_id
        self.date = date
        self.time = time

    def __str__(self):
        return f"Appointment(id={self.id}, Patient ID= {self.patient_id}, Doctor ID= {self.doctor_id}, Date= {self.date})"