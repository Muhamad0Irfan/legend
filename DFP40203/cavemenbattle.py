import random


print("*****************************")
print("Welcome to the cavemen battle")
print("*****************************")



#info registration
player1_name = input("Player 1, create your name :")


player2_name = input("Player 2, create your name :")

#set the initial health,ammo ,damage
player1_health  = 100
player1_ammo    = 50
player1_damage  = 50
player1_stamina = 100

player2_health  = 100
player2_ammo    = 100
player2_damage  = 25
player2_stamina = 100

print("\n" + player1_name +" "+ "has " + str(player1_health) + " health" + str(player1_ammo) + " rounds of ammo" + str(player1_damage) + " damage")
print("\n" + player2_name +" "+ "has " + str(player2_health) + " health" + str(player2_ammo) + " rounds of ammo" + str(player2_damage) + " damage")

print('\n Your cave suddenly is attacked by wild animals. What do you do?') 
print('1. Fight') 
print('2. Run') 
print('3. Search for supplies')

choice1 = int(input('player 1, Enter either 1,2 0r 3: ')) 
if choice1 == 1: 
    print("Shoot the animals")
    player1_ammo -= 10
    if player1_ammo > 0 :
        print('Animals is dead')

    print(str(player1_ammo) + 'ammo left')


elif choice1 == 2:
    print("Run for help")
    player1_stamina-= 20
    print(player1_ammo)


elif choice1 == 3:
    random_number = random.randint(1,10) 
    print(random_number) 
    if random_number > 5: 
        print("the manage to save some foods") 
    else: 
        print("they manage to ran away with their cloths")


else :
    print("Game over!!")


choice2 = int(input('Enter either 1,2 0r 3: ')) 
if choice2 == 1: 
    print("Shoot the animals")
    player2_ammo -= 10
    print(str(player2_ammo) + "ammo left")
 

elif choice2 == 2:
    print("run for help")
    player2_stamina-= 20
    print(player2_ammo)

elif choice2 == 3:
    print("Animals manage to chase you")        

else :
    print("Game over!!")    
    

    
    
print("Animal attacks on player 2")
player2_health -= 20
print(str(player2_health))

print("Animal attacks on player 1")
player1_health -= 20
print(str(player1_health))