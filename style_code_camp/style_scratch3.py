
score = float(input("Enter Score:"))
if score < 0 or score > 1:
    print('Error. Enter a number between 0 and 1.')
else:
    if score >= 0.9:
        grade = 'A'
    elif score >= 0.8:
        grade = 'B'
    elif score >= 0.7:
        grade = 'C'
    elif score >= 0.6:
        grade = 'D'
    else:
        grade = 'F'
    print('Grade :', grade)
