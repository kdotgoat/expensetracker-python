# currency_api.py - Fetch real-time currency exchange rates

import requests

API_URL = "https://api.exchangerate-api.com/v4/latest/USD"  # Base API URL; USD can be changed as needed

def get_exchange_rates(base_currency="USD"):
    """
    Fetch the latest exchange rates from the API.
    :param base_currency: The base currency to convert from (default is USD).
    :return: Dictionary of exchange rates or None if an error occurred.
    """
    try:
        response = requests.get(f"https://api.exchangerate-api.com/v4/latest/{base_currency}")
        data = response.json()
        if response.status_code == 200:
            print(f"Exchange rates for {base_currency} fetched successfully.")
            return data['rates']
        else:
            print("Failed to fetch exchange rates.")
            return None
    except Exception as e:
        print(f"An error occurred while fetching exchange rates: {e}")
        return None

def convert_currency(amount, from_currency, to_currency, rates):
    """
    Convert an amount from one currency to another.
    :param amount: The amount to convert.
    :param from_currency: The currency to convert from.
    :param to_currency: The currency to convert to.
    :param rates: Dictionary of exchange rates.
    :return: Converted amount.
    """
    if from_currency == to_currency:
        return amount
    if from_currency not in rates or to_currency not in rates:
        print(f"Conversion from {from_currency} to {to_currency} is not supported.")
        return None
    
    # Convert to base currency first, then to the target currency
    base_amount = amount / rates[from_currency]
    converted_amount = base_amount * rates[to_currency]
    return round(converted_amount, 2)

def show_conversion_options(transactions):
    """
    Show currency conversion options to the user.
    """
    rates = get_exchange_rates()
    if not rates:
        print("Could not fetch exchange rates. Please try again later.")
        return

    from_currency = input("Enter the currency to convert from (e.g., USD): ").upper()
    to_currency = input("Enter the currency to convert to (e.g., EUR): ").upper()
    print("\nConverted Transactions:")
    for transaction in transactions:
        converted_amount = convert_currency(transaction['amount'], from_currency, to_currency, rates)
        if converted_amount is not None:
            print(f"{transaction['type']} of {transaction['amount']} {from_currency} is {converted_amount} {to_currency}.\n")
