#
# byron.py
#
# Trapped in a cabin with Lord Byron simulator/RPG.
# Original concept and rules by Oliver Darkshire: Henry Sotherans, LTD.
#
# Coded by Imaginos the Quantum Magician 20220326
#
# 20220327 Completely refactored since it's not just me looking at it now.
#

import random

# Declare global/main variables
# What level of scandal are you at?
scandal = 0
# How close are you to your masterpiece?
masterpiece = 0
# How stressed has Byron gotten you?
stress = 0
# Has one of Byron's disasters happened yet?
disaster = 0

#
# Now, define the methods
#

# The Introduction.
def Introduction():
    print("")
    print("TRAPPED in a cabin with LORD BYRON.")
    print("")
    print("You are on vacation with Lord Byron in his holiday home,")
    print("but the weather has trapped you and your friends inside the house.")
    print("")
    print("Only the strong will survive.")
    print("")

def ItsADisaster(event):
# Declare the global variables in use here.
    global scandal
    global masterpiece
    global stress

    print("")
    print("Disaster occurs!")
    print("")
    print("Byron destroyed your masterpiece either by accident or on purpose during one of his episodes.")
    print("")
    if (event < 3):
        print("(At least it rescued your reputation.)")
        scandal = 0
    elif (event < 5):
        print("(You must begin anew.)")
        masterpiece = 0
    else:
        print("(But at least now you can relax.)")
        stress = 0


# The basic response to a new happenstance.
def basicResponse(happenstance, event, events):
# Whatever the happenstance, the basic response is the same.
# Print out the happenstance category, the event, and then
#    adjust scandal, masterpiece, and stress levels.

# Declare the global variables in use here.
    global scandal
    global masterpiece
    global stress

    eventsIndex = event - 1
    print(happenstance, end = "\t")
    print(events[eventsIndex][0])
    scandal += events[eventsIndex][1]
    masterpiece += events[eventsIndex][2]
    scandal += events[eventsIndex][3]

# We've had a recreation. Let's find out which one.
def Recreations(event):

# Array layout is text, scandal, masterpiece, stress.
    events = [
["Is he aware the walls are exceptionally thin?", 0, 0, 1],
["He's made a mess of your desk in the process.", 0, -1, 0],
["May he borrow your husband? Of course.", 1, 0, -1],
["His half-sister is here, and they are far too intimate.", 2, 0, 0],
["You weary of listening to his exploits.", 0, 0, 2],
["He makes an excellent muse on occasion.", 0, 2, -1]
]

    basicResponse("Byron's Recreations:", event, events)

# Byronic Drama tra la!
def Drama(event):
# Array layout is text, scandal, masterpiece, stress.
    events = [
["He needs help reading his fan mail.", 0, 0, 1],
["He's brought his pet bear. It is not trained.", 0, 0, 2],
["He wants to read you his poetry.", 0, 0, 3],
["He's in the papers. Again. Which means you are too.", 1, 0, 0],
["He broke up with his latest girlfriend/boyfriend.", 2, 0, 0],
["He's found a new skull to use as a goblet.", 3, 0, 0]
]

    basicResponse("Byron's Drama\t:", event, events)

def ABriefRedoubt(event):
# Array layout is text, scandal, masterpiece, stress.
    events = [
["Time alone. Blissful time.", 0, 1, 0],
["He's busy with a paramour.", 0, 0, -1],
["A walk around the house! Underwear on our heads!", 1, 0, 0],
["He has an excellent supply of contraband substances.", 1, 1, 0],
["Wine! A chest of wine!", 0, -1, 0],
["He passed out in his study.", 0, 1, 0]
]

    basicResponse("A Brief Redoubt\t:", event, events)


# Let the user know what they're in for.
Introduction()

# When either scandal, masterpiece, or stress hits 10, the game is over
while ((scandal < 10) and (masterpiece < 10) and (stress < 10)):
    # See what Byronic happenstance is next
    # 1-2 Byron's Recreations, 3-4 Byron's Drama, 5-6 A Brief Redoubt
    what_happened = random.randint(1,6)
    # Each type of happenstance has many events. Which one this time?
    event = random.randint(1, 6)
    # First, check for disaster.
    if (what_happened == 6):
        # Potential disaster -- 3 6s in a row for a disaster
        disaster += 1
        if (disaster == 3):
            ItsADisaster(event)
            # Reset the disaster count. Knowing Byron, it might happen again.
            disaster = 0
            print("")
    else:
        # Had a non-6, reset disaster count
        disaster = 0
    if (what_happened < 3):
        # Byron's Recreations!
        Recreations(event)
    elif (what_happened < 5):
        # Byron's Drama.
        Drama(event)
    else:
        # A brief redoubt.
        ABriefRedoubt(event)

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
