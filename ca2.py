class Times:
    def __init__(self,hour,min):
        self.hour=hour
        self.min=min

    def add(t1,t2):
        t3 = Times(0, 0) 
        t3.hour = t1.hour + t2.hour
        t3.min = t1.min + t2.min
        while t3.min >= 60:
            t3.hour = t3.hour+1
            t3.min = t3.min-60
        return t3
    
    def show(self):
        print ("Time is",self.hour,"hours and",self.min,"minutes.")
        

obj = Times(6,30)
obj1 = Times(4,14)
sumy = Times.add(obj,obj1)
sumy.show()
obj2 = Times(2,55)
obj3 = Times(3,23)
sumj = Times.add(obj2,obj3)
sumj.show()

