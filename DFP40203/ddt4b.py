

class Student:

    def __init__(self,name,age,weight,height):
         self.name = name
         
         self.age = age
         self.weight = weight
         self.height = height

    def Student_detail(self):
        print(f"My name is {self.name}. I am {self.age} years old. My weight is {self.weight}kg and my height is {self.height}cm.")



Ali = Student("Ali",20,60,171)


Ali.Student_detail()












  
   
