"""
Name: <Olivia Bianco>
<HW11>.py

Problem: <Sales person class.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


class SalesPerson:
    """
    Class to represent the information of different sales people in a file
    """

    def __init__(self, employee_id, name):
        self.employee_id = int(employee_id)
        self.name = name
        self.sales = []

    def get_id(self):
        return self.employee_id

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def enter_sale(self, sales):
        self.sales.append(sales)

    def total_sales(self):
        acc = 0
        for sale in self.sales:
            acc += sale
        return acc

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.total_sales() == quota or self.total_sales() > quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other.total_sales() > self.total_sales():
            return -1
        if self.total_sales() > other.total_sales():
            return 1
        return 0

    def __str__(self):
        return "{0}-{1}: {2}".format(self.employee_id, self.name, self.total_sales())
