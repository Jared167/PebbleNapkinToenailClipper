import random

print("These are the rules:")
print(" pebble vs napkin -> napkin wins")
print(" napkin vs toe nail clipper -> toe nail clipper wins")
print(" pebble vs toe nail clipper -> pebble wins\n")

while True:
    print("Pick:")
    print(" 1 - pebble")
    print(" 2 - napkin")
    print(" 3 - toe nail clipper")

    choice = int(input("Enter your choice: "))
    while choice > 3 or choice < 1:
        choice = int(input("Invalid choice. Enter 1, 2, or 3: "))

    if choice == 1:
        choice_name = 'pebble'
    elif choice == 2:
        choice_name = 'napkin'
    else:
        choice_name = 'toe nail clipper'

    print("Your choice is:", choice_name)
    print("Now the computer will decide...")

    rps_comp = random.randint(1, 3)
    if rps_comp == 1:
        comp_choice_name = 'pebble'
    elif rps_comp == 2:
        comp_choice_name = 'napkin'
    else:
        comp_choice_name = 'toe nail clipper'

    print("Computer choice is:", comp_choice_name)
    print(choice_name, "vs", comp_choice_name)

    if choice == rps_comp:
        result = "draw"
    elif (choice == 1 and rps_comp == 2) or (choice == 2 and rps_comp == 1):
        result = "napkin"
    elif (choice == 1 and rps_comp == 3) or (choice == 3 and rps_comp == 1):
        result = "pebble"
    elif (choice == 2 and rps_comp == 3) or (choice == 3 and rps_comp == 2):
        result = "toe nail clipper"

    if result == "draw":
        print("It's a draw!")
    elif result == choice_name:
        print("You win!")
    else:
        print("Computer wins!")

    ans = input("Do you want to play again? (y/n): ")
    if ans.lower() != 'y':
        print("Thanks for playing!")
        break
