def negativeCheck(number1, number2):
    if number1 < 0:
        print("One of the Numbers is a Negative, Please Try Again.")
        primaryProcess()

    if number2 < 0:
        print("One of the Numbers is a Negative, Please Try Again.")
        primaryProcess()

    else:
        return


def primaryProcess():
    CostPrice = int(input("Cost Price:"))
    SellPrice = int(input("Sale Price:"))

    negativeCheck(CostPrice, SellPrice)

    if SellPrice < CostPrice:
        margin_status = "Loss"
        amount = SellPrice - CostPrice
    else:
        margin_status = "Profit"
        amount = CostPrice - SellPrice

    print(margin_status, amount)


primaryProcess()