"""
Day 12 of 90-Day Coding Series
Beginner-Friendly Currency Converter

This program converts amounts from one currency to another
using fixed example rates stored in a dictionary.

After each conversion you can choose:
    1 = Quit the program
    2 = Convert another amount

This is free to use (no warranty).
"""

# ---------------------------
# Step 1: Create some sample exchange rates
# (In a real app you’d fetch live rates from an API,
#  but for beginners we keep fixed example values.)
# ---------------------------

# Rates are relative to 1 unit of the "from currency"
# For example: 1 USD = 280 PKR, 0.92 EUR, 83.5 INR
exchange_rates = {
    "USD": {"PKR": 280, "EUR": 0.92, "INR": 83.5},
    "PKR": {"USD": 0.0036, "EUR": 0.0033, "INR": 0.30},
    "EUR": {"USD": 1.09, "PKR": 300, "INR": 90.7},
    "INR": {"USD": 0.012, "PKR": 3.3, "EUR": 0.011}
}

# ---------------------------
# Step 2: Helper function to show available currencies
# ---------------------------

def show_currencies():
    """Print all available currency codes."""
    print("Available currencies:")
    for code in exchange_rates:
        print("-", code)

# ---------------------------
# Step 3: Main conversion function
# ---------------------------

def convert_currency(amount, from_currency, to_currency):
    """
    Convert 'amount' from 'from_currency' to 'to_currency'
    using the exchange_rates dictionary.
    """
    try:
        rate = exchange_rates[from_currency][to_currency]
        return amount * rate
    except KeyError:
        # If user enters unsupported currency codes
        print("Conversion not available between those currencies.")
        return None

# ---------------------------
# Step 4: Main program loop
# ---------------------------

def main():
    print("=== Day 12: Currency Converter ===")
    show_currencies()

    while True:
        # Ask the user for input
        from_curr = input("\nEnter FROM currency code (e.g. USD): ").strip().upper()
        to_curr = input("Enter TO currency code (e.g. PKR): ").strip().upper()

        try:
            amount = float(input("Enter the amount to convert: "))
        except ValueError:
            print("Please enter a valid number for amount.")
            continue

        # Perform conversion
        result = convert_currency(amount, from_curr, to_curr)
        if result is not None:
            print(f"\n{amount} {from_curr} = {result:.2f} {to_curr}")

        # Ask whether to continue or quit
        print("\nWhat would you like to do next?")
        print("1. Quit")
        print("2. Convert another amount")
        choice = input("Enter 1 or 2: ").strip()

        if choice == "1":
            print("Goodbye! Thanks for using the Currency Converter.")
            break
        elif choice == "2":
            continue
        else:
            print("Invalid choice, exiting.")
            break

# Only run main() if this file is executed directly
if __name__ == "__main__":
    main()
