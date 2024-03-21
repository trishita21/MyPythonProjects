# This is a naive treasure hunt game.

print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.")

print("You are at crossroads. You can go left or right")
dir = input("Which way do you want to go?")

if dir.lower() == "left":
  print("You have come to a lake. There is an island in the middle of the lake.")
  print("You can wait for a boat or swim across.")
  wait = input("Do you want to wait or swim?")
  if wait.lower() == "wait":
    print("You have arrived at the island unharmed. There is a house with 3 doors.\nOne is red, one is yellow, and one is blue.")
    door = input("Which door do you want to open?")
    if door.lower() == "yellow":
      print("You have found the treasure! You win!")
    elif door.lower() == "red":
      print("You have been burned by fire. Game over.")
    elif door.lower() == "blue":
      print("You have been eaten by beasts. Game over.")
    else:
      print("Game over.")
  else:
    print("You have been attacked by trout. Game over.")
else:
  print("You have fallen into a hole. Game over.")
