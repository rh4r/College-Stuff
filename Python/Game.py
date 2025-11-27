# Import functions from libraries with aliases for easier reference
from time import sleep as wait                  # Pause execution for a given duration
from math import floor as round                 # Used for rounding damage (downward)
from os import system as SYSTEM_RUN             # Used to clear the terminal screen
from sys import stdout as STANDARD_OUTPUT       # For direct character-by-character output
from random import choice as RANDOM_CHOICE      # Choose random element from a list
from random import randint as RANDOM_INTEGER    # Generate a random integer in a range

# Assign commonly used string and output functions for quick access
upper = str.upper
isupper = str.isupper
flush = STANDARD_OUTPUT.flush
write = STANDARD_OUTPUT.write

# Create storage lists and dictionaries for game logic
Wizards = []  # List to store Wizard objects
Elements = ["Earth", "Fire", "Air", "Water", "Omega"]  # Available elements for wizards
Artifacts = {  # Artifact bonuses mapped by name
    "Excalibur": "2x Damage",
    "Golden Experience Requiem": "2x Health",
    "Sensei Wuu's Golden Staff": "2x Wisdom",
    "Critical Strike": "Chance to deal a CRITICAL strike (4x damage on hit)"
}

# Initialize core game state variables
MainLoop = True
BattleWinner = None
FirstWizardGenerated = None
PlaceholderArtifact1 = None
PlaceholderArtifact2 = None

# ASCII banner for the game intro screen
Banner = """
    ██╗    ██╗██╗███████╗ █████╗ ██████╗ ██████╗      ██╗ ██████╗  ██╗
    ██║    ██║██║╚══███╔╝██╔══██╗██╔══██╗██╔══██╗    ███║██╔═████╗███║
    ██║ █╗ ██║██║  ███╔╝ ███████║██████╔╝██║  ██║    ╚██║██║██╔██║╚██║
    ██║███╗██║██║ ███╔╝  ██╔══██║██╔══██╗██║  ██║     ██║████╔╝██║ ██║
    ╚███╔███╔╝██║███████╗██║  ██║██║  ██║██████╔╝     ██║╚██████╔╝ ██║
    ╚══╝╚══╝ ╚═╝╚══════╝╚═╝  ╚═╝╚═╝  ╚═╝╚═════╝      ╚═╝ ╚═════╝  ╚═╝

"""

# Create the wizard class, each player will get a wizard, and give them base variables.
class Wizard:
    def __init__(self, Name, Element):
        self.Health = 300
        self.Wisdom = RANDOM_INTEGER(10, 15)
        self.Name = Name
        self.Element = Element


# Simulates typing effect by writing characters one-by-one
def WriteTextOnScreen(text_to_write):
    for character in text_to_write:
        write(character)
        flush()
        wait(0.0000000000000000000000000000000000000000000000000000000000000000000000001)


# Clears terminal screen
def ClearScreen():
    SYSTEM_RUN("cls")


# Resets game variables and clears wizard list
def RefreshVariables():
    global BattleWinner
    global FirstWizardGenerated
    global PlaceholderArtifact1
    global PlaceholderArtifact2

    BattleWinner = None
    FirstWizardGenerated = None
    PlaceholderArtifact1 = None
    PlaceholderArtifact2 = None

    Wizards.clear()
    ClearScreen()


# Lowercase a string (simplified)
def ReturnLowerStr(string_object):
    return str(string_object).lower()


# Custom function to convert any uppercase characters to lowercase
def ReturnLoweredStr(element_string):
    new_string = ""

    for string_index in range(0, len(element_string)): # for each character in the string
        current_char = element_string[string_index] # find the current character

        if isupper(current_char): # if the character is uppercase then convert it to lowercase through assigning it to the new_string
            new_string = new_string + str.lower(current_char)
        else:
            new_string = new_string + current_char

    return new_string


# Determines whether an attack is a critical hit (25% chance)
def HandleCriticalStrike():
    HitsCritical = RANDOM_INTEGER(1, 4)

    if HitsCritical == 1:
        return True
    else:
        return False


