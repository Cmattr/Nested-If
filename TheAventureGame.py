# Task 1: Buggy code
place = input("Choose a place: forest or cave? ")
# use == to see if the user input for place is equall to forest
if place == "forest":
    action = input("climb a tree or cross a river?")
    # use == to see if the user input for action is equall to climb a tree
    if action == "climb a tree":
        print("You found a bird's nest!")
    # remove (action = "cross a river")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
# use == to see if the user input for place is equall to cave
elif place == "cave":
    print("You find a hidden treasure!")
    # Task 2: Setting the scene
    dark =  input("would you like to light a torch or proceed in the dark?")
    if dark == "light a torch":
        print("The torch has been lit")
    elif dark == "proceed in the dark":
        print("the darkness surrounds you")
    else:
        pass