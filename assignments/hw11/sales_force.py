"""
Name: <Olivia Bianco>
<HW11>.py

Problem: <Sales force class.>

Certification of Authenticity:
<I certify that this assignment is entirely my own work.>
"""
from sales_person import SalesPerson


class SalesForce:
    """
    Class to collect the data of different sales people and
    manipulate the data.
    """
    def __init__(self):
        self.sales_people = []

    def add_data(self, file):
        my_file = open(file, "r")
        for line in my_file.readlines():
            split_file = line.split(",")
            i_d = split_file[0]
            i_d = int(i_d)
            name = split_file[1]
            name = name.strip()
            sales = split_file[2]
            sales = sales.strip()
            sales = sales.split(" ")
            employee = SalesPerson(i_d, name)
            for i in range(len(sales)):
                employee.enter_sale(float(sales[i]))
            self.sales_people += [employee]

    def quota_report(self, quota):
        report = []
        for person in self.sales_people:
            people = []
            employee_id = person.get_id()
            employee_name = person.get_name()
            employee_total = person.total_sales()
            employee_quota = person.met_quota(quota)
            people.append(employee_id)
            people.append(employee_name)
            people.append(employee_total)
            people.append(employee_quota)
            report.append(people)
        return report

    def top_seller(self):
        top_list = []
        top_sales = []
        for i in self.sales_people:
            sales = i.get_sales()
            sales.sort()
            highest = sales[-1]
            top_sales.append(highest)
            top_sales.sort()
        if top_sales[-1] != top_sales[-2]:
            for i in self.sales_people:
                if top_sales[-1] in i.get_sales():
                    top_list.append(i)
                    return top_list
        elif top_sales[-1] == top_sales[-2]:
            for i in self.sales_people:
                if top_sales[-1] in i.get_sales():
                    top_list.append(i)
                if top_sales[-2] in i.get_sales():
                    top_list.append(i)
                    return top_list

    def individual_sales(self, employee_id):
        for person in self.sales_people:
            if employee_id == person.get_id():
                return person

    def get_sale_frequencies(self):
        list_sales = []
        for person in self.sales_people:
            sales = person.get_sales()
            list_sales.append(sales)
        frequency = {}
        for sub in list_sales:
            for item in sub:
                if item in frequency:
                    frequency[item] += 1
                else:
                    frequency[item] = 1
        return frequency
