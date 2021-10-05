# LAB NOTES PMT
class Livestock:
   def __init__(self, age):
       self.age = age

   # return this animal's age
   def get_age(self):
       return self.age

   # return the type of animal (alpaca, camel, or donkey)
   def get_animal_type(self):
       return self.type

   # Determine and return the price of this animal
   def get_price(self):
       return 0


class Alpaca(Livestock):
   def __init__(self, age, weight):
       super().__init__(age)
       self.weight = weight
       self.type = "Alpaca"

   def get_price(self):
       if self.age <= 3:
           return 10000
       elif self.weight <= 300:
           return 80000
       else:
           return 100000


class Camel(Livestock):
   def __init__(self, age, numberOfHumps):
       super().__init__(age)
       self.numberOfHumps = numberOfHumps
       self.type = "Camel"

   def get_price(self):
       if self.age <= 3:
           return 50000
       elif self.numberOfHumps == 2:
           return 15000
       elif self.numberOfHumps == 3:
           return 200000
       else:
           return 1000000


class Donkey(Livestock):
   def __init__(self, age, breed):
       super().__init__(age)
       self.breed = breed
       self.type = "Donkey"

   def get_price(self):
       if self.age <= 3:
           return 20000
       elif self.breed <= "Miniature":
           return 100000
       elif self.breed <= "Burro":
           return 120000
       elif self.breed <= "American Mammoth Jack":
           return 80000
       else:
           print("This breed of donkey does not exist")
           return 0


class FarmApp:
   def __init__(self):
       self.livestockList = []

   # return a list of sold animals
   def get_livestock(self):
       return self.livestockList

   def add_livestock(self, livestock):
       self.livestockList.append(livestock)
       return

   def get_total_price(self):
       return sum([i.get_price() for i in self.livestockList])


def main():
   farm = FarmApp()
   animal1 = Alpaca(5, 600)  # parameters: (int age, int weight)
   animal2 = Camel(5, 3)  # parameters: (int age, int number of humps)
   animal3 = Donkey(6, "Miniature")  # parameters: (int age, String breed)

   farm.add_livestock(animal1)
   farm.add_livestock(animal2)
   farm.add_livestock(animal3)

   animals = farm.get_livestock()
   print("List of animals sold")
   print("====================\n")

   for animal in animals:
       print(animal.get_animal_type(), '\t$', animal.get_price())
   print('\nTotal Sales \t$', farm.get_total_price())

   animal4 = Donkey(2, "American Mammoth Jack")  # parameters: (int age, string breed)
   animal5 = Donkey(7, "Burrow")  # parameters: (int age, string breed)
   animal6 = Alpaca(2, 250)  # parameters: (int age, int weight)

   farm.add_livestock(animal4)
   farm.add_livestock(animal5)
   farm.add_livestock(animal6)

   for animal in animals:
       print(animal.get_animal_type(), '\t$', animal.get_price())
   print('\nTotal Sales \t$', farm.get_total_price())

main()
