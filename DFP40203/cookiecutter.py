class CookieCutter:

 def __init__(self,shape):
  self.shape = shape
    

 def cut_cookie(self):
   print(f"A {self.shape}-shaped cookie has been cut!")
 
   


circle_cutter = CookieCutter("circle")

octagon_cutter = CookieCutter("octagon")

triangle_cutter = CookieCutter("triangle")

circle_cutter.cut_cookie()   

octagon_cutter.cut_cookie()

triangle_cutter.cut_cookie()