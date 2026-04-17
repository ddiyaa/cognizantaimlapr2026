#write test case for doctore not found exception
import sys
import os
import pytest
#add project root tp python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.append(project_root)

from conf.logger_conf import setup_logger
"""
entry point for the healthcare application
"""
logger = setup_logger()
from src.models.doctor import Doctor
from src.exceptions.doctor_not_found_exception import DoctorNotFoundException
from src.stores.doctorstore import DoctorStore

def test_doctor_not_found_exception():
    doctorstore = DoctorStore()
    with pytest.raises(DoctorNotFoundException):
        doctorstore.get_doctor_by_id(999)  # Assuming 999 is an ID that does not exist
