import time
import subprocess

User = 'Slice'
MysMan = 'Mysterious man'
Message_Lost = 'You lost!'

Quest1 = input("Would you like to start your first quest, " + User + " Y/N: ")
if Quest1 == 'Y':

    while Quest1 == '':
      print("Please enter Y or N")
      Quest1 = input("Would you like to start your first quest, " + User + " Y/N: ")

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
    ChooseWay_Road_Scenario1 = input("Choose from road 1-3: ")
    if ChooseWay_Road_Scenario1 == '1':
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

    elif ChooseWay_Road_Scenario1 == '2':

      print("You took road 2, ")

    elif ChooseWay_Road_Scenario1 == '3':
      print("You took road 3, ")
    
    else:
      print("")
      print("What are you doing?!?!")
      print("")
      print("Make stupid mistakes like these and you lose...")
      print("")
      print(Message_Lost)
      print("")
      time.sleep(2.1)
      input("--press enter--")
      quit()


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

