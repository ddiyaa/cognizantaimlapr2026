import sys
import os
import pytest
import csv

#test for patient contract
#add project root tp python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.append(project_root)

from conf.logger_conf import setup_logger
"""
entry point for the healthcare application
"""
logger = setup_logger()
from src.models.patient import Patient

#test for patient using csv file
def read_patients_from_csv(file_path):
    patient_data = []
    with open('tests/patients.csv', mode='r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            patient_data.append((int(row['id']), row['name'], int(row['age']), int(row['doctor_id'])))
    return patient_data
@pytest.mark.parametrize("id, name, age, doctor_id", read_patients_from_csv('tests/patients.csv'))
def test_patient_from_csv(id, name, age, doctor_id):
    patient = Patient(id=id, name=name, age=age, doctor_id=doctor_id)
    assert patient.id == id
    assert patient.name == name
    assert patient.age == age
    assert patient.doctor_id == doctor_id

