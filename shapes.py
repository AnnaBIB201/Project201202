class Circle():
    def __init__(self,x,y,r,color,vx,vy):
        self.x = x
        self.y = y
        self.r = r
        self.color = color
        self.vx = vx
        self.vy = vy
    def peresechenie(self,other):
        if (self.x - other.x)**2 + (self.y - other.y)**2<=(self.r + other.r)**2:
            return True
        else:
            return False
class Rect():
    def __init__(self,x,y,w,h,color,vx,vy):
        self.x = x
        self.y = y
        self.w = w
        self.h = h
        self.color = color
        self.vx = vx
        self.vy = vy
