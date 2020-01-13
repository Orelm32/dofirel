from time import sleep

room1 = open("C:/Users/Orel Moshe/Desktop/Python Projects/room1.txt", "r")
room2 = open("C:/Users/Orel Moshe/Desktop/python Projects/room2.txt", "r")
room3 = open("C:/Users/Orel Moshe/Desktop/Python Projects/room3.txt", "r")
room4 = open("C:/Users/Orel Moshe/Desktop/Python Projects/room4.txt", "r")
room1res = open("C:/Users/Orel Moshe/Desktop/Python Projects/room1res.txt", "r")
room2res = open("C:/Users/Orel Moshe/Desktop/Python Projects/room2res.txt", "r")
room3res = open("C:/Users/Orel Moshe/Desktop/Python Projects/room3res.txt", "r")
room4res = open("C:/Users/Orel Moshe/Desktop/Python Projects/room4res.txt", "r")
def dates():
    sleep(1)
    print("\nfor room 1 with 2 adults:\n" + str(room1.read()))
    sleep(1)
    print("\nfor room 2 with 2 adults:\n" + str(room2.read()))
    sleep(1)
    print("\nfor room 3 with 3 adults:\n" + str(room3.read()))
    sleep(1)
    print("\nfor room 4 with 3 adults:\n" + str(room4.read()))
    room1.close()
    room2.close()
    room3.close()
    room4.close()


def invitation():
    boolean = 0
    while boolean == 0:
        date = input("enter your date: ")
        days = input("How many days do you want? ")
        cost2 = (int(days) * 300)
        cost3 = (int(days) * 400)
        while True:
            try:
                adults = int(input("How many adults are you? "))
                break
            except ValueError:
                print("That was not a valid number!")
                print("Answer with numbers only!")
        if adults == 2:
            room1_list = room1.read().splitlines()
            room2_list = room2.read().splitlines()
            boolean = 1
            if date in room1_list and date in room2_list:
                print("Both room 1 and room 2 are available.")
                print("you can invite " + str(days) + " days from " + str(date) + "for a room of 2 adults.")
                print("This will cost you: " + str(cost2))
            elif date in room1_list:
                print("you can invite " + str(days) + " days from " + str(date) + " for " + str(adults) + " adults for room 1")
                print("This will cost you: " + str(cost2))
            elif date in room2_list:
                print("you can invite " + str(days) + " days from " + str(date) + " for " + str(adults) + " adults for room 2")
                print("This will cost you: " + str(cost2))
            else:
                print("This date is taken for both room 1 and room 2")
            room1.close()
            room2.close()
        elif adults == 3:
            room3_list = room3.read().splitlines()
            room4_list = room4.read().splitlines()
            boolean = 1
            if date in room3_list and date in room4_list:
                print("Both room 3 and room 4 are available.")
                print("you can invite " + str(days) + " days from " + str(date) + "for a room of 3 adults.")
                print("This will cost you: " + str(cost3))
            elif date in room3_list:
                print("you can invite " + str(days) + " days from " + str(date) + " for " + str(adults) + " adults for room 3")
                print("This will cost you: " + str(cost3))
            elif date in room4_list:
                print("you can invite " + str(days) + " days from " + str(date) + " for " + str(adults) + " adults for room 4")
                print("This will cost you: " + str(cost3))
            else:
                print("This date is taken for both room 3 and room 4")
                print("Please choose another date.")
            room3.close()
            room4.close()
        else:
            print("We offer only rooms for 2 or 3 adults.")
            sleep(1)
            print("If you are more adults then we suggest you divide the order and take more rooms.")



