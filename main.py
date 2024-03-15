print("Welcome to the GC Fruit Market!")
name = input("What is your name?")
price = 0
subTotal = 0
numApples = 0
numGrapes = 0
numOranges = 0
shopping = "y"
fruitStr = ""
while shopping == "y":
    fruit = int(input("Welcome " + name + ". Which Fruit would you like to buy?" + """
    1. Apple $2
    2. Grape $1
    3. Orange $3
    """))
    if fruit == 1:
        fruitStr = "Apple"
        price = 2
        numApples += 1
    elif fruit == 2:
        fruitStr = "Grape"
        price = 1
        numGrapes += 1
    elif fruit == 3:
        fruitStr = "Orange"
        price = 3
        numOranges += 1
    else:
        print("please enter a valid fruit")
    subTotal += price
    print("You Bought 1 " + fruitStr + " at " + str(price))
    shopping = input("Would you like to buy another piece of fruit? y/n")

tax = subTotal * .05
totalCost = tax + subTotal
print("Order for "+name+"""
""" + str(numApples)+" apple(s) at $2 apiece"+"""
""" + str(numGrapes)+" grape(s) at $1 apiece"+ """
""" + str(numApples)+" orange(s) at $3 apiece"+"""
Sub Total: $""" + str(subTotal) + """
5% Tax $"""+str(tax) + """
Total: $"""+str(totalCost))
