#exercise1
l = [1,2,3,4,5,6,7,8,9,10]
output = 0
for i in l:
    output = output + i
    print(output)
    
output :
1
3
6
10
15
21
28
36
45
55

#exercise2
n = [3,5,6,7,8,9,10,11,15,19,20]
i = 0
for i in n:
        if i%5 == 0:
            print(i)
            i = i+1
        else:
            i = i+1
            
 output :
 5
10
15
20

#exercise3
name = input("Enter your name: ")
role = input("Enter your designation: ")
salary = float(input("Enter your salary per month(INR): "))
def currency(salary):
    salary = salary / 75.23
    salary = round(salary, 2)
    return salary
print("Name: ", name)
print("Designation: ", role)
salary = currency(salary)
print("Salary per month(in Dollars): ", salary)
salary = salary * 12
salary = round(salary, 2)
print("Salary per annum(in Dollars): ", salary)
if salary < 10000:
    print("You have no tax")
elif salary <= 20000:
    money = salary - 10000
    another_money = money * 0.1
    another_money = round(another_money, 2)
    print(another_money)
elif salary > 20000:
    tax_free = 10000
    first_tax = 10000 * 0.1
    rest_money = salary - tax_free
    money = rest_money - first_tax
    final = salary - 20000
    remain_tax = final * 0.2
    total_tax = remain_tax + first_tax
    print("10% of tax for the 2nd $10,000 from the income", first_tax)
    print("20% of tax for rest of the income", remain_tax)
    print("total tax: ", total_tax) 
    print("Salary left after all the tax deduction: ", salary - total_tax)
else:
    print("Something went wrong")
    
output:
  Enter your name: ani
Enter your designation: manager
Enter your salary per month(INR): 300000
Name:  ani
Designation:  manager
Salary per month(in Dollars):  3987.77
Salary per annum(in Dollars):  47853.24
10% of tax for the 2nd $10,000 from the income 1000.0
20% of tax for rest of the income 5570.648
total tax:  6570.648
Salary left after all the tax deduction:  41282.592

  
#exercise4

x = []
for i in range(1,501):
    if i % 5 == 0:
        x.append(i)
        print(i)
print("the count: ", len(x))

output:
  5
10
15
20
25
30
35
40
45
50
55
60
65
70
75
80
85
90
95
100
105
110
115
120
125
130
135
140
145
150
155
160
165
170
175
180
185
190
195
200
205
210
215
220
225
230
235
240
245
250
255
260
265
270
275
280
285
290
295
300
305
310
315
320
325
330
335
340
345
350
355
360
365
370
375
380
385
390
395
400
405
410
415
420
425
430
435
440
445
450
455
460
465
470
475
480
485
490
495
the count:  99

#exercise5
consumer_number = input("Enter your consumer number: ")
name = input("Enter your name: ")
unit = int(input("Enter unit consumed: "))
if unit <= 100:
     amount = unit * 1.5
     amount = amount + 25
     print(amount)       
elif unit > 100 and unit <= 200:
     amount = (100 * 1.5) + (unit - 100) * 2.5
     amount = amount + 50
     print(amount)
elif unit > 200 and unit <= 300:
     amount = (100 * 1.5) + (200 - 100) * 2.5 + (unit - 200) * 4
     amount = amount + 75
     print(amount)
elif unit > 300 and unit <= 350:
     amount = (100 * 1.5) + (200 - 100) * 2.5 +(300 - 200) * 4 + (unit - 350) * 5
     amount = amount + 100   
     print(amount)
elif unit > 350:
     amount = 1500
     print(amount)
else:
    print("Something went wrong")
    
output:
  Enter your consumer number: 454789
Enter your name: ani
Enter unit consumed: 248
667.0

#casestudy 

annual_salary = int(input("Enter starting annual salary: "))
portion_saved = float(input("Enter the portion to be saved: "))
total_cost = int(input("Enter the cost of your dream house: "))
monthly_salary = annual_salary / 12
monthly_salary = round(monthly_salary, 2)
portion_down_payment = total_cost * 0.25
monthly_savings = monthly_salary * portion_saved
monthly_savings = round(monthly_savings, 2)
print("monthly_salary: ", monthly_salary)
print("portion_down_payment: ", portion_down_payment)
print("monthly_savings: ", monthly_savings)
current_savings = 0
months = 0
while current_savings <= portion_down_payment:
    current_savings = current_savings + current_savings * (0.04 / 12) + monthly_savings
    months = months + 1
print("Months it'll take to reach the down payment amount is " + str(months) + " months")

output:
Enter starting annual salary: 110000
Enter the portion to be saved: 0.1
Enter the cost of your dream house: 1250000
monthly_salary:  9166.67
portion_down_payment:  312500.0
monthly_savings:  916.67
Months it'll take to reach the down payment amount is 229 months
  
#casestudyB

annual_salary = int(input("Enter starting annual salary: "))
portion_saved = float(input("Enter the portion to be saved: "))
total_cost = int(input("Enter the cost of your dream house: "))
semi_raise = float(input("Enter the semi annual raise: "))
monthly_salary = annual_salary / 12
monthly_savings = annual_salary * portion_saved / 12
portion_down_payment = total_cost * 0.25
print("monthly_salary: ", monthly_salary)
print("monthly_savings: ", monthly_savings)
print("portion_down_payment: ", portion_down_payment)
current_savings = 0
months = 0
while current_savings <= portion_down_payment:
    current_savings += monthly_savings 
    current_savings += current_savings * 0.04 / 12
    months = months + 1
    if months % 6 == 0:
        monthly_savings += monthly_savings * semi_raise 
print("Months it'll take to reach the down payment amount is " + str(months) + " months")

output:
  
  Enter starting annual salary: 110000
Enter the portion to be saved: 0.05
Enter the cost of your dream house: 700000
Enter the semi annual raise: 0.06
monthly_salary:  9166.666666666666
monthly_savings:  458.3333333333333
portion_down_payment:  175000.0
Months it'll take to reach the down payment amount is 147 months



  

  
