import random
from FUN import TeamA
from FUN import GameA
from FUN import GameB
from FUN import TeamB
from FUN import Chennai
from FUN import Mumbai
from FUN import Rajasthan
from FUN import Kolkata
from FUN import Kandy
from FUN import Uthura
from FUN import Uva
from FUN import Wayamba
from FUN import flipCoin
from FUN import Bat_Ball
from FUN import Best_bats_mans
from FUN import Best_bowelrs
import time
with  open("Bats man score.txt", 'a+') as F:
    F.truncate(0)
with  open("Bowlers Wickets.txt", 'a+') as E:
    E.truncate(0)

print("WELCOME TO THE CRICKET WARRIORS ")
time.sleep(3)
print("LETS START THE GAME")
time.sleep(2)
print("SELECT A FOLLOWING OPTION")
Edit=1
Delete=2
Edit_delete=int(input("PRESS 1 TO START THE MATCH\nPRESS 2 TO EDIT\DELETE"))

if Edit_delete==2 :# can apply or

      A = open("Group A.txt", 'r')
      B = open("Group B.txt", 'r')
      print(A.read(),B.read())
      while True:
          Team=input("THESE ARE THE AVAILABLE TEAMS WHICH TEAM YOU WANT TO EDIT?\n ENTER THE FIRST NAME OF THE TEAM")
          if Team=="Chennai":
              Chennai()
              break

          elif Team=="Mumbai":
              Mumbai()
              break

          elif Team == "Rajasthan":
              Rajasthan()
              break

          elif Team == "Kolkata":
              Kolkata()
              break

          elif Team == "Kandy":
              Kandy()
              break

          elif Team == "Uthura":
              Uthura()
              break

          elif Team == "Uva":
              Uva()
              break

          elif Team == "Wayamba":
             Wayamba()
             break
          try:

              if Team!="Chennai"or Team!="" or Team!="Mumbai" or Team!="Rajasthan" or Team!="Kolkata" or Team!="Kandy" or Team!="Uthura" or Team!="Uva" or Team!="Wayamba":
                  print("OOPS THERE IS NO SUCH A TEAM PLEASE ENTER CORRECTLY")
                  print("ENTER AGAIN")
          except:
              pass
else:
 print("LET'S BEGIN THE GAME !!!")



Gruop=input("WHICH GROUP DO YOU WANT TO PLAY THE GAME FROM?? (A OR B)??")

if Gruop=="A":
    Matches = [["Chennai super Kings", "Mumbai indians"], ["Chennai super Kings", "Rajasthan Royal"],
               ["Chennai super Kings", "Kolkata knight riders"],
               ["Mumbai indians", "Rajasthan Royal"], ["Mumbai indians", "Kolkata knight riders"],
               ["Rajasthan Royal", "Kolkata knight riders"]]
    for matches in range(0, 6):
        Selected_Match = random.choice(Matches)
        print(Selected_Match)
        Matches.remove(Selected_Match)

        First_Team = Selected_Match[0]
        Second_Team = Selected_Match[1]

        print(f" MATCH IS {First_Team} VS {Second_Team}")
        Team = random.choice([First_Team, Second_Team])
        print(f"{Team} FLIPS THE COIN")
        print(flipCoin())
        BnB = Bat_Ball()
        print(BnB)
        print("GAME STARTS!!!")
        if (BnB == "Ball" and Team == First_Team) or (BnB == "Bat" and Team == Second_Team):
            temp = First_Team
            First_Team = Second_Team
            Second_Team = temp
            First_Team_Players = TeamA(Second_Team)
            Second_Team_Players = TeamA(First_Team)
            GameA(First_Team, Second_Team, First_Team_Players, Second_Team_Players)
        else:
            First_Team_Players = TeamA(First_Team)
            Second_Team_Players = TeamA(Second_Team)
            GameA(First_Team, Second_Team, First_Team_Players, Second_Team_Players)
    Best_bats_mans()
    Best_bowelrs()



elif Gruop=="B":
    B = ["Kandy Tuskers", "Uthura rudras", "Uva Next", "Wayamba United"]
    Matches = [["Kandy tuskers", "Uthura Riders"], ["Kandy tuskers", "Uva next"], ["Kandy tuskers", "Wayamba United"],
               ["Uthura Riders", "Uva next"], ["Uthura Riders", "Wayamba United"], ["Uva next", "Wayamba United"]]
    for matches in range(0, 6):
        Selected_Match = random.choice(Matches)
        print(Selected_Match)
        Matches.remove(Selected_Match)

        First_Team = Selected_Match[0]
        Second_Team = Selected_Match[1]



        print(f" FIRST MATCH IS {First_Team} VS {Second_Team}")
        Team = random.choice([First_Team, Second_Team])
        print(f"{Team} FLIPS THE COIN")
        print(flipCoin())  # always win the toss
        BnB = Bat_Ball()
        print(BnB)
        print("GAME STARTS!!!")
        if (BnB == "Ball" and Team == First_Team) or (BnB == "Bat" and Team == Second_Team):
            temp = First_Team
            First_Team = Second_Team
            Second_Team = temp
            First_Team_Players = TeamB(Second_Team)
            Second_Team_Players = TeamB(First_Team)
            GameB(First_Team, Second_Team, First_Team_Players, Second_Team_Players)
        else:
            First_Team_Players = TeamB(First_Team)
            Second_Team_Players = TeamB(Second_Team)
            GameB(First_Team, Second_Team, First_Team_Players, Second_Team_Players)
    Best_bats_mans()
    Best_bowelrs()





