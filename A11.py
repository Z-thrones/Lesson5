Real_amount = float(input("Please enter the actual product price: "))
Sale_price = float(input("Please enter the price you are selling it at: "))
if Real_amount < Sale_price:
    print("It is profit")
else:
    print("It is a loss")