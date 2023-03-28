class Animal:

 def __init__(food,choices,anti,leg):
  food.choices = choices
  food.anti = anti
  food.leg = leg
  
    

 def lion_food(food):
   print(f"A Lion is eating {food.choices} but lions do not eat {food.anti}")
 
 def chicken_food(food):
  print(f"A chicken is eating {food.choices} but chicken do not eat {food.anti}")  

 def animal_size(food):
  if food.leg > 2:
    print(f"this animal have {food.leg} leg and it can sleep by it's back")
  else:
    print(f"this animal have {food.leg} leg and it sleeps standing")
    
a = input("What is the food that lion eat?")
b = input("what is the food that lion do not eat?")
c = int (input("How many legs does lion have?"))

tiger_cub = Animal(a,b,c)

a2 = input("What is the food that chicken eat?")
b2 = input("what is the food that chicken do not eat?")
c2 = int (input("How many legs does chicken have?"))
 
corn = Animal(a2,b2,c2)

# tiger_cub = Animal("meat","bone",4)
# corn = Animal("corn","fork",2)

tiger_cub.lion_food()
tiger_cub.animal_size()

corn.chicken_food()
corn.animal_size()

