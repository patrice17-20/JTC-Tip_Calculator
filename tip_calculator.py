# A meal for 1



print("This is a Calculator to help split the bill")
total_bill = float(input("what is the total bill?: "))
percentage_tip = int(input('what % tip would you like to give to your waiter?'))
number_of_people = int(input('How many people are splitting the bill?: '))

payment_per_person = (round(float(((percentage_tip / 100 + 1) * total_bill) / number_of_people) , 2))

print(f'Each person owes : ${ payment_per_person}')

payment_per_person = ("%.2f" % round(float(((percentage_tip / 100 + 1) * total_bill) / number_of_people), 2))
tip_amount = "%.2f" % float(percentage_tip / 100  * total_bill)

print(f"Tip amount: ${tip_amount}")
# 

total_bill_float = float(total_bill)
tip_amount_float = float(tip_amount)
tip_and_total = (total_bill_float+tip_amount_float)
print(f"Total bill including tip: ${tip_and_total}")


# I tried to do it on my own but i went to google, the math equations are very hard for me


