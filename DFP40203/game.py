print("""

o-o   o   o o   o  o-o  o--o  o-o  o   o  o-o                  o-o   o--o    O   o-o   o-o  o   o  o-o  
|  \  |   | |\  | o     |    o   o |\  | |               o     |  \  |   |  / \ o     o   o |\  | |     
|   O |   | | \ | |  -o O-o  |   | | \ |  o-o           /|     |   O O-Oo  o---o|  -o |   | | \ |  o-o  
|  /  |   | |  \| o   | |    o   o |  \|     |         o-O-    |  /  |  \  |   |o   | o   o |  \|     | 
o-o    o-o  o   o  o-o  o--o  o-o  o   o o--o            |     o-o   o   o o   o o-o   o-o  o   o o--o  
                                                                                                        
                                                                                                        
 """)


print ('Welcome to Dungeons & Dragons')

player_name = input('What is your name, adventurer?\n')


dragon_damage = 50
health = 200
damage = 300
hit = health - dragon_damage

print('\nwelcome, ' + player_name + ' !you have ' + str(health) + ' health and can do damage ' + str(damage))


print('You came across a dragon!!!!! What will you do??')
print('1. Fight')
print('2. Run')

choice = int(input('Enter either 1 or 2: ')) 
if choice == 1: 
    print("Hit the Dragon")
    print("You hit the Dragon")
    print( "!!!!!"+" "+str(damage) +" "+"!!!!!") 

elif choice == 2:
    print("You hit by the Dragon")
    health -= dragon_damage
    print(health)
    print("You have low health") 

else :
    print("Game over!!")

print('The Dragon manage to fight u back')
health -= damage*2
print(health) 
