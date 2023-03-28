def suhu(name,celc,):
    print("Hii"+" "+str(name)+" "+"this is the temperature in fahrenheit" +" "+ str(fahrenheit))

    if fahrenheit >150:

        print(f"cuaca amat panas {fahrenheit}")
    else:
        print(f"Cuaca bagus di luar iaitu {fahrenheit} boleh main ")
            

name = input("Dear user, please enter your name:")
celc = float (input ( "What is your temperature in celcius?\n"))
fahrenheit = ((celc*1.8)+32)


suhu(name,celc,)




