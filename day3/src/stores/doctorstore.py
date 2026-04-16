"""create doctor crud operations"""
from exceptions.doctor_not_found_exception import DoctorNotFoundException
from models.doctor import Doctor
import sys
import os

#add project root tp python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.append(project_root)

from conf.logger_conf import setup_logger
logger = setup_logger()
class DoctorStore:
    def __init__(self):
        self.doctors = []

    def add_doctor(self, doctor: Doctor):
        logger.info(f"adding doctor: {doctor.name}")
        self.doctors.append(doctor)

    def get_doctor_by_id(self, doctor_id: int) -> Doctor:
        logger.info(f"getting doctor by id: {doctor_id}")
        for doctor in self.doctors:
            if doctor.id == doctor_id:
                return doctor
        raise DoctorNotFoundException(f"Doctor with id {doctor_id} not found")

    def get_all_doctors(self) -> list[Doctor]:
        logger.info("getting all doctors")  
        return self.doctors

    def update_doctor(self, doctor_id: int, name: str = None, specialty: str = None) -> bool:
        logger.info(f"updating doctor: {doctor_id}")
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            if name:
                doctor.name = name
            if specialty:
                doctor.specialty = specialty
            return True
        return False

    def delete_doctor(self, doctor_id: int) -> bool:
        logger.info(f"deleting doctor: {doctor_id}")
        doctor = self.get_doctor_by_id(doctor_id)
        if doctor:
            self.doctors.remove(doctor)
            return True
        return False