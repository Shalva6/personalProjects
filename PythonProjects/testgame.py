# imports here
import msvcrt 


# Color classing for better UX
class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


mainArea = [
    [0, 0, 0, 0, 0, 0, 0, 13],
    [0, 0, 0, 2, 0, 0, 0, 0],
    [0, 11, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 12, 0],
    [0, 0, 0, 0, 0, 0, 0, 0],
    [0, 0, 4, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 3, 0, 0]
]
# number 0 represents an empty space.
# number 1 represents the player.
# numbers between 2 and 10 represent collectable food.
# numbers between 11 and 20 represent enemies.

# list of items that can be consumed.
items = [
    {
    "Id": 2,
    "Name": "Cake",
    "Energy": 50
    },
    {
    "Id": 3,
    "Name": "Cookie",
    "Energy": 20
    },
    {
    "Id": 4,
    "Name": "Suspicious soup",
    "Energy": 90
    },
]

# list of enemies that can damage you.
enemies = [
    {
        "Name": "Oogie Boogie",
        "Id": 11,
        "Damage": 20
    },
    {
        "Name": "An Evil Owl",
        "Id": 12,
        "Damage": 40
    },
    {
        "Name": "A Car Going 200 in a 40 zone",
        "Id": 13,
        "Damage": 90
    }
]

# up/down.
x = 0
# left/right.
y = 0
# starting point. X is for the rows, Y is for the position on the rows. 
mainArea[x][y] = 1

def IdChecker():
    # cheks if the number corresponds to the ones in the 'items' section.
    if mainArea[x][y] > 1 and mainArea[x][y] < 10:
        for eachItem in items:
            if mainArea[x][y] == eachItem["Id"]:
                # if id's match, the item is pushed into the inventory.
                game.inventory.items.append(eachItem)
                print("")
                print(f"{bcolors.OKGREEN}You found {eachItem["Name"]}!{bcolors.ENDC}")
                return
            
    # cheks if the number corresponds to the ones in the 'enemies' section.
    if mainArea[x][y] > 10 and mainArea[x][y] < 20:
        for eachEnemy in enemies:
            if mainArea[x][y] == eachEnemy["Id"]:
                # if id's match, the player takes damage according to the enemy info.
                game.health -= eachEnemy["Damage"]
                print("")
                print(f"{bcolors.FAIL}You met {eachEnemy["Name"]} and took {eachEnemy["Damage"]} damage! Ouch!{bcolors.ENDC}")
                return
        
    # continues if there is none.
    return

class Inventory:
    def __init__(self):
        self.items = []
    
    def printInventory(self):
        print("")
        # checks if there is anything to print.
        if len(self.items) > 0:
            for eachItem in self.items:
                print(f"{bcolors.OKCYAN}You have {eachItem["Name"]} in your backpack worth {eachItem["Energy"]} energy.{bcolors.ENDC}")
        else:
            print(f"{bcolors.FAIL}Empty inventory.{bcolors.ENDC}")

    def useFood(self, foodName):
        # removes food from the inventory by their index id.
        counter = -1
        for eachItem in self.items:
            counter += 1
            if eachItem["Name"].lower() == foodName.lower():
                game.energy += eachItem["Energy"]
                print(f"{bcolors.OKBLUE}You ate the food '{eachItem["Name"]}' and gained {eachItem["Energy"]} energy!{bcolors.ENDC}")
                del self.items[counter]
                return
        print(f"No food in the inventory found under the name '{foodName}'.")

