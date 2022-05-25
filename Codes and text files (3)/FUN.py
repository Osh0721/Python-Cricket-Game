# Teams and players Details
import random
A=["Chennai super Kings" , "Mumbai insians" ,"Rajasthan Royal" ,"Kolkata knigh riders"]
with open("Group A.txt",'w') as a:
    for ele in A:
        a.write(ele +"\n")

B=["Kandy Tuskers" ,"Uthura rudras" ,"Uva Next", "Wayamba United"]
with open("Group B.txt",'w') as a:
    for ele in B:
        a.write(ele+"\n")

Chennai=["Dhonni" ,"Raina" ,"bravo", "ambani" ,"ali" ,"robin", "deepak","asif" ,"Lungi" ,"karn", "dominic"]
with open("Chennai super Kings.txt",'w') as a:
    for ele in Chennai:
        a.write(ele+"\n")


Mumbai=["rohit", "yadav", "pandya", "pollard", "krunal ", "brumra","tren" ,"adam", "chris" , "chwla" ,"gayat"]

with open("Mumbai indians.txt",'w') as a:
    for ele in Mumbai:
        a.write(ele+"\n")

Rajasthan=["Liam", "manan" ,"gopal", "morris" ,"Mahipal" ,"Andrew","oshen","jaydev" ,"Chetan"  ,"Rahman", "archer"]

with open("Rajasthan Royal.txt",'w') as a:
    for ele in Rajasthan:
        a.write(ele+"\n")

Kolkata=["Morgan" ,"Russell", " Shakib" ,"Sunil",  "Shubman", "venkatesh", "Varun","Lockie","Tim","Harbhajan","krishna"]
with open("Kolkata Knight riders.txt",'w') as a:
    for ele in Kolkata :
        a.write(ele+"\n")

Kandy=["Oshan", "Bhathiya", "Pandula", "Isitha", "Aluwa" ,"lahiru","Uditha" ,"hasindu" ,"Wishawa" ,"Janitha", "Charitha"]
with open("Kandy tuskers.txt", 'w') as a:
    for ele in Kandy:
        a.write(ele+"\n")

Uthura=["pasindu" ,"denidu" ,"Thisanka" ,"sanga", "mahela", "sanath","chamika" ,"malinga" ,"hasaranga", "abekoon"]

with open("Uthura Riders.txt", 'w') as a:
    for ele in Uthura:
        a.write(ele+"\n")

Uva=["Theshan", "Deshapriya", "Thiwanka", "Iresh" ,"anuka", "buddika","manuka" ,"ginuka" ,"nimal", "kamal" ,"theminida"]

with open("Uva next.txt", 'w') as a:
    for ele in Uva:
        a.write(ele+"\n")

Wayamba=["kumara" ,"ajith" ,"lasantha", "ayantha" ,"nuwan", "asiri","rahal", "jainth" ,"chamindu", "janaka" ,"sathila"]

with open("Wayamba United.txt", 'w') as a:
    for ele in Wayamba:
        a.write(ele+"\n")



#Edit and Delete Function
def Chennai():

    Chennai = open("Chennai super Kings.txt", 'r')

    print(Chennai.read())
    print("THESE ARE THE PLAYERS")
    print()
    with open("Chennai super Kings.txt", "r") as f:
        players = f.readlines()
        X=input("ENTER THE NAME OF THE PLAYER TO DELETE")

    with open("Chennai super Kings.txt", "w") as f:
        for line in players:
            if line.strip("\n") != (X) :
                f.write(line)
    Chennai = open("Chennai super Kings.txt", 'a+')
    New_player = input("ENTER THE NEW PLAYER NAME ")
    Chennai.write(New_player)
    print("LET'S GO TO THE GAME!!!!")


def Mumbai():
    Mumbai = open("Mumbai indians.txt", 'r')
    print(Mumbai.read())
    print("THESE ARE THE PLAYERSs")
    print()
    with open("Mumbai indians.txt", "r") as f:
        players = f.readlines()
        X=input("ENTER THE NAME OF THE PLAYER TO DELETE")
    with open("Mumbai indians.txt", "w") as f:
        for line in players:
            if line.strip("\n") != (X) :
                f.write(line)
    # delete players
    Mumbai = open("Mumbai indians.txt", 'a+')
    New_player = input("ENTER THE NEW PLAYER NAME ")

    Mumbai.write(New_player)
    print("LET'S GO TO THE GAME!!!!")


