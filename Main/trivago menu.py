from Main import hotel

print("Welcome to Net4U Hotel!")
print("""Choose your option:
1.Get available dates at the hotel.
2.Choose your dates and how many adults.
3.Calculate the costs and complete your order.
4.Cancel an order (with a fine of 10%).
5.Add a room or adults to existing order.
6.Search existing order.""")
boolean = 0
while boolean == 0:
    while True:
        try:
            choice = int(input("What do you choose?: "))
            break
        except ValueError:
            print("That was not a number!")
            print("Only valid numbers please!")
    if choice == 1:
        hotel.dates()
        hotel.anyelse()
        boolean = 1
    elif choice == 2:
        hotel.invitation()
        hotel.anyelse()
        boolean = 1
    elif choice == 3:
        hotel.calculate()
        hotel.anyelse()
        boolean = 1
    elif choice == 4:
        hotel.cancel()
        hotel.anyelse()
        boolean = 1
    elif choice == 5:
        boolean = 1
    elif choice == 6:
        boolean = 1
    else:
        print("Please choose 1-6")