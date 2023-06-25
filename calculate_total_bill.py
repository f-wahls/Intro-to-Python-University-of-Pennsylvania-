bill = float(input("How much is the meal?"))#cast to a float to allow users to enter decimal
tax = float(input("What is the sales tax percentage?"))
tip = float(input("How much of a tip(percentage)?"))



#Calculate and add tax
tax_amount = (bill * tax) / 100 #calculate the tax
total = bill + tax_amount #add tax amount to final bill

#Calculate and add tip
tip_amount = (total * tip) / 100 #calculate the tip
total = total + tip_amount #add tip amount to final bill


#round the total to 2 decimal places
total = round(total, 2) #round the total amount



#print the final amount
print("The total bill is $", total)
