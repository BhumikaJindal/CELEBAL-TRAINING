salary = float(input())
late_days = int(input())
absent_days = int(input())

if late_days > 5:
    salary = salary - salary * 0.05

if late_days > 10:
    salary = salary - salary * 0.10

if absent_days > 2:
    salary = salary - salary * 0.05

print(int(salary) if salary.is_integer() else salary)