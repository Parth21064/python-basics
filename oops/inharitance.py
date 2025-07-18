class Grandfather():
    def __init__(self):
        print("Grandfather constructed.")
    def name(self):
        print("Jhoru Mandal")
    def vill(self):
        print("Village Banamali pur")
    
class Father(Grandfather):#inharite
    def __init__(self,age):
        self.age=age
        Grandfather.__init__(self)#self call
        print("Father constructed.")
    
    def name(self):
        print("Ganesh Mandal.")#override

    


dadu=Grandfather()

baba=Father(40)

dadu.name()
baba.name()

dadu.vill()
baba.vill()
print(baba.age)


