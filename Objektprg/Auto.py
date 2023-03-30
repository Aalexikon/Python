class car:
    def __init__(self, carmake, color, model, km):
        self.carmake = carmake
        self.color = color
        self.model = model
        self.km = km 

my_car= car("Toyota,", "černobílá,", "AE86,", "136 000 km")
my_car02= car("Honda,", "červená,", "Civic 6g,", "92 000 km")
print(my_car.carmake, my_car.color, my_car.model, my_car.km)
print(my_car02.carmake, my_car02.model, my_car02.color, my_car02.km)
