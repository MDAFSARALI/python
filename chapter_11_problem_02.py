class Animals:
    animalType="Mammel"
class pets(Animals):
    petColour="White"
class Dog(pets):
    @staticmethod
    def bark():
        print("Bow Bow!!")

d=Dog()
d.bark()