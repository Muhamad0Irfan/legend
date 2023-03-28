password = 'irfan123'
max_attempt = 5
i = 0

while i < max_attempt:
    guess = input('Please enter the password: ')
    i = i+1
    if guess == password:
        print('You are logged in to the system')
        break
else:
    print('You are blocked from the system')        
