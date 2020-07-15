
largest = None
smallest = None
while True:
    num = input("Enter a number: ")

    if num == 'done':
        break

    # Check if int
    try:
        num_int = int(num)
    except:
        print('Invalid input')

    # Min/Max logic
    if largest is None:
        largest = num_int
        smallest = num_int
    if num_int > largest:
        largest = num_int
    if num_int < smallest:
        smallest = num_int

# Results
print("Maximum is", largest)
print("Minimum is", smallest)
