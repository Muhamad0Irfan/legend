name = input ( "What is your name?\n")
marks = int (input ( "What is your marks in final exam?\n"))
grade = input ( "What is your grade?\n")
if marks >= 80 :
    print ("you are brilliant")

elif marks <= 60 :
    print ("better luck next time")
  

else :
    print ("refer spmp")

greeting = "Hi" +" "+ name +" "+ "your marks is" + str( marks ) + " your grade is " + str(grade)
print (greeting)
