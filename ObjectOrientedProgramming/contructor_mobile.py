class Mobile():
    name:str
    price:int
    brand:str

    def __init__(self,name,price,brand):
        self.name=name
        self.price=price
        self.brand=brand

    def mobile_display(self):
        print(self.name,self.price,self.brand)


mobile_instance1=Mobile("GALAXY A35",25000,"SAMSUNG")



mobile_instance1.mobile_display()