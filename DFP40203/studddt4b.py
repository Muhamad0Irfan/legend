
class player:

    def __init__(self,ign,rank,kill,totalmatches,totalwin):
         self.ign = ign
         self.rank = rank
         self.kill = kill
         self.totalmatches = totalmatches
         self.totalwin = totalwin


    def detail(self):
        print(f"id :{self.ign} Rank:{self.rank} kill:{self.kill} total matches:{self.totalmatches} total win:{self.totalwin}")    

        
class enemy:
   def __init__(self,ign,rank,kill,totalmatches,totalwin):
         self.ign = ign
         self.rank = rank
         self.kill = kill
         self.totalmatches = totalmatches
         self.totalwin = totalwin


   def detail(self):
        print(f"id :{self.ign} Rank:{self.rank} kill:{self.kill} total matches:{self.totalmatches} total win:{self.totalwin}") 

        
RESET = "\033[0m"
BLACK = "\u001b[30m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
MAGENTA = "\u001b[35m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37m"




print(BLACK + "***********************************" + RESET)
print(BLACK + "*********"+ RED + "WELCOME TO PUBG MOBIL" + BLACK +"*******" + RESET)
print(BLACK +  "***********************************" + RESET)


name = input(RED +"insert name:")
ranknow = (input(BLACK+"insert rank:"))
kill = (input(BLUE+"insert kill:"))
matchesplayed = (input(YELLOW+"insert matches played:"))
winpergame =  (input(MAGENTA+"insert win per game:"))


player1 = player(name,ranknow,kill,matchesplayed,winpergame)
enemy1 = enemy(name,ranknow,kill,matchesplayed,winpergame)





player1.detail()

enemy1.detail()












