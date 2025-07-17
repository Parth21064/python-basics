class sample():
    def __init__(self,argument):
        self.atribute=argument

        print('samlple created..')

mySample=sample(argument='bidhan')




class Dog():
    def __init__(self,name):
        print("constructed")
        self.name=name

    def greet(self,num):
        print("attu attu {} and the number is {}".format(self.name,num))

myDog=Dog(name="lalu")
myDog.greet(69)