def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def c_to_f(c):
    return (c * 9/5) +32

def f_to_c(f):
    return (f - 32) * 5/9

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def main():
    print("📏 Unit Converter")
    while True:
        print("\nChoose a conversion:")
        print("1. Kilometers to Miles")
        print("2. Miles to Kilometers")
        print("3. Celsius to Fahrenheit")
        print("4. Fahrenheit to Celsius")
        print("5. Kilograms to Pounds")
        print("6. Pounds to Kilograms")
        print("0. Exit")

        choice = input("Enter your choice (0-6): ")

        try:
            if choice == "1":
                val = float(input("Enter kilometers: "))
                print(f"{val} km = {km_to_miles(val):.2f} miles")
            elif choice == "2":
                val = float(input("Enter miles: "))
                print(f"{val} miles = {miles_to_km(val):.2f} km")
            elif choice == "3":
                val = float(input("Enter Celsius: "))
                print(f"{val}°C = {c_to_f(val):.2f}°F")
            elif choice == "4":
                val = float(input("Enter Fahrenheit: "))
                print(f"{val}°F = {f_to_c(val):.2f}°C")
            elif choice == "5":
                val = float(input("Enter kilograms: "))
                print(f"{val} kg = {kg_to_lb(val):.2f} lb")
            elif choice == "6":
                val = float(input("Enter pounds: "))
                print(f"{val} lb = {lb_to_kg(val):.2f} kg")
            elif choice == "0":
                print("👋 Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")
        except ValueError:
            print("⚠️ Invalid input. Please enter a number.")

if __name__ == "__main__":
    main()