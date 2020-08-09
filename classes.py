
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

    @property
    def Name(self):
        return self.__name
        
    @Name.setter
    def Name(self, val):
        self.__name = val


if __name__ == "__main__":
    dog = Dog()
    dog.Noise()
    dog.Limbs()
    dog.Name = 'Bonzo'
    print(dog.Name)