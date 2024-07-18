import streamlit as st
from babel import numbers
from currency_converter import CurrencyConverter

converter = CurrencyConverter()
countriesList = ['EUR - Euro Member Countries', 'IDR - Indonesia Rupiah', 'BGN - Bulgaria Lev', 'ILS - Israel Shekel', 'GBP - United Kingdom Pound', 'DKK - Denmark Krone', 'CAD - Canada Dollar', 'JPY - Japan Yen', 'HUF - Hungary Forint', 'RON - Romania New Leu', 'MYR - Malaysia Ringgit', 'SEK - Sweden Krona', 'SGD - Singapore Dollar', 'HKD - Hong Kong Dollar', 'AUD - Australia Dollar', 'CHF - Switzerland Franc', 'KRW - Korea (South) Won', 'CNY - China Yuan Renminbi', 'TRY - Turkey Lira', 'HRK - Croatia Kuna', 'NZD - New Zealand Dollar', 'THB - Thailand Baht', 'USD - United States Dollar', 'NOK - Norway Krone', 'RUB - Russia Ruble', 'INR - India Rupee', 'MXN - Mexico Peso', 'CZK - Czech Republic Koruna', 'BRL - Brazil Real', 'PLN - Poland Zloty', 'PHP - Philippines Peso', 'ZAR - South Africa Rand']
countriesDictList = []
for country in countriesList:
    newDict = {}
    newDict['abbreviation'] = country[0:3]
    newDict['name'] = country[6:len(country)]
    newDict['symbol'] = numbers.get_currency_symbol(country[0:3])
    countriesDictList.append(newDict)

currencyList = []
currencyList.append("Please select")
for x in countriesDictList:
    currencyList.append(x.get('name'))

def converterFunc():
    #build converter
    def convertCurrency(firstCountry, secondCountry, amount):
        firstCountrySymbol = None
        secondCountrySymbol = None
        for countryDict in countriesDictList:
            if firstCountrySymbol is not None and secondCountrySymbol is not None:
                break
            elif countryDict.get('name') == firstCountry:
                firstCountrySymbol = countryDict.get('abbreviation')
            elif countryDict.get('name') == secondCountry:
                secondCountrySymbol = countryDict.get('abbreviation')
                currencySymbol = countryDict.get('symbol')
        print(firstCountrySymbol)
        print(secondCountrySymbol)
        
        newAmount = converter.convert(amount, firstCountrySymbol, secondCountrySymbol)
        return ("The converted amount is " + currencySymbol + str(round(newAmount,2)))

    def runConverter(firstCountry, secondCountry, amount):
        if(firstCountry == "Please Select" or secondCountry == "Please Select"):
            return
        else:
            st.markdown(f"<h3 style = 'text-align: center;'>{convertCurrency(firstCountry, secondCountry, amount)}</h3>", unsafe_allow_html = True)

    def main():
        st.markdown("<h1 style='text-align: center;'>Currency Converter</h1>", unsafe_allow_html=True)
        with st.container():
            with st.form("myform"):
                amount = st.number_input("Enter the amount to be converted: ")
                firstCurrency = st.selectbox("From currency: ",currencyList)
                secondCurrency = st.multiselect("To currency(ies): ", currencyList, key = "countryName")
                submitButton = st.form_submit_button(
                    "Convert Currency",
                )
        st.container(height = 50, border = False)
        with st.container():
            if submitButton:
                returnedValues = []
                for newCurrency in secondCurrency:
                    returnedValues.append(runConverter(firstCurrency, newCurrency, amount))
                
                for convertedValue in returnedValues:
                    st.markdown(f"<h3 style ='text-align: center;'{convertedValue}</h3>", unsafe_allow_html = True)
        


    if __name__ == "__main__":
        main()