#----IMPORTS----
import time
import subprocess
import sys
import playsound

# USEFUL LINKS
#I only know lua but if you use a cmd such as script.Parent:FindFirstChild("hello.mp3")

# https://www.fantasynamegenerators.com/sword-names.php

#----ITEM RARITY----
"""
THIS TELLS THE RARITY OF THE ITEM

blue = common
Green = uncommon
yellow = epic 
purple = legendary
red = mythical

SOME MEANING:

kamikaze no Tachi -

divine Tachi
tachi = sabre like sword

"""

#----NAME FOR VILLANS---
# add x after the name if you used it

# Yaminokōtei = 
# Captain Dark = 

#----DEFINE VARIABLES----
def GameEnd():
   print("Game Over!")
   print("")
   time.sleep(1)
   print("Closing...")
   quit()

def Not_Chosen_Path():
   subprocess.run("cls", shell=True)
   red = "\033[0;31m" 
   bright_white = "\033[0;97m"
   print(red + "You have not chosen a path " + User + ".")
   time.sleep(1)
   print(bright_white + "")
   input("--PRESS ANY KEY--")



#----VARIABLES----
nar = 'Narrator:'
mman = 'Mysterious man:'
message_won = 'You won!'
secret_message = '01010011 01101000 01100001 01110010 01100101 00100000 01110100 01101000 01101001 01110011 00100000 01100111 01100001 01101101 01100101 00100000 01110111 01101001 01110100 01101000 00100000 01111001 01101111 01110101 01110010 00100000 01100110 01110010 01101001 01100101 01101110 01100100 01110011 00100001(In Binary)'
start_time = 5
has_sword = False
inventory_road1 = []

#----LOADING COUNTDOWN----
print("\033[97m__Loading__")
while start_time > 0:
  print(start_time)
  time.sleep(1)
  start_time -= 1
subprocess.run('cls', shell=True)
#--------


print("Hello! welcome to a game developed and produced by \033[93m@SliceOnePiece and \033[93m@leviathen0199")
print("\033[97m")
playsound.playsound('ADVENTUREOTOPIA/Audio/hello.mp3')
time.sleep(1)
print("This an adventure game about finding the lost treasure of the Once Greatest Swordsman!")
print("")
time.sleep(1.5)
print("If you feel like you have finished the game then you can create a ticket on discord asking to mod the game!")
print("")
time.sleep(1)
print("WARNING: Don't do stupid things or you'll regret(I MEAN IT!) and Any answer except Y or N will result in a no!!")
print("")
time.sleep(3)
input("--PRESS ANY KEY--")
print("")
#--------

