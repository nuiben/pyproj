# Truck Objects
# Holds a name, a float of its miles driven, fixed package capacity of 16 , and a list of PackageIDs

class Truck:

    def __init__(self, name, package_array):
        self.name = name
        self.miles = 0.0
        self.size = 16
        self.set = package_array

    def remove(self, key):  # When a package is delivered
        self.set.remove(key)

    def print(self):
        print(self.name + ' Report: ' + str(round(self.miles, 2)) + ' mi')
