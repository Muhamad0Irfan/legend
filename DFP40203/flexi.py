from prettytable import PrettyTable
x = PrettyTable()
z = PrettyTable()


RESET = "\033[0m"
BLACK = "\u001b[30m"
RED = "\u001b[31m"
GREEN = "\u001b[32m"
YELLOW = "\u001b[33m"
BLUE = "\u001b[34m"
MAGENTA = "\u001b[35m"
CYAN = "\u001b[36m"
WHITE = "\u001b[37m"

print(MAGENTA + "******************************************************************************************************************" + RESET)
print(CYAN + """ 
 __      __          ___                                          __               ____    ___                          ____    ___               __      __      
/\ \  __/\ \        /\_ \                                        /\ \__           /\  _`\ /\_ \                  __    /\  _`\ /\_ \   __        /\ \    /\ \__   
\ \ \/\ \ \ \     __\//\ \     ___    ___     ___ ___      __    \ \ ,_\   ___    \ \ \L\_\//\ \      __   __  _/\_\   \ \ \L\_\//\ \ /\_\     __\ \ \___\ \ ,_\  
 \ \ \ \ \ \ \  /'__`\\ \ \   /'___\ / __`\ /' __` __`\  /'__`\   \ \ \/  / __`\   \ \  _\/ \ \ \   /'__`\/\ \/'\/\ \   \ \  _\/ \ \ \\/\ \  /'_ `\ \  _ `\ \ \/  
  \ \ \_/ \_\ \/\  __/ \_\ \_/\ \__//\ \L\ \/\ \/\ \/\ \/\  __/    \ \ \_/\ \L\ \   \ \ \/   \_\ \_/\  __/\/>  </\ \ \   \ \ \/   \_\ \\ \ \/\ \L\ \ \ \ \ \ \ \_ 
   \ `\___x___/\ \____\/\____\ \____\ \____/\ \_\ \_\ \_\ \____\    \ \__\ \____/    \ \_\   /\____\ \____\/\_/\_\\ \_\   \ \_\   /\____\ \_\ \____ \ \_\ \_\ \__\
    '\/__//__/  \/____/\/____/\/____/\/___/  \/_/\/_/\/_/\/____/     \/__/\/___/      \/_/   \/____/\/____/\//\/_/ \/_/    \/_/   \/____/\/_/\/___L\ \/_/\/_/\/__/
                                                                                                                                               /\____/            
                                                                                                                                               \_/__/             
 """ + MAGENTA )
print(MAGENTA + "***************************************************************************************************************" + RESET)


x.field_names = ["ID", "From", "To", "Depart Time", "Adult Price", "Child Price"]
x.add_row([1, "Lawas", "Limbang", 6.30,40.00,30.00])
x.add_row([2, "Mukah", "Bakalalan", 7.30,28.00,13.00])
x.add_row([3, "Bintulu", "Kapit", 8.30,13.00,25.00])
x.add_row([4, "Kuching", "Sibu", 9.30,35.00,40.00])
x.add_row([5, "Miri", "Bintulu", 5.30,55.00,45.00])


print(x)


name = input("pls input ur name")
fromw = input("pls input where u from")
dest = input("pls input the destination")
noadult = input("pls input number of adult")
nochildren = input("pls input number of children")
ttlpayment = input("pls input number of children")

z.field_names = ["Name", "From", "To", "Number of Adult", "Number of Children", "Total Payment"]
z.add_row([name,fromw,dest,noadult,nochildren,ttlpayment])

print(z)
