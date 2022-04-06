"""
Name: <Olivia Bianco>
<HW11>.py

Problem: <Sales person class.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""


class SalesPerson:

    def __init__(self, employee_id, name):
        self.employee_id = employee_id
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
        sum(self.sales)

    def get_sales(self):
        return self.sales

    def met_quota(self, quota):
        if self.sales >= quota:
            return True
        else:
            return False

    def compare_to(self, other):
        if other.sales > self.sales:
            return -1
        elif self.sales > other.sales:
            return 1
        elif self.sales == other.sales:
            return 0

    def __str__(self):
        return self.employee_id, self.name, self.sales
