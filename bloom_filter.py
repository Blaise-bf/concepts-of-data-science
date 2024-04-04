import random
import string
import time

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

    def add(self, item):
        indexes = [self.hash1(item), self.hash2(item)]
        for index in indexes:
            self.bit_array[index] = True

    def contains(self, item):
        indexes = [self.hash1(item), self.hash2(item)]
        return all(self.bit_array[index] for index in indexes)

# Generate random email addresses
def generate_email():
    username = ''.join(random.choices(string.ascii_lowercase, k=8))  # 8 random lowercase letters
    domain = ''.join(random.choices(string.ascii_lowercase, k=5))  # 5 random lowercase letters
    return f"{username}@{domain}.com"

if __name__ == "__main__":
    # Creating 10 million random email addresses
    num_emails = 10000000
    random_emails = [generate_email() for _ in range(num_emails)]

    # Initializing Bloom filter 
    bloom_filter = BloomFilter(100000000) 

    # Measure the time taken to add all generated email addresses to the Bloom filter
    start_time = time.time()
    for email in random_emails:
        bloom_filter.add(email)
    end_time = time.time()
    print(f"Time taken to add {num_emails} emails to the Bloom filter: {end_time - start_time:.4f} seconds")

    # Measure the time taken to check for presence of all generated email addresses using the Bloom filter
    start_time = time.time()
    for email in random_emails:
        bloom_filter.contains(email)
    end_time = time.time()
    print(f"Time taken to check presence of {num_emails} emails using the Bloom filter: {end_time - start_time:.4f} seconds")

    # Count false positives
    false_positives = 0
    test_items_not_present = [generate_email() for _ in range(num_emails)]  # Generating test items that are not in the dataset
    for item in test_items_not_present:
        if bloom_filter.contains(item):
            false_positives += 1

    print(f"Number of false positives: {false_positives}")
