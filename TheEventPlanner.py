# Task 1: Buggy code
# identify the input as an int.
attendees = int(input("Enter number of attendees: "))
venue = "large hall" if attendees > 100 else "conference room"
print(venue)

# Task 2: Venue selection
if venue == "large hall":
    print("You will need a large audio system for this number of attendees")
else:
    print("A projector will suffice for this many atendees")

# Task 3: 
food = input("What kind of meal would you like? (Meat/Vegetarian): ")
choice = "I recommend Gourmet Meals Caterers" if food == "Meat" else "I recommend Veggie delight Caterers"
print(choice)



