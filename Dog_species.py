class Dog:
    species = "Canis lupus familiaris"  

    def __init__(self, name, breed):
        self.name = name  
        self.breed = breed  

    def display_details(self):
        print(f"Name: {self.name}, Breed: {self.breed}, Species: {Dog.species}")

dog1 = Dog("Max", "Labrador Retriever")
dog2 = Dog("Bella", "German Shepherd")

dog1.display_details()
dog2.display_details()
