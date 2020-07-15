
def computepay(hours, pay_rate):
    if hours > 40:
        pay = 40 * pay_rate + (hours - 40) * 1.5 * pay_rate
    else:
        pay = hours * pay_rate
    return pay


# Inputs
hrs = float(input("Enter hours:"))  # 45
rate = float(input("Enter rate:"))  # 10.5
# Compute
p = computepay(hrs, rate)
# Print
print("Pay ", p)
