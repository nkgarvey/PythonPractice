#create list of pies
PieList = ["(1)Pecan", "(2)Apple", "(3)Bean", "(4)Cherry", "(5)Blueberry","(6)Chocolate"]
#Create a list to track all of the pies purchased
PieBucket = []
print("Welcome to The House of Pies! Here are our pies!-----------------")
print(PieList)
#create while loop to see if they would like to make another order
x = "yes"
while x == "yes":
#take the input of their order 
    selected = input("Which pie would you like to order?")
    print("Great!  We'll have" + (Pie in (PieList)) + "right out for you")
    x = input("would you like to make another order?")
#add it to the PieBucket
    PieBucket.append(PieList[int](selected + 1))
    print(PieBucket)

