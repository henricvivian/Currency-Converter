# Currency Converter
This is a Python function that uses an API to perform real-time Currency conversions. The 'currency_converter()' function takes three arguments: 'amount', 'from_currency', and 'to_currency'. The 'amount' argument is the amount of the money that the user wants to convert. The ' from_currency' argument is the currency code for the currency that the user wants to convert from, and the 'to_currency' arguments is the currency code for the currency that the user wants to convert to.

The function uses the 'requests' library to send a GET request to an API endpoint that provides real-time currency conversion rates. If the API call is successful, the function extracts the conversion rate from the API response and returns the converter amount. If the API call is unseccessful, the function returns an error message.

# Usage
To use the 'currency_converter()' function, you should have Python installed on your system. You can call the function from your Python script or from the Python shell.

1. Install requests module:
```bash
    pip install requests
```
2. Run the program:
```bash
    python currency_converter.py
```
3. Enter the amount you want to convert, the currency you want to convert from, and the currency you want to convert to.
4. The program will output the converted amount.
```bash
    Enter the amount: 100
    Enter the currency you want to convert from: USD
    Enter the currency you want to convert to: EUR
    Converted amount: 84.17
```
# Limitations:
- The program may not work if the API endpoint is down or unavailable.
- The program may not work for currencies that are nit supported by the API endpoint.

# Contributing:
Contributions are welcome! If you find a bug or have a suggestion for improvement, please open an issue or submit a pull requests.
