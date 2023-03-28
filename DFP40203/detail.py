






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

        

        



  
    