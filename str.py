class TireDimension:
    def __init__(self, TireDescription):
        self.TireDescription=TireDescription
        self.length=len(TireDescription)
    def fct(self):
        print(self.length) 

p1= TireDimension("360/75 R 28")
p1.fct()

