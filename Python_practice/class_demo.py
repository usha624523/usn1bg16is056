class parrot:
    species="bird"
    def __init__(self,name,age):
        self.name=name
        self.age=age
blu=parrot("Blu",10)
woo=parrot("woo",15)
print("blue is a {}".format(blu.__class__.species))
print("woo is a {}".format(woo.__class__.species))
print("{} is {} years old".format(blu.name,blu.age))
print("{} is {} years old".format(woo.name,woo.age))
  