class Player:
    def __init__(self):
        self.energy = 100
        self.health = 100
        self.inventory = Inventory()

    # move left function
    def moveLeft(self):
        global y

        # check if the action is possible by checking the borders.
        if (y - 1) < 0:
            print("")
            print(f"{bcolors.FAIL}ERROR: out of bounds.{bcolors.ENDC}")
            return 
        
        # deplete energy if avalable, remove health if energy is 0.
        if self.energy > 0:
            self.energy -= 5
        else:
            self.health -= 5
        
        # turn the previous space into a 0 (aka empty space).
        mainArea[x][y] = 0

        # move character on the field by changing the variable.
        y -= 1

        # check if an item or an enemy was found.
        IdChecker()

        # check if the health hit 0 to not display a false movement confirmation message.
        if game.health > 0:
            # move the character.
            mainArea[x][y] = 1
            print("")
            print(f"{bcolors.OKBLUE}Move has been made successfully.{bcolors.ENDC}")
            print("")

    # move right function
    def moveRight(self):
        global y

        # check if the action is possible by checking the borders.
        if (y + 1) > len(mainArea) - 1:
            print("")
            print(f"{bcolors.FAIL}ERROR: out of bounds.{bcolors.ENDC}")
            return
        
        # deplete energy if avalable, remove health if energy is 0.
        if self.energy > 0:
            self.energy -= 5
        else:
            self.health -= 5

        # turn the previous space into a 0 (aka empty space).
        mainArea[x][y] = 0

        # move character on the field by changing the variable.
        y += 1

        # check if an item or an enemy was found.
        IdChecker()

        # check if the health hit 0 to not display a false movement confirmation message.
        if game.health > 0:
            # move the character.
            mainArea[x][y] = 1
            print("")
            print(f"{bcolors.OKBLUE}Move has been made successfully.{bcolors.ENDC}")
            print("")

    # move up function
    def moveUp(self):
        global x

        # check if the action is possible by checking the borders
        if (x - 1) < 0:
            print("")
            print(f"{bcolors.FAIL}ERROR: out of bounds.{bcolors.ENDC}")
            return
        
        # deplete energy if avalable, remove health if energy is 0.
        if self.energy > 0:
            self.energy -= 5
        else:
            self.health -= 5

        # turn the previous space into a 0 (aka empty space).  
        mainArea[x][y] = 0

        # move character on the field by changing the variable.
        x -= 1

        # check if an item or an enemy was found.
        IdChecker()

        # check if the health hit 0 to not display a false movement confirmation message.
        if game.health > 0:
            # move the character.
            mainArea[x][y] = 1
            print("")
            print(f"{bcolors.OKBLUE}Move has been made successfully.{bcolors.ENDC}")
            print("")

    # move down function
    def moveDown(self):
        global x

        # check if the action is possible by checking the borders
        if (x + 1) > len(mainArea) - 1:
            print("")
            print(f"{bcolors.FAIL}ERROR: out of bounds.{bcolors.ENDC}")
            return
        
        # deplete energy if avalable, remove health if energy is 0.
        if self.energy > 0:
            self.energy -= 5
        else:
            self.health -= 5

        # turn the previous space into a 0 (aka empty space).  
        mainArea[x][y] = 0 

        # move character on the field by changing the variable.
        x += 1

        # check if an item or an enemy was found.
        IdChecker()

        # check if the health hit 0 to not display a false movement confirmation message.
        if game.health > 0:
            # move the character.
            mainArea[x][y] = 1
            print("")
            print(f"{bcolors.OKBLUE}Move has been made successfully.{bcolors.ENDC}")
            print("")

    def printEnergy(self):
        # prints energy and health
        print(f"You have {self.energy} energy and {self.health} health remaining.")

    def printMap(self):
        for row in mainArea:
            print("")
            for eachPoint in row:
                # print 0 (empty space) as a '.'
                if eachPoint == 0:
                    print(".", end = " ")

                # prints 1 (player location) as 'P'
                elif eachPoint == 1:
                    print("P", end = " ")
                
                # prints everything else as a '?'
                else:
                    print("?", end = " ")
        print("")

# function to display tips.
def printTips():
    print("")
    print("0. end.")
    print("(a). move left.")
    print("(d). move right.")
    print("(w). move up.")
    print("(s). move down.")
    print("5. Print energy.")
    print("6. Show map (single print).")
    print("7. Toggle map.")
    print("8. Print inventory.")
    print("9. Eat food.")

# 'load' game.
game = Player()

# toggles.
hintToggle = False
mapToggle = False

# start game.
while game.health > 0:
    # check if the toggles are turned on.
    if hintToggle:
        printTips()
    if mapToggle:
        game.printMap()

    # Choosing action here:
    print("Hit 'H' to toggle game tips on/off.")
    print("Choose your next option: ", end = "")
    option = msvcrt.getch().decode()
    match option.lower():
        case 'h':
            if hintToggle == False:
                hintToggle = True
            else:
                hintToggle = False
        case "0":
            print("Ending game.")
            break
        case "a":
            game.moveLeft()
        case "d":
            game.moveRight()
        case "w":
            game.moveUp()
        case "s":
            game.moveDown()
        case "5":
            game.printEnergy()
        case "6":
            game.printMap()
        case "7":
            if mapToggle == False:
                mapToggle = True
            else:
                mapToggle = False
        case "8":
            game.inventory.printInventory()
        case "9":
            print("")
            game.inventory.useFood(input("What food would you like to use? "))
        case "":
            pass
        case _:
            print("Incorrect command")
if game.health <= 0:
    print(f"{bcolors.FAIL}You lost by losing health.{bcolors.ENDC}")