def calculation(enter): #uses the inputs from the user-input
    enter.setProductPrice(float(enter.cost) * 1.35)
    enter.setInventoryCost(float(enter.cost) * float(enter.quantity))
    return enter

def calcEmployeeData(employee):
    grossWage = float(employee.wage) * float(employee.hours) # calculates the wage of an employee
    if grossWage <= 500 and grossWage >= 0:
        employee.setTaxes(grossWage * 0.25)# calculates the taxes for a pay less than $500
    elif grossWage <= 900 and grossWage >= 501:
        employee.setTaxes(grossWage * 0.30)# calculates the taxes
    elif grossWage <= 1200 and grossWage >= 901:
        employee.setTaxes(grossWage * 0.35)
    else:
        employee.setTaxes(grossWage * 0.40)
    employee.setNetPay(grossWage - employee.taxes)

    return employee;
