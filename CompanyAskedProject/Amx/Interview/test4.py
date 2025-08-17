# def count_up_to_n(n):
#     count = 1
#     while count <= n:
#         yield count
#         count +=1
        

# gen = count_up_to_n(5)
# print(next(gen))
# # for num in gen:
# #     print(num)
class Animal:
    def speak(self):
        pass

class Dog(Animal):
    def speak(self):
        return "bark"
class Cat(Animal):
    def speak(self):
        return "meow"

class AnimalFactory:
    def get_animal(self, animal_type):
        if animal_type == 'dog':
            return Dog()
        elif animal_type == 'cat':
            return Cat()
        else:
            raise ValueError("any error")
        
factory = AnimalFactory()

a1 = factory.get_animal("dog")
print(a1.speak())
    