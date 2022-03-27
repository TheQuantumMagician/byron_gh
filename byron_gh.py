#
# byron.py
#
# Trapped in a cabin with Lord Byron simulator/RPG.
# Original concept and rules by Oliver Darkshire: Henry Sotherans, LTD.
#
# Coded by Imaginos the Quantum Magician 20220326
#

import random

scandal = 0
masterpiece = 0
stress = 0
disaster = 0
last_happened = 0

# Let the user know what they're in for.
print("")
print("TRAPPED in a cabin with LORD BYRON.")
print("")
print("You are on vacation with Lord Byron in his holiday home,")
print("but the weather has trapped you and your friends inside the house.")
print("")
print("Only the strong will survive.")
print("")
 
# When either scandal, masterpiece, or stress hits 10, the game is over
while ((scandal < 10) and (masterpiece < 10) and (stress < 10)):
    # See what Byronic event is next
    # 1-2 Byron's Recreations, 3-4 Byron's Drama, 5-6 A Brief Redoubt
    what_happened = random.randint(1,6)
    event = random.randint(1, 6)
    if (what_happened == 6):
        disaster += 1
        if (disaster == 3):
            print("")
            print("Disaster occurs!")
            print("")
            print("Byron destroyed your masterpiece either by accident or on purpose during one of his episodes.")
            print("")
            disaster = 0
            if (event < 3):
                print("(At least it rescued your reputation.)")
                scandal = 0
            elif (event < 5):
                print("(You must begin anew.)")
                masterpiece = 0
            else:
                print("(But at least now you can relax.)")
                stress = 0
            print("")
    if (what_happened < 3):
        # Byron's Recreations!
        print("Byron's Recreations:", end = "\t")
        if (event == 1):
            print("Is he aware the walls are exceptionally thin?")
            stress += 1
        elif (event == 2):
            print("He's made a mess of your desk in the process.")
            masterpiece -= 1
        elif (event == 3):
            print("May he borrow your husband? Of course.")
            stress -= 1
            scandal += 1
        elif (event == 4):
            print("His half-sister is here, and they are far too intimate.")
            scandal += 2
        elif (event == 5):
            print("You weary of listening to his exploits.")
            stress += 1
        else:
            print("He makes an excellent muse on occasion.")
            stress -= 1
            masterpiece +=2
    elif (what_happened < 5):
        # Byron's Drama
        print("Byron's Drama:\t", end = "\t")
        if (event == 1):
            print("He needs help reading his fan mail.")
            stress += 1
        elif (event == 2):
            print("He's brought his pet bear. It is not trained.")
            stress += 2
        elif (event == 3):
            print("He wants to read you his poetry.")
            stress += 3
        elif (event == 4):
            print("He's in the papers. Again. Which means you are too.")
            scandal += 1
        elif (event == 5):
            print("He broke up with his latest girlfriend/boyfriend.")
            scandal += 2
        else:
            print("He's found a new skull to use as a goblet.")
            scandal += 3
    else:
        # A Brief Redoubt
        print("A Brief Redoubt:", end = "\t")
        if (event == 1):
            print("Time alone. Blissful time.")
            masterpiece += 1
        elif (event == 2):
            print("He's busy with a paramour.")
            stress -= 1
        elif (event == 3):
            print("A walk around the house! Underwear on our heads!")
            scandal += 1
        elif (event == 4):
            print("He has an excellent supply of contraband substances.")
            scandal += 1
            masterpiece += 1
        elif (event == 5):
            print("Wine! A chest of wine!")
            masterpiece -= 1
        else:
            print("He passed out in his study.")
            masterpiece += 1

print("")
if (scandal >= 10):
    print("You are no longer fit to enter society and must flee to nurse your reputation.")
elif (masterpiece >= 10):
    print("You create a new genre of supernatural horror fiction based on your time with Byron.")
else:
    print("You have reached the limits of your stress.")
    stressedOut = random.randint(1, 2)
    if (stressedOut < 2):
        print("You lose your patience with the man and kill him in a fit of rage.")
    else:
        print("You descend into uncontrollable weeping from which you never emerge.")
