number_in_seconds = int(input('\nPlease enter the number in seconds :'))


number_in_minutes = number_in_seconds // 60
remainder_in_seconds = number_in_seconds % 60

print("The number of seconds for"+" "+str(number_in_seconds)+" "+"seconds is"+" "+str(number_in_minutes) +" "+ " minute and " + str(remainder_in_seconds) +"seconds")