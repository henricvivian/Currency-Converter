import requests


def currency_converter(amount, from_currency, to_currency):
    # API endpoint to get real-time currency conversion rates
    url = "https://api.exchangerate-api.com/v4/latest/" + from_currency

    # Send a GET request to the API endpoint
    response = requests.get(url)

    # Check if the API call was successful
    if response.status_code == 200:
        # Get the conversion rate from the API response
        conversion_rate = response.json()["rates"][to_currency]

        # Return converted amount
        return amount * conversion_rate
    else:
        # Return an error message if the API call was unsuccessful
        return "Error getting conversion rate from API."


# Test the function
amount = float(input("Enter the amount: "))
from_currency = input("Enter the currency you want to convert from: ").upper()
to_currency = input("Enter the currency you want to convert to: ").upper()

converted_amount = currency_converter(amount, from_currency, to_currency)
print("Converted amount: ", converted_amount)