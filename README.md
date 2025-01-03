Currency Converter

A simple currency converter built using Python and Streamlit, which allows users to convert amounts between various world currencies. It utilizes the CurrencyConverter library for real-time exchange rates and the babel library for currency symbols.

Features

Converts amounts between over 30 currencies.
User-friendly dropdown menu to select currencies.
Real-time exchange rate conversion using the CurrencyConverter library.
Displays the currency symbol for better clarity.
Built with Streamlit for an interactive and responsive UI.
Technologies Used

Python: Core language for building the logic.

Streamlit: For creating the web interface.

CurrencyConverter: To fetch and calculate live exchange rates.

Babel: To retrieve currency symbols and format numbers.

Installation

Clone the Repository
git clone https://github.com/yourusername/currency-converter.git
cd currency-converter
Install Dependencies Use pip to install the required libraries:
pip install streamlit babel currencyconverter
Usage

Run the Application 
Start the Streamlit server:
streamlit run app.py

Interact with the Interface

Select the currencies to convert from and to.

Input the amount to be converted.

View the converted amount in real-time.


Code Highlights

Currency Data
The app supports a wide range of currencies:

countriesList = [
    'EUR - Euro Member Countries', 'IDR - Indonesia Rupiah', 'BGN - Bulgaria Lev', 
    'ILS - Israel Shekel', 'GBP - United Kingdom Pound', 'USD - United States Dollar', 
    'INR - India Rupee', 'JPY - Japan Yen', ...
]
Each currency includes:

Abbreviation (e.g., USD for United States Dollar)
Name (e.g., United States Dollar)
Symbol (e.g., $ for USD)
Conversion Functionality
The converterFunc() fetches exchange rates and performs the conversion:

def convertCurrency(firstCountry, secondCountry, amount):
    # Match abbreviations for the selected countries
    firstCountrySymbol = ...
    secondCountrySymbol = ...
    
    # Use CurrencyConverter to calculate the amount
    converted_amount = converter.convert(amount, firstCountrySymbol, secondCountrySymbol)
    return converted_amount
Example Usage

Convert 100 USD to EUR:
Input: 100
From: United States Dollar
To: Euro Member Countries
Output: Converted amount: €91.23 (example value).
Extending the Project

Add support for historical exchange rates.
Implement graphs to visualize currency trends.
Allow users to save and export conversion histories.
Contributing

Contributions are welcome! Feel free to submit issues or pull requests for new features and improvements.

License

This project is licensed under the MIT License.
