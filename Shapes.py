class Circle:
    def __init__(self,radius):
        self.radius=radius 
    def area(self):
        pie=3.14 
        circle_area=pie*self.radius**2 
        print(circle_area)  

    def circumference(self):
        pie=3.14
        c=2*pie*self.radius 
        print(c)  


class Square:
    def __init__(self,side_a):
        self.side_a=side_a 

    def area(self):
        Square_area=self.side_a**2 
        print(Square_area) 

    def perimeter(self):
        Square_perimeter=4*self.side_a 
        print(Square_perimeter)  



class Rectangle:
    def __init__(self,width,length):
        self.width=width 
        self.length=length 
    def rectangle_area(self):
        area=self.width*self.length 
        print(area)

    def perimeter(self):
        perimeter=2(self.width+self.length)
        print(perimeter) 



class Sphere:
    def __init__(self,radius):
        self.radius=radius

    def surfaceArea(self): 
        pie=3.14
        s_area=4*pie*self.radius**2 
        print(s_area)

    def volume(self):
        pie=3.14 
        v_sphere=4/3(pie*self.radius**3)
        print(v_sphere)    
               





     













