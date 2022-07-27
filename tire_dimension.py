from sys import setswitchinterval


class TireDimension:
    def __init__(self, TireDescription):
        self.TireDescription=TireDescription
        self.length=len(TireDescription)
        
        self.pos_1=self.TireDescription.find("/")           #find / position in string
        self.pos_2=self.TireDescription.find("R")           #find R position in string

        self.first_str=self.TireDescription[:self.pos_1]
        self.second_str=self.TireDescription[self.pos_1+1:self.pos_1+3]
        self.rim_string= self.TireDescription[self.pos_2+2:]
        self.status=1

        '''
        if self.status<0:
            x=1
        elif x==0:
            x=2
        else:
            x=3
        '''

        match self.status:
            case 1:     #  360/75 R 28
                 self.tire_SW=int(self.first_str)*int(self.second_str)/100  #section width 
                 self.tire_ID=int(self.rim_string)                          #Internal Diam. inch                
                 self.tire_OD=25.4*self.tire_ID+2*self.tire_SW              #Outside Diam. mm 
                 
            case 2:  # 35/65 R 33
                 print(self.second_str)
            case 3:  # 25.5 R 33
                 print(self.second_str)
            case 4:  # 18.00 R 33
                 print(self.second_str)
             

    def fct(self):
        print(self.tire_SW)
        print(self.tire_ID)
        print(self.tire_OD)

        print(self.first_str)
        print(self.second_str)
        print(self.rim_string)


p1= TireDimension("360/75 R 28")
p1.fct()