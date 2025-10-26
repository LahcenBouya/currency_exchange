import os
import time

ascci_money = """
||====================================================================||
||//$\\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\//$\\||
||(100)==================|       bouyalahcen    |================(100)||
||\\$//        ~         '------========--------'                \\$//||
||<< /        /$\              // ____ \\                         \ >>||
||>>|  12    //L\\            // ///..) \\         L38036133B   12 |<<||
||<<|        \\ //           || <||  >\  ||                        |>>||
||>>|         \$/            ||  $$ --/  ||        One Hundred     |<<||
||<<|      L38036133B        *\\  |\_/  //* series                 |>>||
||>>|  12                     *\\/___\_//*   1989                  |<<||
||<<\      Treasurer     ______/Franklin\________     Secretary 12 />>||
||//$\                 ~|UNITED STATES OF AMERICA|~               /$\\||
||(100)===================  ONE HUNDRED DOLLARS =================(100)||
||\\$//\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\/\\$//||
||====================================================================||
"""

exchange_rates = {
    "": ascci_money,
    "USD": 1.0,
    "EUR": 0.85,
    "EGP": 30.9,
    "RMB": 6.5,
    "MAD": 9.23,
    "JPY": 152.81,
    "PKR": 281.17,
    "KWD": 0.31,
}

def clear_screen():
    os.system("cls" if os.name == "nt" else "clear")

def display_rates():
    print("welcome to 'currency converter':\n")
    for currency in exchange_rates:
        print(f"{currency}: {exchange_rates[currency]}")

def currency_converter():
    clear_screen()
    display_rates()

    from_currency = input("\nchoose a currency to convert from: ").upper()
    while True:
        amount = float(input("Enter your amount: "))

        confirmation = input(f"\nyou entered {amount} {from_currency}. confirm?(y/n): ").upper()

        if confirmation == "Y":
            break
    
    clear_screen()
    display_rates()

    to_currency = input("\nchoose a currency to convert to: ").upper()

    print("Analyzing your request..... please wait.")
    time.sleep(2)
    print(f"checking for {to_currency.upper()}'s best rates available... please wait")
    time.sleep(3)
    print(f"getting a discount price for {from_currency.upper()}...... please wait")
    time.sleep(2)


    if from_currency not in exchange_rates or to_currency not in exchange_rates:
        print("invalid currency. conversion canceled.")
        time.sleep(2)
        currency_converter()

    new_rate = exchange_rates[to_currency] / exchange_rates[from_currency]

    converted_amount = amount * new_rate

    clear_screen()
    print(f"preparing the deal from {from_currency} to {to_currency}..... please wait")
    time.sleep(2)
    print(f"Exchange Rate: 1 {from_currency} = {converted_amount} {to_currency}\n")
    time.sleep(2)
    print(f"{amount} {from_currency} is equal to {round(converted_amount, 2)} {to_currency}")
    time.sleep(1)

    accept_transaction = input("\ndo you accept this transaction. (y/n): ").upper()

    if accept_transaction == 'Y':
        print("transaction successful!")
    else:
        print("transaction canceled.")

    another_conversion = input("\ndo you want to perform another conversion? (y/n): ").upper()

    if another_conversion == "Y":
        currency_converter()
    else:
        print("thanks for using the currency converter!")


currency_converter()