def Rajasthan():
    Rajasthan = open("Rajasathan Royals.txt", 'r')
    print(Rajasthan.read())
    print("THESE ARE THE PLAYERS")
    print()
    with open("Rajasathan Royals.txt", "r") as f:
        players = f.readlines()
        X=input("ENTER THE NAME OF THE PLAYER TO DELETE")
    with open("Rajasathan Royals.txt", "w") as f:
        for line in players:
            if line.strip("\n") != (X) :
                f.write(line)
    # delete players
    Rajasthan = open("Rajasathan Royals.txt", 'a+')
    New_player = input("ENTER THE NEW PLAYER NAME ")
    Rajasthan.write(New_player)
    print("LET'S GO TO THE GAME!!!!")

def Kolkata():
    Kolkata = open("Kolkata Knight riders.txt", 'r')
    print(Kolkata.read())
    print("THESE ARE THE PLAYERS")
    print()
    with open("Kolkata Knight riders.txt", "r") as f:
        players = f.readlines()
        X=input("ENTER THE NAME OF THE PLAYER TO DELETE")

    with open("Kolkata Knight riders.txt", "w") as f:
        for line in players:
            if line.strip("\n") != (X) :
                f.write(line)
    # delete players
    Kolkata = open("Kolkata Knight riders.txt", 'a+')
    New_player = input("ENTER THE NEW PLAYER NAME ")
    Kolkata.write(New_player)
    print("LET'S GO TO THE GAME!!!!")

def Kandy():

    Kandy = open("Kandy tuskers.txt", 'r')
    print(Kandy.read())
    print("THESE ARE THE PLAYERS")
    print()
    with open("Kandy tuskers.txt", "r") as f:
        players = f.readlines()
        X=input("ENTER THE NAME OF THE PLAYER TO DELETE")
    with open("Kandy tuskers.txt", "w") as f:
        for line in players:
            if line.strip("\n") != (X) :
                f.write(line)
    # delete players
    Kandy = open("Kandy tuskers.txt", 'a+')
    New_player = input("ENTER THE NEW PLAYER NAME ")
    Kandy.write(New_player)
    print("LET'S GO TO THE GAME!!!!")


def Uthura():
    Uthura = open("Uthura Riders.txt", 'r')
    print(Uthura.read())
    print("THESE ARE THE PLAYERS")
    print()
    with open("Uthura Riders.txt", "r") as f:
        players = f.readlines()
        X=input("ENTER THE NAME OF THE PLAYER TO DELETE")
    with open("Uthura Riders.txt", "w") as f:
        for line in players:
            if line.strip("\n") != (X) :
                f.write(line)
    # delete players
    Uthura = open("Uthura Riders.txt", 'a+')
    New_player = input("ENTER THE NEW PLAYER NAME ")
    Uthura.write(New_player)
    print("LET'S GO TO THE GAME!!!!")


def Uva():
    Uva = open("Uva next.txt", 'r')
    print(Uva.read())
    print("THESE ARE THE PLAYERS")
    print()
    with open("Uva next.txt", "r") as f:
        players = f.readlines()
        X=input("ENTER THE NAME OF THE PLAYER TO DELETE")
    with open("Uva next.txt", "w") as f:
        for line in players:
            if line.strip("\n") != (X) :
                f.write(line)
    # delete players
    Uva = open("Uva next.txt", 'a+')
    New_player = input("ENTER THE NEW PLAYER NAME ")
    Uva.write(New_player )
    print("LET'S GO TO THE GAME!!!!")

def Wayamba():
    Wayamba = open("Wayamba United.txt", 'r')
    print(Wayamba.read())
    print("THESE ARE THE PLAYERS")
    print()
    with open("Wayamba United.txt", "r") as f:
        players = f.readlines()
        X=input("ENTER THE NAME OF THE PLAYER TO DELETE")
    with open("Wayamba United.txt", "w") as f:

        for line in players:
            if line.strip("\n") != (X) :
                f.write(line)
    # delete players
    Wayamba = open("Wayamba United.txt", 'a+')
    New_player = input("ENTER THE NEW PLAYER NAME ")
    Wayamba.write(New_player )
    print("LET'S GO TO THE GAME!!!!")

# Toss and coin
def flipCoin():
    return random.choice(["Head", "Tail"])


def Bat_Ball():
    return random.choice(["Bat", "Ball"])


