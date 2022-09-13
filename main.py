# This is the start to a really cool battle royale game. You will start with a list
# of available weapon options. Then choose your weapon of choice.
# Keep up with the game's journey to partake in the rest of the added features.


# This simply outputs this string and starts the game.
print("CHOOSE THE WEAPONS OF YOUR LIKING\n")

# This is an empty list used to add user's choice of accessories if they
# choose to go with the AK-47. It will be utilized more later on for the other
# weapons.
choices = []

# List of weapons user can choose from. List is then printed so users can
# see their options before they choose.
weapons = ['AK-47', 'knife', '9mm',  'sawed-off', 'mossberg']
print(weapons)

# Created for user input. Tells them to now select your choice of weapons and
# accessories.
user = input("Select your weapons below:\n")

# Conditional statements; if user picks the AK-47, they also have the choice of
# adding accessories. Also, it will print the AK-47 with added accessories so they
# can double check what they picked out. And if they choose any other weapon, then they
# are just stuck with the weapon for now. There will be added features later on.
if (user == 'AK-47'):
    print("You have chosen the " + user)
    user2 = input("Do you want to add a 16in barrel or a silencer?\n")
    if (user2 == '16in'):
        print("Your AK-47 is equipped with a 16in barrel.")
        print("THIS IS WHAT YOU HAVE CHOSEN SO FAR:")
        choices.append(user)
        choices.append(user2)
        print(choices)
    elif (user2 == 'silencer'):
        print("Your AK-47 is equipped with a silencer.")
        print("THIS IS WHAT YOU HAVE CHOSEN SO FAR:")
        choices.append(user)
        choices.append(user2)
        print(choices)
elif (user == 'knife'):
    print("You have chosen the " + user)
elif (user == '9mm'):
    print("You have chosen the " + user)
elif (user == 'sawed-off'):
    print("You have chosen the " + user)
elif (user == 'mossberg'):
    print("You have chosen the " + user)

# These will be used later on to hardcode weapon attributes.
range = []
velocity = []
recoil = []
magazine_cap = []
