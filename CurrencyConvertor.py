from pip._vendor.distlib.compat import raw_input


def currencyConverter():
    choice= input("Please select your choice of operation"
    "\n1. Dollar to Rupee "
    "\n2. Rupee to Dollar ")
    #print("\nYou selected- ", choice)

    if choice == "1":  #convert dollar to rupee
        userDollar = int(input("Please Enter $ amount to convert"))
        rupee = userDollar * 66.58
        print(" $ %0.2f" %userDollar, "= Rs. %0.2f " %rupee)
        doAgain()
    elif choice == "2": #convert rupee to dollar
        userRupee = int(input("Please Enter Rs amount to convert"))
        dollar= userRupee * 0.015
        print("\n Rs. %0.2f " %userRupee, "= $ %0.2f " %dollar)
        doAgain()
    else:   #wrong choice 
        print("wrong choice please try again")
        currencyConverter()
        
def doAgain():  #A function to prompt again for conversion
    again = raw_input("Do you want to do it again?"
    "\n1. Yes "
    "\n2. No")
    #print("\nYou selected- ", again)  
    if again == "1":
        currencyConverter()
    elif again == "2":
        print("Thank you. Do visit again")
    else:
        print("Invalid choice please try again.")
        doAgain()
        
currencyConverter() #call this function to convert