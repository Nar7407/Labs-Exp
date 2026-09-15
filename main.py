import sci_calc

MENU = """\n===== SCIENTIFIC CALCULATOR =====
1. Power
2. Factorial
3. GCD
4. Prime check
5. Exit
Enter your choice: """

def get_int(prompt):
    return int(input(prompt))

def main():
    while True:
        try:
            choice = int(input(MENU))
        except ValueError:
            print("Invalid choice: please enter a number between 1 and 5.")
            continue

        try:
            if choice == 1:
                base = get_int("Enter base: ")
                exp = get_int("Enter exponent: ")
                print(f"{base}^{exp} = {sci_calc.power(base, exp)}")
            elif choice == 2:
                n = get_int("Enter a non-negative integer: ")
                print(f"{n}! = {sci_calc.factorial(n)}")
            elif choice == 3:
                a = get_int("Enter first number: ")
                b = get_int("Enter second number: ")
                print(f"GCD({a}, {b}) = {sci_calc.gcd(a, b)}")
            elif choice == 4:
                n = get_int("Enter a number: ")
                result = "is prime" if sci_calc.is_prime(n) else "is not prime"
                print(f"{n} {result}")
            elif choice == 5:
                print("Goodbye!")
                break
            else:
                raise ValueError("choice must be between 1 and 5")
        except ValueError as e:

            print(f"Invalid menu choice or input: {e}")

if __name__ == "__main__":
    main()
