#  Packages are Objects which contain a python list of 12 Attributes:
#  [PackageID (str), Street Address (str), City (str), State (str), Zip Code (str),
#  Delivery Deadline (datetime object), Weight (str), Special Notes (str),
#  Delivery Status (str),Departure Time (datetime object), Delivery Time (datetime object),
#  and the Address Index (str) (found in addressData.csv)]

class Package:

    def __init__(self):
        self.attributes = 12
        self.set = [None] * self.attributes

    def get(self):
        return self.set

    def update(self, attribute, value):
        self.set[int(attribute)] = value

    def print(self):
        print('---Package ID: ' + str(self.set[0]) + ' ----')
        print('Address: ' + str(self.set[1]) + ', ' + str(self.set[2]) + ', ' + str(self.set[3]) + ', ' + str(self.set[4]))
        print('Location Index:  ' + str(self.set[11]))
        print('Deadline: ' + str(self.set[5]))
        print('Weight: ' + str(self.set[6]))
        print('Note: ' + str(self.set[7]))
        print('Status: ' + str(self.set[8]))
        if self.set[9] != 'None':
            print('Departure Time: ' + str(self.set[9].time()))
        else:
            print('Departure Time: ' + str(self.set[9]))

        if self.set[10] != 'None':
            print('Delivery Time: ' + str(self.set[10].time()))
        else:
            print('Delivery Time: ' + str(self.set[10]))
