
firstNames = []
chipTotals = []
buyBacks = []
buyIn = 0
totalChips = 0

# count is for how many people were in your game loop
count = 0


def getTotalChipCount(chipTotals): 
    chipCount = 0
    j = 0
    for i in chipTotals:
        if (buyBacks[j] > 1):
            chipCount += i + (buyBacks[j] * buyIn)
            j+=1
        else:
            chipCount += i
            j+=1
    return chipCount


def distributeChips(firstNames, chipCount, chipTotals):
    # Best Variable Names Ever
    owePeople = []
    owedPeople = []
    chipTotalsSorted = chipTotals.sort()

    # fill up owe and owed, people who broke even should be 
    for chips in range(len(chipTotalsSorted)):
        if chips <= 500:
            owePeople.append(chips)
        else: 
            owedPeople.append(chips)
    print("owePeople : " + str(owePeople) + "\n" + "owedPeople: " + str(owedPeople))
    

    
    



# Gather information
numPeople = int(input("How many people were in your game? "))
buyIn = int(input("What was the buyIn for your game? "))
while count < numPeople:
    firstName = input("Player first name: ")
    chipTotal = int(input("How many chips did you have at the end of the game? "))
    buyBack = int(input("How many times did you buy back in? (excluding the first buy in) "))

    firstNames.append(firstName)
    chipTotals.append(chipTotal)
    buyBacks.append(buyBack)
    count+=1

chipCount = getTotalChipCount(chipTotals)

print(firstNames, chipTotals, buyBacks)
print("\n")
print(chipTotals)
print("\n")
distributeChips(firstNames, chipCount, chipTotals)
# math time 




    