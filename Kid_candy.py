#Create a loop that prints all of the candies in the store to the terminal with their index stored in brackets beside them.
#Create list for candy
candyList = ["snickers", "skittles", "m&m's", "gummies", "peanutbutter cups", "twix", "mars"]
#create variable for allowance
allowance = 5
#create variable for candy cart to hold the candy selections- need to be a list
CandyCart = []
#create the loop to print the candy
for candy in candyList:
    print("[" + str(candyList.index(candy)) + "]" + candy )
#create loop that runs through the amount of allowance
x = "yes"
while x == "yes":
#create input for user selecting candy by number
    selected = input("Which candy would you like?")
#create input for "would you like more candy"
    x = input("would you like more candy?")
#add the candy to the CandyCart
    CandyCart.append(candyList[int(selected)])
#loop through CandyCart to say what candies were brought home
print("I bought this candy")
for candy in CandyCart:
    print(candy)



