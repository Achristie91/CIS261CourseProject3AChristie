def GetEmpName():
    empname = input("Enter employee name:  ")
    return empname

def GetDatesWorked():
    fromdate = input("Enter Start Date (mm/dd/yyyyy):  ")
    todate = input("Enter End Date (mm/dd/yyyy):  ")
    return fromdate, todate

def GetHoursWorked():
    hours = float(input("Enter amount of hours worked:  "))
    return hours

def GetHourlyRate():
    hourlyrate = float(input("Enter hourly rate:  "))
    return hourlyrate

def GetTaxRAte():
    taxrate = float(input("Enter tax rate:  "))
    return taxrate

def CalcTaxAndNetPay(hours, hourlyrate, taxrate):
    grosspay = hours * hourlyrate
    incometax = grosspay * taxrate
    netpay = grosspay - incometax
    return grosspay, incometax, netpay

def printinfo(EmpDetailList):
    TotEmployees = 0
    TotHours = 0.00
    TotGrossPay = 0.00
    TotTax = 0.00
    TotNetPay = 0.00
    
    for EmpList in EmpDetailList:
        fromdate = EmpList[0]
        todate = EmpList[1]
        empname = EmpList[3]
        hours = EmpList[4]
        hourlyrate = EmpList[4]
        taxrate = EmpList[5]
        
        grosspay, incometax, netpay = CalcTaxAndNetPay(hours,
hourlyrate, taxrate)
        print(fromdate, todate, empname, f"{hours:,.2f}",
f"{hourlyrate:,.2f}", f"{grosspay:,.2f}", f"{taxrate:,.1%}",
              f"{incometax:,.2f}", f"{netpay:,.2f}")
        
        TotEmployees += 1
        TotHours =+ hours
        TotGrossPay =+ grosspay
        TotTax += incometax
        TotNetPay += nnetpay
      
    EmpTotals["TotEmp"] = TotEmployees
    EmpTotals["TotHrs"] = TotHours
    EmpTotals["TotGrossPay"] = TotGrossPay
    EmpTotals["TotTax"] = TotTax
    EmpTotals["TotNetPay"] = TotNetPay
    
