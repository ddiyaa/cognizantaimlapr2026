#person model defination
import re
class Person:
    def __init__(self, adharcardNo: str, mobileNo: str):
        self.__adharcardNo = adharcardNo
        self.__mobileNo = mobileNo

#getter for mobileNo
    @property
    def mobileNo(self):
        return self.__mobileNo
#getter for adharcardNo
    @property
    def adharcardNo(self):
        return self.__adharcardNo

#setter for mobileNo and check if it is valid
    @mobileNo.setter
    def mobileNo(self, value):
        if re.match(r'^\d{10}$', value):
            self.__mobileNo = value
        else:
            raise ValueError("Invalid mobile number. It should be a 10-digit number.")  
    
