import csv

with open('G:/Users/nevin/vsCode/Python non publishing/emp_phone_list/employees.csv') as file:
    listing = csv.DictReader(file)
    for employee in listing:
        print(employee['Name'] + ": " + employee['Phone Number'])