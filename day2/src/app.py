# creating entry point for application
import faker
from store.customerstore import CustomerStore
from view.customerview import CustomerView


"""
creating entrypoint for the application to display a random name.
"""


def check():
    """
    this function creates an instance of the faker class and prints a fake name.

    """
    customer_store = CustomerStore()
    customer_view = CustomerView(customer_store)
    customer_view.display_customers()
    


if __name__ == "__main__":
    check()
