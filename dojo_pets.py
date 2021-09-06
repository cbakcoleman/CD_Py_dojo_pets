# add Pet class
class Pet:
    def __init__(self, name, type, tricks, health, energy):
        self.name = name
        self.type = type
        self.tricks = tricks
        self.health = health
        self.energy = energy

# add methods
    def sleep(self):
        self.energy += 25
        return self

    def eat(self):
        self.energy += 5
        self.health += 10
        return self

    def play(self):
        self.health += 5

    def noise(self, type):
        if type == "dog":
            print('Mung Mong')
        elif type =="cat":
            print('Ya Ong')
        elif type =="duck":
            print("Ggwek Ggwek")

pet1 = Pet("Charlie", "dog", "sit", 25, 50)
pet2 = Pet("Garfield", "cat", "purr", 15, 10)
pet3 = Pet("Huey", "duck", "waddle", 10, 15)

# add Human class, associate class Pet
class Human:
    def __init__(self, first_name, last_name, pet, treats, pet_food):
        self.first_name = first_name
        self.last_name = last_name
        self.pet = Pet()
        self.treats = treats
        self.pet_food = pet_food

    def walk(self):
        self.pet.play()
        return self

    def feed(self):
        self.pet.eat()

    def bathe(self):
        self.pet.noise()

human1 = Human("Charles", "Gunn", pet1, "beggin strips", "alpo")
human2 = Human("Cordelia", "Chase", pet2, "bonito flakes", "meowmix")
human3 = Human("Fred", "Burkle", pet3, "grapes", "greens")
