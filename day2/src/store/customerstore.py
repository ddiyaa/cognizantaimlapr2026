#generate 100 customers
import faker
import typing
from models.customer import Customer
class CustomerStore:
    def __init__(self ,num_customers: int = 100):
        self.customers = []
        self.faker = faker.Faker()
        self.generate_customers(num_customers)

    def generate_customers(self, num_customers: int):
        for _ in range(num_customers):
            name = self.faker.name()
            email = self.faker.email()
            dob = self.faker.date_of_birth()
            customer = Customer(name, email, dob)
            self.customers.append(customer)

    def get_customers(self) -> typing.List[Customer]:
        return self.customers