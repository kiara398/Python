
print("Welcome to WinnieFred Bank")
Trials = 3
UserPin = 9876

while Trials != 0:
    Pin = int(input("Please Enter Your 4 digit pin number: "))
    if Pin != UserPin:
        Trials -= 1
        print("Wrong pin number, you have", Trials, " trials left")
    else:
        myChoice = input("d: Deposit or w: Withdraw: ")
        if myChoice == "d":
            myDeposit = input(" Enter The Amount You Would like to Deposit: ")
            print(myDeposit, " has been deposited into your account")
        if myChoice == "w":
            myWithdraw = input(" Enter The Amount You Would like to Withdraw: ")
            print(myWithdraw, "has been withdrawn from your account")
    myExit = input(" Would You like to continue? Y/N: ")
    if myExit == "N":
        print("Thank you for using WinnieFred Bank")
        break
    else :
        continue

        