#Game flow for Team A
def TeamA(Team_Name):
    if Team_Name == "Mumbai indians":
        file = open("Mumbai indians.txt", "r")
        file_lines=file.read()
        Players = file_lines.split()

    elif Team_Name == "Chennai super Kings":
        Players = ["Dhonni", "Raina", "bravo", "ambani", "ali", "robin", "deepak","asif", "Lungi", "karn", "dominic"]
        file = open("Chennai super Kings.txt", "r")
        file_lines = file.read()
        Players = file_lines.split()


    elif Team_Name == "Rajasthan Royal":
        Players = ["Liam", "manan", "gopal", "morris", "Mahipal", "Andrew","oshen", "jaydev", "Chetan", "Rahman", "archer"]
        file = open("Rajasthan Royal.txt", "r")
        file_lines = file.read()
        Players = file_lines.split()


    elif Team_Name == "Kolkata knight riders":
        Players = ["Morgan", "Russell", "Shakib" ,"Sunil", "Shubman", "venkatesh", "Varun", "Lockie", "Tim","Harbhajan", "krishna"]
        file = open("Kolkata knight riders.txt", "r")
        file_lines = file.read()
        Players = file_lines.split()

    else:
        Players=[]
    return Players


def GameA(First_Team,Second_Team,First_Team_Players,Second_Team_Players):

    First_Team_Players = TeamA(First_Team)
    Second_Team_Players = TeamA(Second_Team)

    players1=First_Team_Players
    Wicket_ballers1={}

    Overs=1
    Wicket=0
    Tot1=0
    Tot_bat_score = 0
    player_position=0
    player=players1[0]
    print(player)
    Batsman_scores1={}

    while Overs<20 and Wicket<10:

      for Y in range (0,6):
          if Wicket >= 10:
              break
          Ball=random.randint(0,6)
          if Ball==0:

           Out = random.choice(["LBW !", "Catch Out !", "Wicket !", "Run Out !"])
           print("Hard Luck",Out)
           Batsman_scores1[player]=Tot_bat_score
           print("His Total score is :",Tot_bat_score)

           if Wicket<9:
               player_position+=1
               player = players1[player_position]
               print(player)
               Tot_bat_score = 0
               print("\n")
           Wicket += 1

          else:
           print("For this ball he got", Ball)
          Tot1 += Ball

          Tot_bat_score+=Ball

      Overs += 1




    print("FIRST INNIGS IS OVER")
    print(f"THE TOTAL TEAM SCORE IS {Tot1}")
    print("TOTAL OVER IS",Overs)
    print("TOTAL WICKETS IS",Wicket)


    Ava_Wicket=Wicket
    for B in Second_Team_Players:
        current_Wicket=random.randint(0,Wicket)
        if current_Wicket<Ava_Wicket:
            Wicket_ballers1[B]=current_Wicket
            Ava_Wicket-=current_Wicket
        else:
            Wicket_ballers1[B]=Ava_Wicket
            Ava_Wicket=0

    print(Wicket_ballers1)
    print()
    print("-----------------------------------------------------------------------------")
    print("LET'S BEGIN THE 2 INNINGS")
    players2 = Second_Team_Players
    Wicket_ballers2={}
    Overs=1
    Wicket=0
    Tot2=0
    Tot_bat_score = 0
    player_position=0
    player=players2[0]
    Batsman_scores2={}

    while Overs<20 and Wicket<10:
      score = 0
      for Y in range (0,6):
          if Wicket >= 10:
              break
          Ball=random.randint(0,6)
          if Ball==0:
           score=0
           Out = random.choice(["LBW !", "Catch Out !", "Wicket !", "Run Out !"])
           print("Hard Luck",Out)

           Batsman_scores2[player]=Tot_bat_score
           print("His Total score is :",Tot_bat_score)
           if Wicket<9:
               player_position+=1
               player = players2[player_position]
               print(player)
               Tot_bat_score = 0
               print("\n")
           Wicket += 1

          else:
           print("For this ball he got", Ball)
          score += Ball
          Tot2 += Ball

          Tot_bat_score+=Ball

      Overs += 1

    print("MATCH IS OVER")
    print(f"THE TOTAL TEAM SCORE IS {Tot2}")
    print("TOTAL OVER IS", Overs)
    print("TOTAL WICKETS IS", Wicket)

    with  open("Bats man score.txt", 'r') as File:
        data = File.readlines()
        if data == []:
            with  open("Bats man score.txt", 'a+') as F:
                for key, X in Batsman_scores1.items():
                    F.write(key + "--" + str(X) + "\n")
        else:
            temp_batsman = []

            for p in Batsman_scores1:
                for x in data:
                    if x.startswith(p):
                        split = x.split("--")
                        split[1] = split[1].strip("\n")
                        File_Score = int(split[1])

                        Dic_Score = Batsman_scores1[p]

                        file_tot = Dic_Score + File_Score
                        index = data.index(x)
                        data[index] = split[0] + "--" + str(file_tot) + "\n"
                        temp_batsman.append(p)

            for key, v in Batsman_scores1.items():
                if key not in temp_batsman:
                    data.append(key + "--" + str(v) + "\n")

            with  open("Bats man score.txt", 'w') as File:
                File.writelines(data)


    Ava_Wicket=Wicket
    for B in First_Team_Players:
        current_Wicket=random.randint(0,Wicket)
        if current_Wicket<Ava_Wicket:
            Wicket_ballers2[B]=current_Wicket
            Ava_Wicket-=current_Wicket
        else:
            Wicket_ballers2[B]=Ava_Wicket
            Ava_Wicket=0

    Wicket_ballers1.update(Wicket_ballers2)
    with  open("Bowlers Wickets.txt", 'r') as File:
        data = File.readlines()
        if data == []:
            with  open("Bowlers Wickets.txt", 'a+') as F:
                for key, X in Wicket_ballers1.items():
                    F.write(key + "--" + str(X) + "\n")
        else:
          temp_Bowlers = []

          for p in Wicket_ballers1:
                for x in data:
                    if x.startswith(p):
                        split = x.split("--")
                        split[1] = split[1].strip("\n")
                        File_Score = int(split[1])
                        Dic_Score = Wicket_ballers1[p]

                        file_tot = Dic_Score + File_Score
                        index = data.index(x)
                        data[index] = split[0] + "--" + str(file_tot) + "\n"
                        temp_Bowlers.append(p)

          for key, v in Wicket_ballers1.items():
                if key not in temp_Bowlers:
                    data.append(key + "--" + str(v) + "\n")

          with  open("Bowlers Wickets.txt", 'w') as File:
                File.writelines(data)




    if Tot1>Tot2:
     print(First_Team,"Won !!!")
    else:
     print(Second_Team,"Won !!!")



