
# Imports
import sys
import subprocess
import time

# Variables
Message_Start = "Start"
Message_Exit = "Closed game"
Message_Lost = "You lost!"
TimeX = 5
Secret_Message = '01010011 01101000 01100001 01110010 01100101 00100000 01110100 01101000 01101001 01110011 00100000 01100111 01100001 01101101 01100101 00100000 01110111 01101001 01110100 01101000 00100000 01111001 01101111 01110101 01110010 00100000 01100110 01110010 01101001 01100101 01101110 01100100 01110011 00100001'
MysMan = "Mysterious man"

# Intro
print("Welcome to Adventureotopia!, bought to you by SliceOnePiece, and with the help of Python Documentation LoL")
print("")
time.sleep(1.5)
print("This is an adventure game about a character who wants to find the lost treasure of the once greatest swordsman in the world!")
print("")
time.sleep(3.5)
print("If you feel you have finished this game you I can give you")
print("the script of the game and edit things in it!")
time.sleep(0.6)
print("")
input("--press enter--")
subprocess.run('cls', shell=True)

# wa
print("Warning: Say Yes and No in capital ex. Y or N. If you don't do ths you might mess up in the game!")
time.sleep(1.6)
print("")
input("--Press enter--")
print("")

# Asking if you want to play or you've changed your mind
Menu_Begin = input("Hello there would you like to Play? Y/N: ")
print("")
if Menu_Begin == 'Y':
  print("Ok let's play")
  print("                 ")
  print("Loading...")
  print("                 ")
  # Countdown timer for loading 
  while TimeX > 0:
    print(TimeX)
    time.sleep(1)
    TimeX -= 1
    print("                 ")
  input("_Press enter_")
  subprocess.run('cls', shell=True)
  # Subprocess clear the terminal

  # User's details
  print("--User details--")
  print("                 ")
  print("Username Min: 8 characters, Max: 16 characters")
  print("")
  User = input("Enter username: ")
  while User == '' or len(User) < 8 or len(User) > 16:
    print("Please enter a valid name!")
    User = input("Enter username: ")
  User = User.strip().capitalize().title()
  print("                 ")
  time.sleep(0.95)
  subprocess.run('cls', shell=True)
  
  print("Hello,", User + "!")
  print("                 ")
  time.sleep(0.89)

  print("Warning: game desn't save!")
  print("                 ")
  time.sleep(0.9)

  input("_Press enter_")
  subprocess.run('cls', shell=True)