#----GAME STARTS----
game_start = input("Would you like to start playing the game? Y/N: ")
if game_start == ('Y' or 'y'):
    subprocess.run('cls', shell=True)
    #--------

    #----USER DETAILS----
    print("--ENTER USER--")
    print("")
    print("Username Min: 8 characters, Max: 16 characters")
    print("")
    User = input("Enter username: ")
    while User == '' or len(User) < 8 or len(User) > 16:
      print("Please enter a valid name!")
      User = input("Enter username: ")
    User = User.strip().capitalize().title()
    time.sleep(2)
    subprocess.run("cls", shell=True)
    print("Hello " + User +"!")
    print("")
    time.sleep(1)
    input("--PRESS ANY KEY--")
    subprocess.run("cls", shell=True)
    #--------


    #----INTRO TO ACTUAL GAME----
    time.sleep(2)
    print(f"{nar} Your journey begins in a deep and dark forest.")
    print("")
    time.sleep(2)
    print(f"{nar} You look around, confused. Suddenly, a man walks up to you")
    print(f"{nar} In a dark trench coat with a cowboy hat.")
    print("")
    time.sleep(3)
    print(f"{nar} He says to you..")
    print("")
    input("--PRESS ANY KEY--")
    subprocess.run("cls", shell=True)
    print(f"{mman} Hello, {User}.")
    time.sleep(1)
    print("")
    print(f"{User}: How do you know my name?!")
    print("")
    time.sleep(1.25)
    print(f"{mman} Not important, for now, choose a road my friend.")
    print("")
    time.sleep(1)
    #--------

    #----FIRST ROAD CHOICE----
    road_choice1 = int(input(f"{nar} Choose a road, 1, 2 or 3: "))
    if road_choice1 == 1:
       
   #----ROAD 1----

      #----AFTER CHOOSING ROAD 1----
       print("")
       print(f"{nar} You chose road 1 hesitantly, and then the man disappeared...")
       print("")
       time.sleep(2)
       input("--PRESS ANY KEY--")
       subprocess.run('cls', shell=True)
       print(f"{nar} he left a scroll behind as he disappeared, and it read...")
       time.sleep(2)
       print("")
       print(f"{nar} Quest - Kill 100 goblins")
       print("")
       print(f"{User}: How am I expected to kill 100 goblins so easily?!?")
       print("")
       time.sleep(2)
       print(f"{nar} Frustrated you went down road 1 and threw a rock..")
       print("")
       print(f"{nar} Hit a goblin in a goblin camp...")
       print("")
       time.sleep(2)
       input("--PRESS ANY KEY--")
       subprocess.run('cls', shell=True)
       #--------
       
       #----AFTER THROWING ROCK----
       print(f"{nar} you start running away and the goblins spot you and start chasing after you!")
       print("")
       time.sleep(1.5)
       print(f"{nar} after the long chase you lost them and get tired but then...") #K
       print("you spot an abondoned mansion which is like 100m away only!")
       print(f"{nar} You run to the abondened mansion as quickly as you can and once you enter you lock the door behind you.")
       print("")
       time.sleep(3.5)
       input("--PRESS ANY KEY--")
       subprocess.run('cls', shell=True)
       #--------

       #----ABONDONED MANSION----
       print(f"{nar} You take a moment to breathe and find a sword glowing with red particles stuck on a pedalstone and it seems to look very intimidating")
       print(f"You get closer to the pedalstone and find some writing on it...")
       print(f"Stone craving: The weak will die, only worthy will live")
       print("")
       time.sleep(4)
       input("--PRESS ANY KEY--")
       subprocess.run('cls', shell=True)
       #--------

       #----SWORD CHOOSES YOU----
       choose_katana = input("Take the risk of taking out the katana from its place? Y/N: ")
       while choose_katana == '':
          print("Input something")
          choose_katana = input("Take the risk of taking out the katana from its place? Y/N: ")
       if choose_katana == "Y":
          playsound.playsound("ADVENTUREOTOPIA/Audio/drawSword.mp3")
          print("")
          print("Game: Recieved x1 \033[91mKamikaze no Tachi(かみかぜ の たち)")
          print("")
          
          print("----Inventory----")
          inventory_road1.append('x1 Kamikaze no Tachi(かみかぜ の たち)')
          print(inventory_road1) #wait imma try something KK BRO THE AUDIO THING IN PYTHON IS FIRE BTW I am gonna take a 30 hr brake cause I have been trying to add audio since 6:30 it was so frustating
          print("-----------------")
          
          # knT = (Kamikaze no Tachi)
          print("")
          print(f"\033[97m{nar} You took the sword out and your veins started rushing with new power and muscles started to grow!")
          time.sleep(1)
          print(f"{User}: I feel powerful and ready to take on anything!")
          print(f"{nar} Then a ghost approaches you and you use slash once even without touching the ghost..")
          print(f"He then dies!")
          print("")
          time.sleep(2)
          input("--PRESS ANY KEY--")

          subprocess.run('cls', shell=True)
          print(f"{User}: wow, no way!!!")
          rest = input(f"{nar} you start to feel tired rest in the house? Y/N: ")
          if rest == 'Y':
             print("")
             print(f"{nar} You decide to rest in the abondoned house till the next morning...")
             print("")
             input("--PRESS ANY KEY--")
             subprocess.run('cls', shell=True)

             print("\033[91m--Day 2--") # KK
             print("\033[97m")
             input("--PRESS ANY KEY--") 
             subprocess.run('cls', shell=True)

             print(f"{nar} You wake up with loud YAWN.")
             print("")
             print(f"{User}: *Yawns*")
             print("")
             print(f"{nar}: You start walking around the house and barely avoid a trap!")
             print(f"")

             #continue
          else:
             print("")
             print(f"{nar} You decide to explore the house and accidently step on a trap because of the darkness.")
             print(f"{nar} The trap sets off a fire...")
             print("")
             input("--PRESS ANY KEY--")
             subprocess.run('cls', shell=True)

             print("☠︎︎.Game: You got incinirated alive by the fire.☠︎︎")
             playsound.playsound('ADVENTUREOTOPIA/Audio/maleScream.mp3')
             print("")
             GameEnd()
             time.sleep(3)

       else:
          print("")
          print(f"{nar} You didn't take the sword, bcause it looked shady and you wanted to proceed on your journey tommorow, so you slept..")
          print(f"{nar} In the morning you wake up in the morning and find yourself on the clouds..")
          print("☠︎︎.Game: A ghost took over your body and you died!.☠︎︎") 
          print("")
          input("--PRESS ANY KEY--")
          subprocess.run('cls', shell=True)

          GameEnd()
          time.sleep(2.5)

       #-------- 
       
   #----ROAD 2----
    elif road_choice1 == 2:
       print("")
       print(f"{mman} You have chosen Road 2, wise choice {User}.")
       time.sleep(2)
       print(f"{mman} I will see you soon. Goodluck and goodbye.")
       print("")
       input("--PRESS ANY KEY--")
       subprocess.run("cls", shell=True)
       time.sleep(0.5)
       print(f"{nar} You walk down the road, looking back at the man as he slowly becomes less visible.")
       print("")
       time.sleep(2)
       print(f"{nar} As you look back forward you see rubble of a castle.")
       print("")
       time.sleep(2)
       head_forward_question1 = input("Do you continue to the castle or turn back? Type Y to go forward and N to turn back. ")
       while head_forward_question1 == '': 
         head_forward_question1 = input("Do you continue to the castle or turn back? Type Y to go forward and N to turn back. ")
       if head_forward_question1 == "Y":
       
         #Entering castle

          subprocess.run("cls", shell=True)
          print(f"{nar} You head to the castle as nightfall approches, you head through the front door.")
          print("")
          time.sleep(1)
          print(f"{nar} The front door creeks open revealing a dusty, abandoned and ruined castle.")
          print("")
          time.sleep(2)
          print(f"{nar} You look around looking for anything useful.")
          print("")
          time.sleep(1)
          print(f"{nar} You find a rusted blade! x 1")
          print(f"{nar} You find a rusted key! x 1")
          rusted_blade_owned = True
          rusted_key_owned = True
          print("")
          input("--PRESS ANY KEY--")
          
          #Choice

          subprocess.run("cls", shell=True)  
          print(f"{nar} You look around and see a staircase and a bottom floor.")
          go_up_stairs = input("Where do you go? Type Up or Down. ")
          if go_up_stairs == "Up":
             subprocess.run("cls", shell=True)
             print(f"{nar} You walk up the stairs as the floor boards creek under you.")
             print("")
             time.sleep(2)
             print(f"{nar} A floor board breaks under you! But you luckily save yourself just in time.")
             print("")
             time.sleep(1)
             #continue
             print(f"{nar} As you continue, bats swarm the broken floor.")#its because you did not set it back with the code # why does it stat with the red color?
          elif go_up_stairs == "Down":
             subprocess.run("cls", shell=True)
             print(f"{nar} You walk straight, avoiding the stairs")
             print("")
             time.sleep(1)
             print(f"{nar} You follow a long narrow hallway avoiding flying bats.")
             time.sleep(1)
             print("")
             print("You see a door that looks like it requires a key.")
             time.sleep(2)
             use_rusty_key_question = input("Do you use your key? Y/N. ")
             if use_rusty_key_question == "Y" and rusted_key_owned == True:
                print(f"{nar} You use the rusty key on the door and it clicks open.")
                print("")
                time.sleep(1)
                print(f"Rusty key - 1!")
                rusted_key_owned = False
                print("")
                time.sleep(2)
                subprocess.run("cls", shell=True)
                print(f"{nar} You continue through the door closing it behind you.")
                print("")
                time.sleep(1)
                print(f"{nar} You look around seeing an abandoned stage.")
                time.sleep(0.5)
                print(f"{nar} You hear footsteps.")
                print("")
                time.sleep(3)
                print(f"{nar} They are getting closer..")
                print("")
                time.sleep(2)
                print(f"{nar} It is very close!")
                print("")
                Choice_1 = input("What do you do? A = Draw sword. B = Run away (Type A or B):  ")
                if Choice_1 == "A":
                   print(f"{nar} You draw your rusty sword and scream..")
                   input("--PRESS ANY KEY--")
                   subprocess.run("cls", shell=True)
                   print(f"{User}: YOU WILL NOT SCARE ME! I AM POWERFUL!")
                   time.sleep(1) #hi fahad
                   print("")
                   print("The monster jumps!")
                   input("--PRESS ANY KEY TO CONTINUE!--")
                   print("")
                   print(f"{nar} You stab the monster in its eye with your sword! It dies")
                   print("")
                   time.sleep(1)
                   print(f"{nar} It dies and ends up vaporising into dust.")
                   time.sleep(1)
                   
                   subprocess.run("cls", shell=True)
                   print("")
                   print(f"{User}: What was that thing?")
                   print("")
                   time.sleep(1)
                   print("Your Rusty Sword has been damaged! 20%/100%")
                   time.sleep(1)
                   print(f"{nar} You continue forward.")
                   print("")
                   time.sleep(0.5)
                   input("--PRESS ANY KEY--")
                   print("")
                   subprocess.run("cls", shell=True)

                   print(f"{nar} You pace around wondering what do do.")
                   print("")
                   time.sleep(1)
                   print(f"{nar} You think of 2 things that you should do.")
                   print("")
                   Choice_2 = input("Do you search around (Y) or do you find a place to sleep (N): ")#kk
                   if Choice_2 == "Y":
                      subprocess.run("cls", shell=True)
                      print(f"{nar} You decide to walk around and you found something that may help you!")  # YES ITS WORKING niceeee when i get my pad thing ill make the music
                      time.sleep(1)
                      print("")
                      time.sleep(0.5)
                      print("YOU HAVE FOUND:")
                      time.sleep(0.5)
                      print("1x Trap Door")
                      time.sleep(0.5)
                      print("1x Detachable Lever")
                      time.sleep(0.5)
                      found_trap_door = True
                      found_detachable_lever = True
                   if Choice_2 == "N":
                      subprocess.run("cls", shell=True)
                      print(f"{nar} You find a place to lay down and you fall through the floor!")
                      time.sleep(1)
                      print("")
                      print(f"{nar} You save yourself and walk around a dark cave")
                      print("")
                      time.sleep(1)
                      print(f"{nar} You find a glowing orb..")
                   else:
                      print(f"{nar} You spend hours trying to decide what to do and end up dying!")
                      time.sleep(1)
                      GameEnd()
                   

                  # 


                elif Choice_1 == "B":
                   print(f"The monster runs up to you and jumps ontop of you")
                   input("--PRESS ANY KEY--")
                   subprocess.run("cls", shell=True)
                   GameEnd()
                else:
                   subprocess.run("cls", shell=True)
                   print(f"{nar} The creature jumps ontop of you and rips you apart!")
                   time.sleep(1)
                   GameEnd()
               

                

               
             elif use_rusty_key_question == "N":
                print(f"{nar} You continue down the hallway as the bats get closer to your head.")
                print("")
                time.sleep(1)
                print(f"{nar} One bat swoops at you grasping on")
             else:
                pass
          else:
             subprocess.run("cls", shell=True)
             print(f"{nar} You wait for hours not finding a decision.")
             print(f"")
             time.sleep(1)
             print(f"{nar} You end up falling asleep and dying of starvation.☠︎")
             time.sleep(2)
             GameEnd()

       elif head_forward_question1 == "N":
          print("You walk back into the forest. but something bites your ankle.")
          time.sleep(1.5)
          print("Your vision blurs and your movement slows, you see the man just before death.")
          time.sleep(1)
          print(f"{mman} There is no turning back, keep moving.") # this is miserable death we don't need to add something in the function kk
          time.sleep(1)
          input("--PRESS ANY KEY--")
          subprocess.run("cls", shell=True)
          GameEnd()
          time.sleep(5)
       else: # End the game to make user rage if they think they're smart and press something else
          print("You think you're smart??")
          print("")
          input("--PRESS ANY KEY--")
          subprocess.run('cls', shell=True)
          GameEnd()
          time.sleep(5)
   #--------
             
   #----ROAD 3----
    elif road_choice1 == 3:
       pass
   #--------

   #----YOU DID NOT PICK A ROAD!----
    else:
       print("")
      # Work on a miserable DEATH if they don't pick a road DONE
       Not_Chosen_Path()
       print(f"{nar} You ignored the road and started walking out of the forest but on the way...")
       print("You tripped...")
       print("Hit a rock...")
       print("")
       # we have to make the user look like at this point they have some chance to survive but they're going to die anyway
       death_Scenario = input("You are seriously bleeding give up? Y/N: ")
       if death_Scenario == 'Y':
          print("☠︎︎.Game: You flew peacefully to heaven.☠︎︎")# hello
          print("")
          input("--PRESS ANY KEY--")
          print("")
          GameEnd()
          time.sleep(5)
       else:
          print(f"{nar} As you were crawling through the ground seeking help...")
          print("Bunch of animals came running and squished you to death!")
          print("☠︎︎.Game: It was a stampede.☠︎︎")
          print("")
          input("--PRESS ANY KEY--")
          print("")
          GameEnd()
          time.sleep(5)
   #--------

#----DON'T WANT TO PLAY GAME---- 
else:
    secret_end1 = input("Before quitting the game would you like to hear the secret message? Y/N: ")
    while secret_end1 == '':
       print("Not valid option")
       secret_end1 = input("Before quitting the game would you like to hear the secret message? Y/N: ")
    if secret_end1 == "Y": # does it work?
        print(secret_message)
        time.sleep(1)
        input("--PRESS ANY KEY--")
        quit()# just add brackets
        
    elif secret_end1 == "N":
       print("")
       GameEnd()
       time.sleep(5)
    
    else:
       print("")
       GameEnd()
       time.sleep(5)
#--------