# Calculates elemental (dis)advantage multiplier based on chosen elements
def ReturnElementDisadvantage(Element1, Element2):
    # !! COULD REWORK THIS TO USE A BETTER SYSTEM !! # 

    # Turn each wizards element into a string I can compare to values. 
    StringCheck = Element1 + " Vs " + Element2
    ReturningValue = None

    # Dictionary responsible for holding each value associated with element
    ElementChart = {
        "water Vs fire": 1.5,
        "water Vs earth": 0.8,
        "water Vs air": 1,
        "water Vs water": 0.1,
        "water Vs omega": 1,

        "fire Vs water": 0.5,
        "fire Vs air": 1.2,
        "fire Vs earth": 1.5,
        "fire Vs fire": 1,
        "fire Vs omega": 1,

        "air Vs earth": 1,
        "air Vs fire": 0.8,
        "air Vs air": 1,
        "air Vs water": 1,
        "air Vs omega": 1,

        "earth Vs water": 1.2,
        "earth Vs fire": 0.5,
        "earth Vs air": 1,
        "earth Vs earth": 1,
        "earth Vs omega": 1,

        "omega Vs fire": 1,
        "omega Vs water": 1,
        "omega Vs air": 1,
        "omega Vs earth": 1,
        "omega Vs omega": 2,
    }

    # Loop through the dictionary and check if the value matches the string we created at the beginning. If so, then return the value of the string in the index.
    for BadIndex, BadValue in ElementChart.items():
        if BadIndex == StringCheck:
            print("--- ELEMENT DISAVANTAGE --- ")
            print("      ", StringCheck, "      ")
            print("YOUR ELEMENT DEBUFF: ", BadValue)
            print("----------------------------")
            wait(5)
            ReturningValue = BadValue

    if ReturningValue != None:
        return BadValue
    else:
        WriteTextOnScreen(" FAILED TO CALCULATE THE ELEMENTAL DISADVANTAGE!, RETURNING (1)\n")
        return 1


# Displays elements of a list with index numbers
def PrintArray(Array):
    Count = 1

    for index in Array:
        WriteTextOnScreen(f"\n{Count} {index}")

        Count += 1

# Displays items and bonuses from a dictionary
def PrintDict(Dictionary):
    Count = 1

    for index, value in Dictionary.items():
        WriteTextOnScreen(f"\n    Item {Count}: ({index}) has the added bonus of ({value})")

        Count += 1


# Adds a new wizard to the wizard list
def CreateWizard(name, element):
    if name and element:
        FirstWizardObject = Wizard(name, element)
        Wizards.append(FirstWizardObject)


# Handles artifact selection by the player (random or debug-triggered)
def HandleArtifactIfGenerated(toggle):
    toggle = True
            
    while toggle:
        global PlaceholderArtifact1
        global PlaceholderArtifact2

        Artifact = None
        ArtifactBonus = None
        ChosenArtifact = None
        IsHappyArtifact = None
        IsInteger = None

        print("\n!--------------------------------------------------------------------------!")
        WriteTextOnScreen("You got a rare drop! Choose an artifact to accompany you in the battle:")
        PrintDict(Artifacts)
        print("\n!--------------------------------------------------------------------------!\n")
        WriteTextOnScreen("Please enter either the name of the item, or the number of the item:\n")

        ChosenArtifact = input()

        try:
            int(ChosenArtifact)
            ChosenArtifact = int(ChosenArtifact)
            
            IsInteger = True
        except:
            IsInteger = False

        if IsInteger:
            Count = 0

            for indx, bons in Artifacts.items():
                Count += 1

                if ChosenArtifact == Count:
                    Artifact = indx
                    ArtifactBonus = bons

        elif IsInteger == False:
            for index, bonus in Artifacts.items():
                if index[0] == ChosenArtifact[0] and index[1] == ChosenArtifact[1]:
                    Artifact = index
                    ArtifactBonus = bonus
 
        if Artifact != None:
            WriteTextOnScreen(f"\nYou have chosen: {Artifact}, Is this correct? Y/N\n")

            IsHappyArtifact = ReturnLowerStr(input())

            if IsHappyArtifact[0] == "n":
                ClearScreen()
            else:
                toggle = False

                if FirstWizardGenerated == None:
                    PlaceholderArtifact1 = Artifact
                elif FirstWizardGenerated != None:
                    PlaceholderArtifact2 = Artifact

                return Artifact, ArtifactBonus


