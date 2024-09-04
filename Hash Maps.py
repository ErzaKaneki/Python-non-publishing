class HashMap:
    def __init__(self, array_size):
        self.array_size = array_size
        self.array = [None for i in range(self.array_size)]

    def hash(self, key):
        key_bytes = key.encode()
        hash_code = sum(key_bytes)
        return hash_code
    
    def compressor(self, hash_code):
        return hash_code % self.array_size
    
    def assign(self, key, value):
        self.array[self.compressor(self.hash(key))] = value

    def retrieve(self, key):
        return self.array[self.compressor(self.hash(key))]
    
hash_map = HashMap(20)
hash_map.assign("gneiss", "metamorphic")
print(hash_map.retrieve("gneiss"))