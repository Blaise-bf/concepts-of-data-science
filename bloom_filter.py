class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [False] * size

    def hash1(self, item):
        hash_value = 0
        for char in item:
            hash_value = (hash_value * 31 + ord(char)) % self.size
        return hash_value

    def hash2(self, item):
        hash_value = 5381
        for char in item:
            hash_value = ((hash_value << 5) + hash_value) + ord(char)
        return hash_value % self.size

    def hash3(self, item):
        hash_value = 0
        for char in item:
            hash_value = (hash_value * 33) ^ ord(char)
        return hash_value % self.size

    def add(self, item):
        indexes = [self.hash1(item), self.hash2(item), self.hash3(item)]
        for index in indexes:
            self.bit_array[index] = True

    def contains(self, item):
        indexes = [self.hash1(item), self.hash2(item), self.hash3(item)]
        return all(self.bit_array[index] for index in indexes)


if __name__ == "__main__":
    bloom_filter = BloomFilter(80)

    items = ['apple', 'banana', 'orange', 'AGTC', 'CGTA', 'ATCG']
    for item in items:
        bloom_filter.add(item)

    test_items = ['apple', 'banana', 'orange', 'grape', 'AGTC', 'CGTA', 'ATCG', 'GATTACA']
    for item in test_items:
        if bloom_filter.contains(item):
            print(f"Item '{item}' may be present.")
        else:
            print(f"Item '{item}' is definitely not present.")
