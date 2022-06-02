class Student: 
     school="akirachix" 
     def __init__(self,firstname,secondname,age,country):
         self.firstname=firstname 
         self.secondname=secondname
         self.age=age  
         self.country=country 
      
         

     def greet(self):
         return f"Hello {self.firstname} welcome to {self.school} you are from{self.country}" 
     def fullname(self):
         name=f"{self.firstname} {self.secondname}"
         return name 
     def year_of_birth(self):
         yob=2022-self.age 
         return yob 
     def initials(self):
         x=f"{self.firstname[0]}{self.secondname[0]}" 
         y=x.upper() 

         return y          




     

        #  Add these methods to class student - full_name, year_of_birth
        #  , initials. Create two instances and verify the work as expected 
        