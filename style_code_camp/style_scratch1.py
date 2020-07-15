hrs = float(input("Enter Hours: "))
rate = float(input("Enter Rate: "))
if hrs > 40:
    max_hours_normal = 40
    overtime_rate = 1.5
    pay = max_hours_normal * rate + (hrs - max_hours_normal) * rate * overtime_rate
else:
    pay = hrs * rate
print(pay)
