
# get loan details
money_owed = float(input("How much money do you owe, in dollars?\n")) # $50,000
apr = float(input("What is the annual percentage rate?\n")) # 3%
payment = float(input("What will your monthly payment be, in dollars?\n")) # $1,000
months = int(input("How many months do you want to see results for?\n")) # 24

# Divide apr by 100 to make percent, then by 12 to make monthly
monthly_rate = apr/100/12

for i in range(months):

    # add interest
    interest_paid = money_owed * monthly_rate
    money_owed = money_owed + interest_paid

    if (money_owed - payment < 0):
        print("The last payment is", money_owed)
        print("Youpaid off the loan in", i+1, "months.")
        break

    # make payment
    money_owed = money_owed - payment

    # results
    print("Paid", payment, "of which", interest_paid, "was interest", end=' ')
    print("Now I owe", money_owed)