def calculate():
    while True:
        try:
            days = int(input("How many days do you want?: "))
            adults = int(input("How many adults are you?: "))
            break
        except ValueError:
            print("Answer with numbers only please")
    cost2 = (int(days) * 300)
    cost3 = (int(days) * 400)
    boolean = 0
    while boolean == 0:
        date = input("Enter your desired date: ")
        if adults == 2:
            room1_list = room1.read().splitlines()
            room2_list = room2.read().splitlines()
            if date in room1_list or date in room2_list:
                print("This order of " + str(days) + " days at a room of " + str(adults) + " adults will cost you: " + str(cost2) + " shekels")
                choice = input("Would you like to continue? ")
                if choice == "yes":
                    room1res = open("C:/Users/Orel Moshe/Desktop/Python Projects/room1res.txt", "a")
                    room2res = open("C:/Users/Orel Moshe/Desktop/Python Projects/room2res.txt", "a")
                    print("Then give us your money!")
                    sleep(1)
                    full = input("Enter your full name: ")
                    credit = input("Enter your credit card: ")
                    if date in room1_list and date in room2_list:

                        v = 0
                        while v == 0:
                            number = input("Both room 1 and 2 are available on this date.\n Please choose 1/2:\n")
                            if number == "1":

                                room1res.write("\n" + "Full Name:" + "\n" + full + "\n" + "Date:" + "\n" + date + "\n" + "Number of days: " + "\n" + str(days))

                                print("The order of " + str(adults) + " adults room for " + str(days) + " days from " + str(date) + " is confirmed for the price of " + str(cost2) + " shekels on the name of: " + str(full) )
                                sleep(1)
                                print("Your room number is:\nRoom number " + str(number))
                                v = 1
                                boolean=1
                            elif number == "2":
                                room2res.write("\n" + "Full Name:" + "\n" + full + "\n" + "Date:" + "\n" + date + "\n" + "Number of days: " + "\n" + str(days))
                                print("The order of " + str(adults) + " adults room for " + str(days) + " days from " + str(date) + " is confirmed for the price of " + str(cost2) + " shekels on the name of: " + str(full))
                                sleep(1)
                                print("Your room number is:\nRoom number " + str(number))
                                v = 1
                                boolean=1
                            else:
                                print("Please answer with 1/2 only.")
                    elif date in room1_list:
                        room1res.write("\n" + "Full Name:" + "\n" + full + "\n" + "Date:" + "\n" + date + "\n" + "Number of days: " + "\n" + str(days))
                        print("The order of " + str(adults) + " adults room for " + str(days) + " days from " + str(date) + " is confirmed for the price of " + str(cost2) + " shekels on the name of: " + str(full))
                        sleep(1)
                        print("Your room number is:\nRoom number 1")
                        boolean = 1
                    elif date in room2_list:
                        room2res.write("\n" + "Full Name:" + "\n" + full + "\n" + "Date:" + "\n" + date + "\n" + "Number of days: " + "\n" + str(days))
                        print("The order of " + str(adults) + " adults room for " + str(days) + " days from " + str(date) + " is confirmed for the price of " + str(cost2) + " shekels on the name of: " + str(full))
                        sleep(1)
                        print("Your room number is:\nRoom number 2")
                        boolean=1
                elif choice == "no":
                    again = input("would you like to change your order?: ")
                    if again == "yes":
                        room1.close()
                        room2.close()
                        calculate()
                    elif again == "no":
                        room1.close()
                        room2.close()
                        print("That's ok, have a good day!")
                        boolean = 1
            else:
                print("This date is taken for both rooms for " + str(adults) + " adults.")
                taken = input("would you like to choose a different date?: ")
                if taken == "yes":
                    room2.close()
                    room1.close()
                elif taken == "no":
                    room1.close()
                    room2.close()
                    print("OK, have a good day!")
                    boolean = 1
        elif adults == 3:
            room3_list = room3.read().splitlines()
            room4_list = room4.read().splitlines()

            if date in room3_list or date in room4_list:
                print("This order of " + str(days) + " days at a room of " + str(adults) + " adults will cost you: " + str(cost3) + " shekels")
                choice = input("Would you like to continue? ")
                if choice == "yes":
                    room3res = open("C:/Users/Orel Moshe/Desktop/Python Projects/room3res.txt", "a")
                    room4res = open("C:/Users/Orel Moshe/Desktop/Python Projects/room4res.txt", "a")
                    print("Then give us your money!")
                    sleep(1)
                    full = input("Enter your full name: ")
                    credit = input("Enter your credit card: ")
                    if date in room3_list and date in room4_list:
                        v = 0
                        while v == 0:
                            number = input("Both room 3 and 4 are available on this date.\n Please choose 3/4:\n")
                            if number == "3":
                                room3res.write("\n" + "Full Name:" + "\n" + full + "\n" + "Date:" + "\n" + date + "\n" + "Number of days: " + "\n" + str(days))
                                print("The order of " + str(adults) + " adults room for " + str(days) + " days from " + str(date) + " is confirmed for the price of " + str(cost3) + " shekels on the name of: " + str(full))
                                sleep(1)
                                print("Your room number is:\nRoom number " + str(number))
                                v = 1
                                boolean=1
                            elif number == "4":
                                room4res.write("\n" + "Full Name:" + "\n" + full + "\n" + "Date:" + "\n" + date + "\n" + "Number of days: " + "\n" + str(days))
                                print("The order of " + str(adults) + " adults room for " + str(days) + " days from " + str(date) + " is confirmed for the price of " + str(cost3) + " shekels on the name of: " + str(full))
                                sleep(1)
                                print("Your room number is:\nRoom number " + str(number))
                                v = 1
                                boolean=1
                            else:
                                print("Please answer with 3/4 only.")
                    elif date in room3_list:
                        room3res.write("\n" + "Full Name:" + "\n" + full + "\n" + "Date:" + "\n" + date + "\n" + "Number of days: " + "\n" + str(days))
                        print("The order of " + str(adults) + " adults room for " + str(days) + " days from " + str(date) + " is confirmed for the price of " + str(cost3) + " shekels on the name of: " + str(full))
                        sleep(1)
                        print("Your room number is:\nRoom number 3")
                        boolean = 1
                    elif date in room4_list:
                        room4res.write("\n" + "Full Name:" + "\n" + full + "\n" + "Date:" + "\n" + date + "\n" + "Number of days: " + "\n" + str(days))
                        print("The order of " + str(adults) + " adults room for " + str(days) + " days from " + str(date) + " is confirmed for the price of " + str(cost3) + " shekels on the name of: " + str(full))
                        sleep(1)
                        print("Your room number is:\nRoom number 4")
                        boolean = 1
                elif choice == "no":
                    again = input("would you like to change your order?: ")
                    if again == "yes":
                        room1.close()
                        room2.close()
                        calculate()
                        boolean = 1
                    elif again == "no":
                        room1.close()
                        room2.close()
                        print("That's ok, have a good day!")
                        boolean = 1
            else:
                print("This date is taken for both rooms for " + str(adults) + " adults.")
                taken = input("would you like to choose a different date?: ")
                if taken == "yes":
                    room2.close()
                    room1.close()
                    boolean = 0
                elif taken == "no":
                    room1.close()
                    room2.close()
                    print("OK, have a good day!")
                    boolean = 1


def cancel():
    print("This will fine you for 10% of the price!")
    choice = input("Are you sure you want to cancel your order? ")
    if choice == "yes":
        name = input("Enter your full name: ")
        room1_list = room1res.read().splitlines()
        room2_list = room2res.read().splitlines()
        room3_list = room3res.read().splitlines()
        room4_list = room4res.read().splitlines()
        # date = input("Enter your order`s date: ")
        print(room1_list)
        adults = str(input("How many adults were you?: "))
        if adults == "2":
            if name in room1_list:
                room1.close()
                with open("C:/Users/Orel Moshe/Desktop/Python Projects/room1res.txt", "r+") as f:
                    s = f.readlines()
                    f.seek(0)
                    for i in s:
                        clean_line = i.replace(name, "")

                    f.truncate()
                    print("Done")
    #     cost = input("How much did your order cost?: ")
    #     fine = int(cost) * 0.1
    #     print("you need to pay " + str(fine) + " shekels to cancel the order on the name of " + str(name) + " at the date " + str(date) + " please.")
    # elif choice == "no":
    #     print("We are glad and waiting to see you")

def anyelse():
    need = input("do you need anything else?")
    if need == "yes":
        boolean = 0
    elif need == "no":
        print("enjoy your trip!")
        boolean = 1