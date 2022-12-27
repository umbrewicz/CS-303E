# File: Payroll.py
# Student: Nick Umbrewicz
# UT EID: nju96
# Course Name: CS303E
#
# Date: 02/11/22
# Description of Program: This program returns a payroll statement given user input.

name = str(input("Enter employee's name: "))
hours = float(input("Enter number of hours worked in a week: "))
rate = float(input("Enter hourly pay rate: "))
fed_tax = float(input("Enter federal tax withholding rate: "))
state_tax = float(input("Enter state tax withholding rate: "))

gross_pay = round(hours * rate, 2)
fed_ded = gross_pay * fed_tax
state_ded = gross_pay * state_tax
total_ded = fed_ded + state_ded
net_pay = gross_pay - total_ded

print("Employee Name: " + name)
print("Hours Worked: " + str(hours))
print("Pay Rate: $" + str("{:.2f}".format(rate)))
print("Gross Pay: $" + str("{:.2f}".format(gross_pay)))
print("Deductions:")
print(" 2 Federal Withholding (" + str(fed_tax * 100)+"%): $"
      + str("{:.2f}".format(fed_ded)))
print("  State Withholding (" + str(state_tax * 100) + "%): $"
      +  str("{:.2f}".format(state_ded)))
print("  Total Deduction: $" + str("{:.2f}".format(total_ded)))
print("Net Pay: $" + str("{:.2f}".format(net_pay)))