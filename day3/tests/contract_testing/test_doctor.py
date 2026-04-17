#test for doctor contract

import sys
import os
import pytest
import csv
#add project root tp python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.append(project_root)

from conf.logger_conf import setup_logger
"""
entry point for the healthcare application
"""
logger = setup_logger()
from src.models.doctor import Doctor

#test for doctor object created
@pytest.fixture
def initialize_doctor():
    doctor = Doctor(id= 1, name="Dr. Smith", specialty="Cardiology")
    return doctor
def read_doctors_from_csv(file_path):
    doctor_data = []
    with open('tests/doctors.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            doctor_data.append((int(row['id']), row['name'], row['specialty']))
    return doctor_data

def test_doctor_creation(initialize_doctor):
    doctor = initialize_doctor
    assert doctor.id == 1
    assert doctor.name == "Dr. Smith"
    assert doctor.specialty == "Cardiology"

@pytest.mark.parametrize("id, name, specialty", [
    (1, "Dr. Smith", "Cardiology"),
    (2, "Dr. Johnson", "Neurology"),
    (3, "Dr. Lee", "Pediatrics")
])
def test_doctor_creation_parametrize(id, name, specialty):
    doctor = Doctor(id=id, name=name, specialty=specialty)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialty == specialty

@pytest.mark.parametrize("id, name, specialty", read_doctors_from_csv('tests/doctors.csv'))
def test_doctor_from_csv(id, name, specialty):
    doctor = Doctor(id=id, name=name, specialty=specialty)
    assert doctor.id == id
    assert doctor.name == name
    assert doctor.specialty == specialty

