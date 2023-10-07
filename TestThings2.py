import time

Message_Lost = 'You lost!'

ChooseWay_Road_Scenario1 = input("Choose from road 1-3: ")
if ChooseWay_Road_Scenario1.isdigit == int('1'):
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
        print("You take out the katana from the pedestal, and nothing happens.")
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
    print(Message_Lost)
    input("--press enter--")
    time.sleep(1.5)
    quit()