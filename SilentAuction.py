def get_float(): #consider passing prompt as parameter

#function prompts for floating number and returns it
    choice=float(input("what is the reserve price?")); #validate as appropriate using try command
    return choice;

#initialise variables…

highestBid = 0
bidCount = 0
name = " "
reservePrice =0
bids = []
names = []
F=""

reservePrice = get_float();
print(reservePrice)


while name.upper()!= 'F': #user enters F to finish
    print ("Highest bid so far is",highestBid)
    name = input("What is your name?") #could use a function to get a validated name
    if name.upper() != F:
        bid = get_float();
    if bid > highestBid:
        highestBid = bid;
        bids.append(bid); #corresponding lists
        names.append(name);
        bidCount += 1;
    else:
        print("Sorry " + name + " You'll need to make another, higher, bid.");
    if highestBid >= reservePrice:
        print( "Auction won",names[bidCount - 1], "at", bids[bidCount - 1]);
    else:
        print("Auction did not meet reserve price")

for i in range (bidCount): #Show list of bids
    print(names[i], bids[i]);
