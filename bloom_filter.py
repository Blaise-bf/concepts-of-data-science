class BloomFilter:
    def __init__(self, size):
        self.size = size
        self.bit_array = [False] * size

    def custom_hash(self, item):
        hash_value = 0
        for char in item:
            hash_value = (hash_value * 31 + ord(char)) % 2**32
        return hash_value % self.size

    def add(self, item):
        index = self.custom_hash(item)
        self.bit_array[index] = True

    def contains(self, item):
        index = self.custom_hash(item)
        return self.bit_array[index]


if __name__ == "__main__":
    
    bloom_filter = BloomFilter(20)

    items = ['apple', 'banana', 'orange']
    for item in items:
        bloom_filter.add(item)

    test_items = ['apple', 'banana', 'orange', 'grape']
    for item in test_items:
        if bloom_filter.contains(item):
            print(f"Item '{item}' may be present.")
        else:
            print(f"Item '{item}' is definitely not present.")
