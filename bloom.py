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