# Gets user input for wizard creation, including optional artifact
def InitalizeInputs():
    # Regular game variables
    global FirstWizardGenerated
    Name = None
    Element = None
    Success = None
    IsRunning = True

    # If artifact is decided to run, these variables need to be in memory
    Artifact = None
    ArtifactBonus = None
    IsRunningArtifact = None
    IsIntOrChar = None

    # Main Loop
    while IsRunning:
        WriteTextOnScreen(f"\n\n Welcome to wizard 101!\nA game about battling wizards, enter your name to begin:")
        Name = ReturnLowerStr(input())

        # Criteria to determine if wizard gets an artifact
        if Name == "debug" or RANDOM_INTEGER(1, 5) == 1:
            Artifact, ArtifactBonus = HandleArtifactIfGenerated(IsRunningArtifact)

        WriteTextOnScreen(f"\nThank you {Name}! Now, select your element (NAME):")
        PrintArray(Elements)

        Element = ReturnLoweredStr(input("\n"))

        # Subroutine to check if the first character in a string "[E]arth", and also randomly generate an element if they don't select a valid one
        count = 0

        for index in Elements:
            count = count + 1

            if upper(Element[0]) == index[0]:
                Element = ReturnLoweredStr(index)
                Success = True
                break

            elif str(Element) == str(count):
                Element = Elements[(int(count) - 1)]
                Success = True
                break
        
        if not Success:
            Element = ReturnLoweredStr(RANDOM_CHOICE(Elements))
            
        WriteTextOnScreen(f"\nYou have selected:\nName:{Name}\nElement:{Element}\nIs this correct 'Y' or 'N'?\n")

        if Artifact:
            WriteTextOnScreen(f"( ARTIFACT: You have selected the artifact: {Artifact} with the bonus of {ArtifactBonus}! )\n")

        # Ask the user if they're happy with their choices, and if so continue.
        IsHappy = ReturnLowerStr(input())

        if IsHappy[0] == "y":
            IsRunning = False
        else:
            Name = None
            Element = None

    # Call external functions
    CreateWizard(Name, Element)
    ClearScreen()

    # Subroutine to error-handle incase both users are given an artifact
    if not FirstWizardGenerated:
        FirstWizardGenerated = True


