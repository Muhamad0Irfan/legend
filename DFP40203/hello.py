#muhamad irfan bin mohamad ikhwan
#0108208492
#muhamadirfanmohamadikhwan@gmail.com



name = input ( "What is your name?\n")
price = float (input ( "What is your price?\n"))
tax = float (input ( "what is you taxes price?\n"))
#sales amount = total sales + sales tax
salestax = (price * (tax/100))
tap = price + salestax
greeting = "Hi" +" "+ name +" "+ "total amount to pay is"+" " +str( tap ) + " the sales tax is " + str(tax)
print (greeting)