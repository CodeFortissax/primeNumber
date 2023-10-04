# Conversion rate
kes_to_usd_rate = 1 / 140  # 1 USD = 140 KES

while True:
    # Ask the user to input the amount and the currency type
    amount = float(input("Enter the amount: "))
    currency_type = input("Enter the currency type (KES or USD): ").strip().upper()

    if currency_type == 'KES':
        # Convert KES to USD
        usd_amount = amount * kes_to_usd_rate
        print(f"{amount} KES is equal to {usd_amount:.2f} USD\n")
    elif currency_type == 'USD':
        # Convert USD to KES
        kes_amount = amount / kes_to_usd_rate
        print(f"{amount} USD is equal to {kes_amount:.2f} KES\n")
    else:
        print("Invalid currency type. Please enter either KES or USD.\n")

        # Ask if the user wants to perform another conversion
    another_conversion = input("Do you want to perform another conversion? (yes/no): ").strip().lower()

    if another_conversion != 'yes':
        print("Thank you for using the currency converter. Goodbye!")
        break
