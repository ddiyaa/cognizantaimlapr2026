# role model defination
class Role(Person):
    def __init__(self, name: str, description: str, role: str):
        super().__init__(adharcardNo, mobileNo)
        self.__role = role
        self.__description = description
    #getter for description and role    
    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, value):
        self.__role = value 
    #getter for description
    @property
    def description(self):
        return self.__description