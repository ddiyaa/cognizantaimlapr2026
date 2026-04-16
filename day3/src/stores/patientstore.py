#create patient crud operations
from exceptions.patient_not_found_exception import PatientNotFoundException
from models.patient import Patient
import sys
import os
#add project root tp python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.append(project_root)   
from conf.logger_conf import setup_logger
logger = setup_logger()
class PatientStore:
    def __init__(self):
        self.patients = []

    def add_patient(self, patient: Patient):
        logger.info(f"adding patient: {patient.name}")
        self.patients.append(patient)

    def get_patient_by_id(self, patient_id: int) -> Patient:
        logger.info(f"getting patient by id: {patient_id}")
        for patient in self.patients:
            if patient.id == patient_id:
                return patient
        raise PatientNotFoundException(f"Patient with id {patient_id} not found")   
    def get_all_patients(self) -> list[Patient]:
        logger.info("getting all patients")  
        return self.patients
    def update_patient(self, patient_id: int, name: str = None, age: int = None) -> bool:
        logger.info(f"updating patient: {patient_id}")
        patient = self.get_patient_by_id(patient_id)
        if patient:
            if name:
                patient.name = name
            if age:
                patient.age = age
            return True
        return False
    def delete_patient(self, patient_id: int) -> bool:
        logger.info(f"deleting patient: {patient_id}")
        patient = self.get_patient_by_id(patient_id)
        if patient:
            self.patients.remove(patient)
            return True
        return False
    