#Game flow for team B
def TeamB(Team_Name):
    if Team_Name == "Kandy tuskers":
        file = open("Kandy tuskers.txt", "r")
        file_lines = file.read()
        Players = file_lines.split("\n")


    elif Team_Name == "Uthura Riders":

        file = open("Uthura Riders.txt", "r")
        file_lines = file.read()
        Players = file_lines.split("\n")



    elif Team_Name == "Uva next":

        file = open("Uva next.txt", "r")
        file_lines = file.read()
        Players = file_lines.split("\n")



    elif Team_Name == "Wayamba United":

        file = open("Wayamba United.txt", "r")
        file_lines = file.read()
        Players = file_lines.split("\n")


    else:
        Players=[]
    return Players

def GameB(First_Team,Second_Team,First_Team_Players,Second_Team_Players):

    First_Team_Players = TeamB(First_Team)
    Second_Team_Players = TeamB(Second_Team)

    players1=First_Team_Players

    Wicket_ballers1={}

    Overs=1
    Wicket=0
    Tot1=0
    Tot_bat_score = 0
    player_position=0
    player=players1[0]
    print(player)
    Batsman_scores1={}

    while Overs<20 and Wicket<10:

      score = 0
      for Y in range (0,6):
          if Wicket >= 10:
              break
          Ball=random.randint(0,6)
          if Ball==0:
           score=0
           Out = random.choice(["LBW !", "Catch Out !", "Wicket !", "Run Out !"])
           print("Hard Luck",Out)
           Batsman_scores1[player]=Tot_bat_score
           print("His Total score is :",Tot_bat_score)
           if Wicket<9:
               player_position+=1
               player = players1[player_position]
               print(player)
               Tot_bat_score = 0
               print("\n")
           Wicket += 1

          else:
           print("For this ball he got", Ball)
          score += Ball
          Tot1 += Ball

          Tot_bat_score+=Ball

      Overs += 1
    print("Match is over")
    print(f"The Total score is {Tot1}")
    print("Total over is",Overs)
    print("Total wickets is",Wicket)

    print(Wicket)
    Ava_Wicket=Wicket
    for B in Second_Team_Players:
        current_Wicket=random.randint(0,Wicket)
        if current_Wicket<Ava_Wicket:
            Wicket_ballers1[B]=current_Wicket
            Ava_Wicket-=current_Wicket
        else:
            Wicket_ballers1[B]=Ava_Wicket
            Ava_Wicket=0

    print(Wicket_ballers1)
    print()
    print("-----------------------------------------------------------------------------")


    print("Lets begin the 2nd Innings")
    players2 = Second_Team_Players
    Wicket_ballers2={}
    Overs=1
    Wicket=0
    Tot2=0
    Tot_bat_score = 0
    player_position=0
    player=players2[0]
    print(player)
    Batsman_scores2={}

    while Overs<20 and Wicket<10:

      for Y in range (0,6):
          if Wicket >= 10:
              break
          Ball=random.randint(0,6)
          if Ball==0:

           Out = random.choice(["LBW !", "Catch Out !", "Wicket !", "Run Out !"])
           print("Hard Luck",Out)

           Batsman_scores2[player]=Tot_bat_score


           print("His Total score is :",Tot_bat_score)
           if Wicket<9:
               player_position+=1
               player = players2[player_position]
               print(player)
               Tot_bat_score = 0
               print("\n")
           Wicket += 1

          else:
           print("For this ball he got", Ball)
          #score += Ball
          Tot2 += Ball

          Tot_bat_score+=Ball

      Overs += 1

    print("Match is over")
    print(f"The Total score is {Tot2}")
    print("Total over is",Overs)
    print("Total wickets is",Wicket)


    Batsman_scores1.update(Batsman_scores2)


    with  open("Bats man score.txt", 'r') as File:
        data = File.readlines()
        if data == []:
            with  open("Bats man score.txt", 'a+') as F:
                for key, X in Batsman_scores1.items():
                    F.write(key + "--" + str(X) + "\n")
        else:
            temp_batsman = []

            for p in Batsman_scores1:
                for x in data:
                    if x.startswith(p):
                        split = x.split("--")
                        split[1] = split[1].strip("\n")
                        File_Score = int(split[1])

                        Dic_Score = Batsman_scores1[p]

                        file_tot = Dic_Score + File_Score
                        index = data.index(x)
                        data[index] = split[0] + "--" + str(file_tot) + "\n"
                        temp_batsman.append(p)

            for key, v in Batsman_scores1.items():
                if key not in temp_batsman:
                    data.append(key + "--" + str(v) + "\n")

            with  open("Bats man score.txt", 'w') as File:
                File.writelines(data)

    Ava_Wicket=Wicket
    for B in First_Team_Players:
        current_Wicket=random.randint(0,Wicket)
        if current_Wicket<Ava_Wicket:
            Wicket_ballers2[B]=current_Wicket
            Ava_Wicket-=current_Wicket
        else:
            Wicket_ballers2[B]=Ava_Wicket
            Ava_Wicket=0

    Wicket_ballers1.update(Wicket_ballers2)
    with  open("Bowlers Wickets.txt", 'r') as File:
        data = File.readlines()
        if data == []:
            with  open("Bowlers Wickets.txt", 'a+') as F:
                for key, X in Wicket_ballers1.items():
                    F.write(key + "--" + str(X) + "\n")
        else:
          temp_Bowlers = []

          for p in Wicket_ballers1:
                for x in data:
                    if x.startswith(p):
                        split = x.split("--")
                        split[1] = split[1].strip("\n")
                        File_Score = int(split[1])
                        Dic_Score = Wicket_ballers1[p]

                        file_tot = Dic_Score + File_Score
                        index = data.index(x)
                        data[index] = split[0] + "--" + str(file_tot) + "\n"
                        temp_Bowlers.append(p)

          for key, v in Wicket_ballers1.items():
                if key not in temp_Bowlers:
                    data.append(key + "--" + str(v) + "\n")

          with  open("Bowlers Wickets.txt", 'w') as File:
                File.writelines(data)



    if Tot1>Tot2:
     print(First_Team,"Won !!!")

    else:
     print(Second_Team,"Won !!!")


#Best bat man function
def Best_bats_mans():
    Best_bat_mans = {}
    F = open("Bats man score.txt", 'r')
    for line in F:
        X = line.split("--")
        X[1] = X[1].strip()
        Best_bat_mans[X[0]] = int(X[1])
    sort_orders = sorted(Best_bat_mans.items(), key=lambda x: x[1], reverse=True)
    print("\n")
    print("THESE ARE THE BEST 5 BATS MAN IN THIS ROUND")
    print(sort_orders[0], sort_orders[1], sort_orders[2], sort_orders[3], sort_orders[4])


#best bowler function
def Best_bowelrs():
    Best_Wickters = {}
    F = open("Bowlers Wickets.txt", 'r')
    for line in F:
        X = line.split("--")
        X[1] = X[1].strip("\n")
        Best_Wickters[X[0]] = int(X[1])
    sort_orders = sorted(Best_Wickters.items(), key=lambda x: x[1], reverse=True)
    print("\n")
    print("THESE ARE THE BEST 5 BOWLERS MAN IN THIS ROUND")
    print(sort_orders[0], sort_orders[1], sort_orders[2], sort_orders[3], sort_orders[4])



