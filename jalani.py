#These are the variables that will store the users' inputs when prompted to answer each question
billAmount = float(input('How much was the bill?: '))
levelOfService = input('Was the service good, fair, or bad?: ')
numberOfSplits = int(input('How many heads was fed, my guy?: '))

#These "if-statements" will take the users' respons to the question about the level of service and calculate a tip based on that level of service relative to the value they iputted for the bill amount
# The variable "tip" is created and calculated only if the user inputs "good", "fair", or "bad". Currently ".20, .15, and .19" are just "MAGIC NUMBERS" with no labels or explanations of their existence
    # consider setting a default value for the variable "tip" out side of these if statements
if levelOfService == "good":
    tip = billAmount * .20
elif levelOfService == "fair":
    tip = billAmount * .15
elif levelOfService == "bad":
    tip = billAmount * .10
else:
    print("Good, fair, or bad????")

#These are the variables that reflect the total cost of the meal as well as the cost per person should multiple people partake in the meal
totalAmount = tip + billAmount
splitAmount = totalAmount / numberOfSplits

#The following will print the tip, total amount, and amount per person based on the users' input
print('Tip amount: $%.2f' % (tip))
print('Total amount: $%.2f' % (tip + billAmount))
print('Amount per person: $%.2f' % (splitAmount))

#4/25/18
#This program will error if the user doesn't input the proper data type when prompted.
#Debug this later when you have an understanding of loops and "try / except"
    #You want to print a message to the user telling them to input something useable and then prompt them again to input the correct data type