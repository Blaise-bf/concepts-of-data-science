
class CustomBloomFilterHashFunctions:
    """
    A class to implement custom hash functions for Bloom Filters.
    """
    def __init__(self, size: int):
        self.size = size
    
    def _hash1(self, item: str) -> int:
        # A simple base hash function that uses character summation
        return sum(ord(char) for char in item) % self.size

    def _hash2(self, item: str) -> int:
        # A more complex hash that considers the character positions
        hash_val = 0
        for i, char in enumerate(item):
            hash_val = hash_val * 31 + ord(char)
        return hash_val % self.size

    def _hash3(self, item: str) -> int:
        # Another hash function that uses a different prime multiplier
        hash_val = 0
        for char in item:
            hash_val = (hash_val * 53 + ord(char)) % self.size
        return hash_val

    def _hash4(self, item: str) -> int:
        # A hash function that uses bitwise operations
        hash_val = 0
        for char in item:
            hash_val = (hash_val << 5) - hash_val + ord(char)
        return hash_val % self.size
    def _hash5(self, item: str) -> int:
         # A hash function that uses a different prime multiplier and bitwise operations
        hash_val = 0
        for char in item:
            hash_val = (hash_val * 101 + ord(char)) % self.size
        return hash_val

    def _hash6(self, item: str) -> int:
        # A hash function that combines polynomial hashing with a different base
        hash_val = 0
        for char in item:
            hash_val = (hash_val * 67 + ord(char)) % self.size
        return hash_val

    def _hash7(self, item: str) -> int:
        # A hash function that uses alternating additions and subtractions
        hash_val = 0
        for i, char in enumerate(item):
            if i % 2 == 0:
                hash_val = (hash_val + ord(char)) % self.size
            else:
                hash_val = (hash_val - ord(char)) % self.size
        return hash_val

    def _hash8(self, item: str) -> int:
        # A hash function that uses multiplication and addition
        hash_val = 0
        for char in item:
            hash_val = (hash_val * 37 + ord(char)) % self.size
        return hash_val

    def _hash9(self, item: str) -> int:
        # A hash function that uses bitwise XOR operations
        hash_val = 0
        for char in item:
            hash_val = (hash_val ^ ord(char) * 41) % self.size
        return hash_val
    
    def get_hashes(self, item: str) -> list:
        """Generate multiple custom hash values for the given item."""
        return [
            self._hash1(item),
            self._hash2(item),
            self._hash3(item),
            self._hash4(item),
            self._hash5(item),
            self._hash6(item),
            self._hash7(item),
            self._hash8(item),
            self._hash9(item)
        ]
    

## add custom bloom filter class
class BloomFilter:
    """
    This creates a custom bbool filter class with functionality to 
    add and check elements elements inserted.
    """
    def __init__(self, size):
        self.size = size
        self.bit_array = [0] * size
        self.hash_functions = CustomBloomFilterHashFunctions(size)
        self.n = 0

    def add(self, item) -> None:
        # Get the hash positions and set them to 1 in the bit array
        positions = self.hash_functions.get_hashes(item)
        for pos in positions:
            self.bit_array[pos] = 1
        self.n += 1
    
    def check(self, item) -> bool:
        # Check if all positions calculated by hash functions are set to 1
        positions = self.hash_functions.get_hashes(item)
      
        if all(self.bit_array[pos] for pos in positions):
            return True
        else:
            return False
