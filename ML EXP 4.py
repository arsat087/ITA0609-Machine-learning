balance = 50000
pin = 1234

p = int(input())
amt = int(input())

if p == pin:
    if amt <= balance:
        print("Balance =", balance)
        print("Withdrawal Successful")
        print("Remaining Balance =", balance - amt)
    else:
        print("Insufficient Balance")
else:
    print("Invalid PIN")