# Starting of game
  print("Narrator: *Wakes up near a tree*")
  print("                 ")
  time.sleep(1.5)
  input("_Press enter_")
  subprocess.run('cls', shell=True)
  
  print( User + ": Where am I what am I doing here?")
  print("                 ")
  time.sleep(1.5)
  input("_Press enter_")
  subprocess.run('cls', shell=True)

  print("Narrator: A mysterious man in a black cloack walks to you saying,")
  print("")
  time.sleep(1.5)
  input("_Press enter_")
  subprocess.run('cls', shell=True)

  print(MysMan + ": You are the chosen one!")
  print("")
  time.sleep(1.5)
  input("_Press enter_")
  subprocess.run('cls', shell=True)

  print(User + ": Who are you?")
  print("")
  time.sleep(1.5)
  input("_Press enter_")
  subprocess.run('cls', shell=True)

  print(MysMan + ": Just another man like you, and by the way I wanna give you a quest would you accept it?")
  print("")
  time.sleep(2)
  input("_Press enter_")
  subprocess.run('cls', shell=True)
  
  # First quest
  Quest1 = input("Would you like to start your first quest, " + User + " Y/N: ")
  if Quest1 == 'Y':

    print("")
    print(User + ": Uhh... yeah sure, but who are you?")

    print("                 ")
    print(MysMan + ": I am 'A' and your quest is to kill 100 goblins")
    print("")
    time.sleep(1.5)

    print(User + ": What does A..")
    print("")
    time.sleep(1)
    input("_Press enter_")
    subprocess.run('cls', shell=True)

    print("Narrator: The man in the black cloak dissapears!")
    print("")
    time.sleep(1)

    print("Narrator: You stand up and go on the journey to kill 100 goblins.")
    print("")
    time.sleep(1.2)

    print("You did this out of true fear as the quest he gave you sounded more like a life threat...")
    print("")
    time.sleep(1)
    input("_Press enter_")
    subprocess.run('cls', shell=True)
    
    print("You start walking to a nearby forest to kill goblins.")
    print("")
    time.sleep(1.2)
    print("You go into a forest leading to three roads.")
    print("")
    
    # Choosing the road 1st Scenario
    ChooseWay_Road_Scenario1 = int(input("Choose from road 1-3: "))
    if ChooseWay_Road_Scenario1 == 1:
      print("")
      print("You took road 1, and instantly regretted it after")
      time.sleep(2)
      print("seeing a camp of goblins and ran away from it")
      time.sleep(2)
      print("until you reached an abondened house.")
      print("")
      time.sleep(2)
      print(
          "You lock the door of the house and then see a glowing katana inside which is in the middle of hundreds of dead skeletons!"
      )
      print("")
      time.sleep(3)
      
      print("The pedalstal that the katana was stuck in had some writing on it, and the writing read..")
      print("")
      time.sleep(2)
      
      print("This is the Cursed katana of the undead samurai, only worthy will live.")
      print("")
      time.sleep(2)
      
      Pickup_katana_scenario = input("Take the risk of picking up the katana? Y/N: ")
      if Pickup_katana_scenario == 'Y':
        
        print("")
        print("You take out the katana from the pedestal, and huge amount of power rushing through your body.")
        print("")
        time.sleep(2)
        # will continue from here
        
      else:
        
        print("")
        print("You decide to stay in the abondened house until tommorow")
        print("")
        time.sleep(2)
        
        print("You wake up the next morning, but you find yourself on the clouds")
        print("")
        time.sleep(2)
        
        print("Game: You got killed by a ghost that lived in the abondened house..")
        print("")
        time.sleep(2)
        
        print(Message_Lost)
        time.sleep(1.5)
        
        quit()

    elif ChooseWay_Road_Scenario1 == 2:

      print("You took road 2, ")

    elif ChooseWay_Road_Scenario1 == 3:
      print("You took road 3, ")
    
    else:
      while ChooseWay_Road_Scenario1 > 3:
        print("Not valid!")



  else:
    print(
        "You thought avoiding the quest will give you freedom, but while walking into a forest.."
    )
    time.sleep(1.5)
    print("                 ")
    print("You tripped..")
    time.sleep(1)
    print("                 ")
    print("Hit a rock..")
    time.sleep(1.5)
    print("                 ")
    Dying_Scenario_1 = input("You are seriously injuired in the middle of the forest, Give up Y/N? ")
    if Dying_Scenario_1 == 'Y':
      print("")
      print("You stabbed yourself with a knife and let your soul leaves your body!")
      print("")
      time.sleep(1)
      print(Message_Lost)
      quit()

    else:
      print("")
      print("You start to walk more deeper into the forest while limping.")
      time.sleep(1)
      print("                 ")
      print("An animal appears...")
      print("it has a shiny crown, surrounded by dark-ness, ")
      time.sleep(1.5)
      print("has red eyes, and a big bloody red blade comes to you...")
      time.sleep(1.5)
      print("                 ")
      print("Stabs you...")
      time.sleep(3.5)
      print("                 ")
      print("*-You died!-*")
      print("                 ")
      print(Message_Lost)
      time.sleep(1)
      quit()
else:
  # secret message
  Secret_message_que1 = input("Do you want to know the secret message? Y/N: ")
  if Secret_message_que1 == 'Y':
    print("")
    print("Secret message is:", Secret_Message)
    print("")
    time.sleep(3.9)
    print(Message_Exit)
    time.sleep(1.2)
    quit()
    
  else:
    print("")
    print(Message_Exit)
    time.sleep(1.5)
    quit()
  
  # Don't know why this exists just keeping it cause not wanna mess up game
  print(Message_Exit)
  time.sleep(1.2)
  quit()

