def celsius_to_fahrenheit(c):
    return (c * 9/5)+32
def fahrenheit_to_celsius(f):
    return (f - 32) * 5/9
def celsius_to_kelvin(c):
    return c+273.15
def kelvin_to_celsius(k):
    return k-273.15

while True:
    print("\n Temperature Converter!..")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")

    choice = input("Enter your choice (1/2/3/4): ")

    if choice not in ["1","2","3","4"]:
        print("Invalid choice. Please try again.")
        continue

    temp=float(input("Enter temperature: "))

    if choice == "1":
        print("Result: ",celsius_to_fahrenheit(temp), "F")
    elif choice == "2":
        print("Result: ",fahrenheit_to_celsius(temp), "C")
    elif choice == "3":
        print("Result: ",celsius_to_kelvin(temp), "K")
    elif choice == "4":
        print("Result: ",kelvin_to_celsius(temp), "C")

    again = input("Do you want to continue? (y/n): ")
    if again != "y":
        print("Thank you for using this temperature converter.")
        break
