#Assignment 1: Design Your Own Class 

# Base class for a general device
class Device:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model
        
        def power_on(self):
            print(f"{self.brand} {self.model} is now powered on.")
            
        def power_off(self):
            print(f"{self.brand} {self.model} is now powered off.")
            
 # Derived class for a specific type of device: Smartphone           
class Smartphone(Device):
    def __init__(self, brand, model, storage, camera_megapixels):
        super().__init__(brand, model)
        self.storage = storage
        self.camera_megalpixels = camera_megapixels
        
        def take_photos(self):
            print(f"Taking photo with {self.camera_megapixels}MP camera")
            
        def install_app(self, app_name):
            print(f"Installing {app_name} on {self.brand} {self.model}.")
            
            
# Creating an object of the Smartphone class

my_phone = Smartphone("TechBrand", "X100", "128GB" 48)
my_phone.power_on()
my_phone.take_photo()
my_phone.install_app("ChatGPT App")
my_phone.power_off()


#Activity 2: Polymorphism Challenge

class Vehicle:
    def move(self):
        pass
    
# Derived class: Car
class Car(Vehicle):
        def move(self):
            print("Driving")
 
# Derived class: Plane       
class Plane(Vehicle):
    def move(self):
        print("Flying")
        
# Derived class: Bicycle
class Bycicle(Vehicle):
    def move(self):
        print("Palding")
        
# Using polymorphism
Vehicles = [Car(), Plane(), Bycicle()]

for Vehicle in Vehicles:
    Vehicle.move()
    