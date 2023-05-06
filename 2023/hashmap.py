#  Req E: Hash table with insertion function and the following components: (Held in the Value which is a Package Object)
#  packageID, delivery address, delivery deadline, delivery city, delivery zip code, package weight, delivery status


class HashMap:
    def __init__(self):
        self.size = 40
        self.map = [None] * self.size

    def add(self, key, value):
        key_hash = int(key) % 40
        while True:
            if self.map[key_hash] is None:
                self.map[key_hash] = [[key, value]]
                return False

    def get(self, key):
        key_hash = int(key) % self.size
        for i in range(self.size+1):
            if self.map[key_hash][0][0] == key:
                return self.map[key_hash][0][1]
