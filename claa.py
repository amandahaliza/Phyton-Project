class Animal :
    name = ""
    color = ""
    voice = ""
    
    def __init__(self, animal_name, animal_color):
        self.name = animal_name
        self.color = animal_color

    def makesound (self, sound):
        print(f"{self.name} with color {self.color} making sound {sound}")

    def eat (self, food):
        print("It is eating", food)
    
cat = Animal("Meng", "Orange")
panda = Animal("Pipah", "Pink")


print(type(cat))
print(type(panda))

#cat.name = "Meng"
#cat.color = "Orange"
#print(cat.name)
cat.makesound("meaw")
cat.eat("fish")

panda.name = "Pipah"
panda.color = "Pink"
print(panda.name)
