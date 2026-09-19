
number = int(input("Enter a multiple of 5 between 1 and 100: "))

if 1 <= number <= 100 and number % 5 == 0:
    print(f"The number {number} is valid.")
else:
    print(f"The number {number} is invalid. It must be between 1 and 100 and a multiple of 5.")