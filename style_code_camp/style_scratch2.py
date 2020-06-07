print('Hell fuckin yeah')

# Interface: inputs/outputs
# inputs: hours, rate
# outputs: pay

total_hours = 45
rate = 10.5

hours = input("hours = ")


# (1) Break down hours into regular_hours and overtime_hours
if total_hours > 40: # Overtime
    # regular_hours = up to first 40
    # overtime_hours = everything over 40
    regular_hours = 40
    overtime_hours = total_hours - 40
else:  # hours < 40
    regular_hours = total_hours
    overtime_hours = 0
# (2) Compute Pay = regular_pay + overtime_pay
regular_pay = regular_hours * rate
overtime_pay = overtime_hours * 1.5 * rate
pay = overtime_pay + regular_pay
# Print pay
print(pay)

if hours > 40:
    pay = 40 * rate + (hours - 40) * 1.5 * rate
else:
    pay = hours * rate

# applying
regular_pay = regular_hours * regular_rate
pay = regular_pay + overtime_pay
pay = 40 * rate + (hours - 40) * 1.5 * rate
pay = 40 * 10.5 + (45 - 40) * 1.5 * 10.5
# 498.75
