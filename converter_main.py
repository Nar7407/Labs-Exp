import convert_utils

MENU = """\n===== UNIT CONVERTER =====
1. Kilometers to miles
2. Celsius to Fahrenheit
3. Kilograms to pounds
4. Exit
Enter your choice: """

def main():
    while True:
        try:
            choice = int(input(MENU))
        except ValueError:
            print("Invalid choice: please enter a number between 1 and 4.")
            continue

        try:
            if choice == 1:
                km = float(input("Enter kilometers: "))
                print(f"{km} km = {convert_utils.km_to_miles(km):.4f} miles")
            elif choice == 2:
                c = float(input("Enter Celsius: "))
                print(f"{c} C = {convert_utils.celsius_to_fahrenheit(c):.4f} F")
            elif choice == 3:
                kg = float(input("Enter kilograms: "))
                print(f"{kg} kg = {convert_utils.kg_to_pounds(kg):.4f} pounds")
            elif choice == 4:
                print("Goodbye!")
                break
            else:
                raise ValueError("choice must be between 1 and 4")
        except ValueError as e:

            print(f"Invalid menu choice or input: {e}")

if __name__ == "__main__":
    main()
