
# that includes a constructor with default parameters.

class Dog:
    def __init__(self, name,breed="Mutt"):
        self.name = name
        self.breed = breed

fido = Dog("Fido")
print(f"Name: {fido.name}, Breed: {fido.breed}")