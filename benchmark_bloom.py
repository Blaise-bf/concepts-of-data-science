from bloom import CustomBloomFilterHashFunctions, BloomFilter
import nltk
import time
import random
import string
import matplotlib.pyplot as plt


def random_string(length=10):
    """Function for generating random strings"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))