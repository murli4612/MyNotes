# Base class (Superclass)
class Bird:
    def __init__(self, name):
        self.name = name
    def make_sound(self):
        raise NotImplementedError("Base class should be must implemented  the 'make sound method'")
class Sparrow(Bird):
    # pass
    def make_sound(self):
        return f"{self.name} chrips"
        return super().make_sound()
class Penguin(Bird):
    def make_sound(self):
        return f"{self.name} honks"
        # return super().make_sound()
# Create instances of the derived classes
sparrow_instance = Sparrow("Sparrow1")
penguin_instance = Penguin("Penguin1")

print(sparrow_instance.make_sound())
print(penguin_instance.make_sound())
#