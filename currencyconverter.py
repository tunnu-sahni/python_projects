# simple currenct converter without forex python

def currency_converter():
    rates = {
        'USD' : {'INR' : 83.0, 'EUR' : 0.95},
        'INR' : {'USD' : 0.012, 'EUR' : 0.011},
        'EUR' : {'USD' : 1.05, 'INR' : 87.5}
    }
    amount = float(input("enter amount: "))

    from_currency = input("from currency(USD,INR,EUR): ").upper()
    to_currency = input("to currency(USD,INR,EUR): ").upper()
    try:
        if from_currency == to_currency:
            result = amount
        else:
            result = amount 
            rates[from_currency][to_currency]

            print(f"{amount} {from_currency} = {round(result, 2)} {to_currency}")

    except KeyError:
        print("Error: currency not supported or wrong code entered.")

if __name__ == "__main__":
    currency_converter()