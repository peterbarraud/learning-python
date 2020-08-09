
class Animal:
    # like abstract
    def Noise(self):
        pass

    def Limbs(self):
        print('{f} legs'.format(f=4))

# inherits Animal
class Dog(Animal):
    def Noise(self):
        print('Bark like an animal')


if __name__ == "__main__":
    dog = Dog()
    dog.Noise()
    dog.Limbs()