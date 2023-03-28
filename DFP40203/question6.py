height = int(input("Enter the number of rows: "))  
  
# the outer loop is executing in reversed order  
#for i in range(height + 1, 0, -1):    
#    for j in range(0, i - 1):  
 #       print("*", end=' ')  
 #   print(" ")  


for i in range(height,0,-1):
    print('*'*i)