from bloom import CustomBloomFilterHashFunctions, BloomFilter
import nltk
import time
import random
import string
import matplotlib.pyplot as plt


def random_string(length=10):
    """Function for generating random strings"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))
def benchmark_custom_bloom_filter() -> dict:
    """This function evaluates the insertion and lookup time for 
    variable amount of data for a custom bloom filter

    Returns:
        dict: a dictionary with the diffrent number of items added to 
        the bloom filter and their respective lookup times
    """
    # define an array of number of elements to add to the bloom filter
    sizes = [1000, 5000, 10000, 20000, 50000, 100000, 500000, 1000000, 5000000]
 
    size = 10000000  # Size of the Bloom filter
    results = {'size': [], 'insertion_time': [], 'lookup_time': []}

    for n in sizes:
        bloom_filter = BloomFilter(size)
        insert_data = [random_string() for _ in range(n)]
        lookup_data = [random_string() for _ in range(n)]

    
    return results