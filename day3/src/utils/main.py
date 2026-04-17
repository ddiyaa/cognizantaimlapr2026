import sys
import os
#add project root tp python path
project_root = os.path.abspath(os.path.join(os.path.dirname(__file__),'..','..'))
sys.path.append(project_root)   

from src.models import person
from conf.logger_conf import setup_logger
logger = setup_logger()
"""create person instance and access its attributes"""
def create_person():
    person_obj = person.Person(adharcardNo="1234-5678-9012", mobileNo=9876543210)
    print(f"Adharcard No: {person_obj.adharcardNo}")
    print(f"Mobile No: {person_obj.mobileNo}")
if __name__ == "__main__":
    create_person()

#update mobile number and check if it is valid and print details
person_obj = person.Person(adharcardNo="1234-5678-9012", mobileNo=9876543210)
person_obj.mobileNo = 23467890
print(f"Updated Mobile No: {person_obj.mobileNo}")
