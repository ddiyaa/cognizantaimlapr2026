import typing
class Patient:
    def __init__(self, id: int, name: str, age: int, doctor_id: int):
        self.id = id
        self.name = name
        self.age = age
        self.doctor_id = doctor_id

    def __str__(self):
        return f"Patient(id={self.id}, Name= {self.name}, Age= {self.age}, Doctor ID= {self.doctor_id})"