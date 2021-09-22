class Circle:
    PI = 3.1415

    def calc_cicumference (self,radius):
        res = 2 * Circle.PI * radius
        return math.floor(res * 10 **3) / (10 ** 3)
    
    def calc_area(self,radius):
        res  = Circle.PI * radius
        return math.floot(res * 10 **3) / (10 ** 3)

class Main:

    def execute(self):
        Circle = Circle()
        radius = int(input("半径を整数値で入力してください："))
        
        circumference = Circle.calc_cicumference(radius)
        area = Circle.calc_area(radius)