# Executes the battle between two wizards using all combat logic
def BeginBattle(Wizard1, Wizard2):
    global BattleWinner # Create a reference to the global "BattleWinner" variable, which will hold the winning wizards name.
    global PlaceholderArtifact1 # The first wizards Artifact, if they have one else it's None type.
    global PlaceholderArtifact2 # The second wizards Artifact, if they have one else it's None type.

    Count = 1 # Variable responsible for tracking the number of turns, begins at one.

    print("\n! ... [PLAYER ONE] ! ... \n")
    DisadvantageWizard1 = ReturnElementDisadvantage(Wizard1.Element, Wizard2.Element) # Calculates the elemental disadvantage for the first wizard

    print("\n! ... [PLAYER TWO] ! ... \n")
    DisadvantageWizard2 = ReturnElementDisadvantage(Wizard2.Element, Wizard1.Element) # Calculates the elemental disadvantage for the second wizard

    # For loop in order to wait four seconds and begin the battle
    for wait_index in range(1, 4): 
        print("BATTLE BEGINS IN: ", wait_index)
        wait(1)
    print("\n\n\n======[ BEGIN! ]======")

    if Wizard1 and Wizard2: # Conditonal to ensure that both wizards actually exist
        # If the artifacs is one effecting the health, run the calculations for it.
        if PlaceholderArtifact1 == "Golden Experience Requiem":
            Wizard1.Health = Wizard1.Health * 2
        if PlaceholderArtifact2 == "Golden Experience Requiem":
            Wizard2.Health = Wizard2.Health * 2


        while Wizard1.Health > 0 and Wizard2.Health > 0: # While both wizards are alive, continue the function
            # Allow for easier calling of wizard names
            WizardName = Wizard1.Name
            Wizard2Name = Wizard2.Name

            # Randomly generate "Wisdom" which is responsible for one of the damage multipliers
            Wizard1.Wisdom = RANDOM_INTEGER(10, 15) 
            Wizard2.Wisdom = RANDOM_INTEGER(10, 15)

            # If the artifacs is one effecting the wisdom, run the calculations for it.
            if PlaceholderArtifact1 == "Sensei Wuu's Golden Staff":
                Wizard1.Wisdom = Wizard1.Wisdom * 2

            if PlaceholderArtifact2 == "Sensei Wuu's Golden Staff":
                Wizard2.Wisdom = Wizard2.Wisdom * 2


            # Calculate the damage for each wizard, round the value so no decimal points. (To avoid the health being stuck on something such as 0.4)
            Wizard1Dmg = round(Wizard1.Wisdom * DisadvantageWizard1)
            Wizard2Dmg = round(Wizard2.Wisdom * DisadvantageWizard2)

            # WIZARD ONE:
            # If the artifacs is one effecting the damage, run the calculations for it.
            if PlaceholderArtifact1 == "Excalibur":
                Wizard1Dmg = Wizard1Dmg * 2

            # If the artifact is the one inwhich involves a 'CRITICAL CHANCE' then do run the function and calculate damage accordingly.
            elif PlaceholderArtifact1 == "Critical Strike":
                if HandleCriticalStrike() == True:
                    print(" .   .   .  WIZARD 1 HAS HIT A CRITICAL STRIKE 4x DAMAGE DONE .   .   .  ")
                    Wizard1Dmg = Wizard1Dmg * 4

            # WIZARD TWO:
            # If the artifacs is one effecting the damage, run the calculations for it.
            if PlaceholderArtifact2 == "Excalibur":
                Wizard2Dmg = Wizard2Dmg * 2

            # If the artifact is the one inwhich involves a 'CRITICAL CHANCE' then do run the function and calculate damage accordingly.
            elif PlaceholderArtifact2== "Critical Strike":
                if HandleCriticalStrike() == True:
                    print(" .   .   .  WIZARD 2 HAS HIT A CRITICAL STRIKE 4x DAMAGE DONE .   .   .  ")
                    Wizard2Dmg = Wizard2Dmg * 4

            # Creates a variable to figure out the new health of both wizards, after the damage has hit them.
            Wizard1NewHealth = (Wizard1.Health - Wizard2Dmg)
            Wizard2NewHealth = (Wizard2.Health - Wizard1Dmg)

            # Error handling to ensure if either player goes below 0 potential health, the other wins.
            if Wizard1NewHealth < 0:
                Wizard1.Health = 0
                BattleWinner = Wizard2.Name
                break

            elif Wizard2NewHealth < 0:
                Wizard2.Health = 0
                BattleWinner = Wizard1.Name
                break

            elif Wizard1NewHealth > 0 and Wizard2NewHealth > 0: # If both wizards are above 0 health, then continue.
                # Assign the new health values to the actual health.
                Wizard1.Health = Wizard1NewHealth
                Wizard2.Health = Wizard2NewHealth

                # Display the information
                print(f"\nATTACK TURN {Count}")
                print(f"{WizardName} now has: {Wizard1.Health} and taken {Wizard2Dmg}")
                print(f"{Wizard2Name} now has: {Wizard2.Health} and taken {Wizard1Dmg}\n")
                wait(1)
                Count += 1

        # Winner calculation is decided once either Wizard1.Health or Wizard2.Health <= 0
        if Wizard1.Health <= 0 and Wizard2.Health > Wizard1.Health:
            BattleWinner = Wizard2.Name
        else:
            BattleWinner = Wizard1.Name

# Main game loop
while MainLoop:
    EndGame = None

    print(Banner)

    # Setup phase: create two wizards
    while len(Wizards) != 2:
        InitalizeInputs()

    # Run battle between created wizards
    BeginBattle(Wizard1=Wizards[0], Wizard2=Wizards[1])

    # Print the winner of the battle
    print(f"    !! BATTLE HAD ENDED !!\n       Our winner is...{BattleWinner}")
    print("Would you like to play again? Y/N")

    # Check for replay input
    EndGame = ReturnLowerStr(input())

    # Check if what the user inputted is a valid string to be compared to 
    if isinstance(EndGame, str) or isinstance(EndGame[0], str):
        if EndGame == "n" or EndGame[0] == "n":
            MainLoop = False
        else:
            RefreshVariables()            
