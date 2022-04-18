print("New Car Recommendation")


# Here we're asking the user what they would prefer in a car.
print("What are you looking in a car?")
print("1. Gas Milage?")
print("2. SUV?")
print("3. Sedans?")
print("4. Trucks?")
print("5. Budget?")

while True:
        #input options we're giving to the user
    choice = input("Enter choice (1/2/3/4/5): ")


 # Line belows asks which specific variant they would want

    if choice in ('1', '2', '3', '4', '5'):

# If statements for the first option
        if choice == '1':
            print('1. <$20,000', '2. <$25,000', '3. <$30,000', '4. <$40,000')
            price = input("What is your Budget?  Please enter a number: ")
            if price in ('1', '2', '3', '4'):

    # Subset to the first If statement
                if price == '1':
                    print("Kia Rio start at $16,250 with an MPG of 36 in the City")

                elif price == '2':
                    print("Toyota Corrola Hybrid starts at $23,750 with an MPG of 53 in the City!")

                elif price == '3':
                    print("Toyota Prius starts at $24,625 with and MPG of 58 in the City!")

                elif price == '4':
                    print("Toyota Avalon Hybrid starts at $37,500 with an MPG of 43 in the City")


        elif choice == '2':
            print('1. <$25,000', '2. <$30,000', '3. <$35,000', '4. <$45,000', '5. >$50,000')
            price = input("What is your Budget?  Please enter a number: ")
            if price in ('1', '2', '3', '4', '5'):

                if price == '1':
                    print("2022 Mazda CX-30 starting price is $22,000")

                elif price == '2':
                    print("2022 Hyundai Santa Fe starting at $27,000")

                elif price == '3':
                    print("2022 Kia Sorento starting at $29,590")

                elif price == '4':
                    print("2022 Toyota Rav4 Prime starting at $39,800")

                elif price == '5':
                    print("2022 Mercedes-Benz GLS-Class starting at $77,000")




            elif choice == '3':
                print("1. <$20,000', '2. <$25,000', '3. <$30,000', '4. <$40,000', '5. >$45,000")
                price = input("What is your Budget?  Please enter a number: ")
                if price in ('1', '2', '3', '4', '5'):

                    if price == '1':
                        print("2022 Hyundai Accent begins at $16,645")

                    elif price == '2':
                        print("2022 Honda Civic starts at $22,350!")

                    elif price == '3':
                        print("2022 Kia K5 EX starts at $26,750")

                    elif price == '4':
                        print("2022 Audi A3 starts at $34,450")

                    elif price == '5':
                        print("2022 Audi S6 starts at $74,800")


            elif choice == '4':
                    print('1. <$25,000', '2. <$30,000', '3. <$35,000', '4. <$40,000', '5. >$50,000')
                    price = input("What is your Budget?  Please enter a number: ")
                    if price in ('1', '2', '3', '4', '5'):

                        if price == '1':
                            print("2022 Ford Maverick starts at $21,490!")

                        elif price == '2':
                            print("2022 Toyota Tacoma starts at $26,000")

                        elif price == '3':
                            print("2022 Ford F-150 starts at $31,335")

                        elif price == '4':
                            print("2022 Jeep Gladiator starts at $37,50")

                        elif price == '5':
                            print("2022 Rivivian R1T starts at $67,000")


            elif choice == '5':
                        print("1. <$15,000', '2. <$20,000', '3. <$22,000', '4. <$25,000', '5. <$30,000")
                        price = input("What is your Budget?  Please enter a number: ")
                        if price in ('1', '2', '3', '4', '5'):

                            if price == '1':
                                print("Chevy Spark starts at $14,905")

                            elif price == '2':
                                print("2022 Kia Rio starts at $17,000")

                            elif price == '3':
                                print("2022 Nissan Sentra starts at $20,635")

                            elif price == '4':
                                print("2022 Hyuandi Sonata starts at $24,000")

                            elif price == '5':
                                print("2022 Toyota Prius starts at $24,975")



