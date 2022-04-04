def divide(x, y):
    return x / y

print(" Cryptocurrency Converter ")
print("1. USD to BTC ")
print("2. USD to ETH ")
print("3. USD to LTC ")
print("4. USD to DOGE ")

while True:

    choice = input("Enter choice(1/2/3/4): ")

    # check if choice is one of the four options
    if choice in ('1', '2', '3', '4'):
        usd = float(input("How much USD do you want to convert: "))

        if choice == '1':
            print(usd, "/", 46650, "=", divide(usd, 46650))
            print("You would have", divide(usd, 46650), "in Bitcoin")

        elif choice == '2':
            print(usd, "/", 3570.43, "=", divide(usd, 3570.43))
            print("You would have", divide(usd, 3570.43), "in Ethereum")

        elif choice == '3':
            print(usd, "/", 129.31, "=", divide(usd, 129.31))
            print("You would have", divide(usd, 129.31), "in LiteCoin")

        elif choice == '4':
            print(usd, "/", 0.15, "=", divide(usd, 0.15))
            print("You would have", divide(usd, 0.15), "in DogeCoin")