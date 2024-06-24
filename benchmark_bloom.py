from bloom import CustomBloomFilterHashFunctions, BloomFilter
import time
import random
import string
import matplotlib.pyplot as plt
from faker import Faker


def random_string(length=10):
    """Function for generating random strings"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_words(num_words: int, locale: str = 'en_US') -> list:
    """Generates random words using the faker packge

    Args:
        num_words (int): number of words to be generated
        locale (str, optional): language specification. Defaults to 'en_US'.

    Returns:
        list: a list of random words
    """
    faker = Faker(locale)
    return [faker.word() for _ in range(num_words)]


def generate_random_dna_sequence(length: int) -> str:
    return ''.join(random.choices('ACGT', k=length))

def generate_random_dna_sequences(num_sequences: int, sequence_length: int) -> list:
    """generate random string of DNA sequences

    Args:
        num_sequences (int): number of sequences to be generated
        sequence_length (int): length of dna sequence

    Returns:
        list: a list of DNA sequences generated
    """
    return [generate_random_dna_sequence(sequence_length) for _ in range(num_sequences)]



def random_string(length=10):
    """Function for generating random strings"""
    return ''.join(random.choices(string.ascii_letters + string.digits, k=length))

def generate_random_words(num_words: int, locale: str = 'en_US') -> list:
    """Generates random words using the faker package"""
    fake = Faker(locale)
    return [fake.word() for _ in range(num_words)]


def benchmark_custom_bloom_filter(data_type: str, num_hashes_list: list) -> dict:
    """Benchmark for custom bloom filter with different data types and number of hash functions"""
    sizes = [i for i in range(20000, 1000001, 20000)]
    size = 5000000 # Size of the Bloom filter
    results = {num_hashes: {'size': [], 'insertion_time': [], 'lookup_time': [], 'compression_rate': [], 'false_positive_rate': []} for num_hashes in num_hashes_list}

    for num_hashes in num_hashes_list:
        for n in sizes:
            bloom_filter = BloomFilter(size, num_hashes)

            if data_type == 'random_string':
                insert_data = [random_string() for _ in range(n)]
                lookup_data = [random_string() for _ in range(n)]
            elif data_type == 'random_words':
                insert_data = generate_random_words(n)
                lookup_data = generate_random_words(n)
            elif data_type == 'dna':
                insert_data = generate_random_dna_sequences(n, 50)
                lookup_data = generate_random_dna_sequences(n, 50)
            else:
                raise ValueError(f"Unknown data type: {data_type}")

            print(f'Inserting {n} {data_type} elements with {num_hashes} hash functions')
            start_time = time.time()
            for item in insert_data:
                bloom_filter.add(item)
            insertion_time = time.time() - start_time

            print(f'Looking up {n} {data_type} elements with {num_hashes} hash functions')
            start_time = time.time()
            for item in lookup_data:
                bloom_filter.check(item)
            lookup_time = time.time() - start_time

            theoretical_false_positive_rate = bloom_filter.calculate_false_positive_rate()
            compression_rate = bloom_filter.calculate_compression_rate()

            results[num_hashes]['size'].append(n)
            results[num_hashes]['insertion_time'].append(insertion_time)
            results[num_hashes]['lookup_time'].append(lookup_time)
            results[num_hashes]['compression_rate'].append(compression_rate)
            results[num_hashes]['false_positive_rate'].append(theoretical_false_positive_rate)

    return results

def plot_results(results, data_type) -> None:
    """Plots benchmarking results with different line colors for number of hash functions"""
    plt.figure(figsize=(18, 24))

    plt.subplot(2, 2, 1)
    for num_hashes, data in results.items():
        plt.plot(data['size'], data['insertion_time'], marker='o', label=f'{num_hashes} hash functions')
    plt.xlabel('Number of Elements')
    plt.ylabel('Insertion Time (s)')
    plt.title(f'Insertion Time vs Number of Elements\n(Data Type: {data_type})')
    plt.legend()

    plt.subplot(2, 2, 2)
    for num_hashes, data in results.items():
        plt.plot(data['size'], data['lookup_time'], marker='o', label=f'{num_hashes} hash functions')
    plt.xlabel('Number of Elements')
    plt.ylabel('Lookup Time (s)')
    plt.title(f'Lookup Time vs Number of Elements\n(Data Type: {data_type})')
    plt.legend()

    plt.subplot(2, 2, 3)
    for num_hashes, data in results.items():
        plt.plot(data['size'], data['compression_rate'], marker='o', label=f'{num_hashes} hash functions')
    plt.xlabel('Number of Elements')
    plt.ylabel('Compression Rate')
    plt.title(f'Compression Rate vs Number of Elements\n(Data Type: {data_type})')
    plt.legend()

    plt.subplot(2, 2, 4)
    for num_hashes, data in results.items():
        plt.plot(data['size'], data['false_positive_rate'], marker='o', label=f'{num_hashes} hash functions')
    plt.xlabel('Number of Elements')
    plt.ylabel('False Positive Rate')
    plt.title(f'False Positive Rate vs Number of Elements\n(Data Type: {data_type})')
    plt.legend()

    plt.tight_layout()
    plt.savefig(f'bloom_benchmark_{data_type}.png')
    plt.close()


# Benchmark and plot for different data types and number of hash functions
data_types = ['random_string', 'random_words', 'dna']
num_hashes_list = list(range(5, 26, 5))

for data_type in data_types:
    results = benchmark_custom_bloom_filter(data_type, num_hashes_list)
    plot_results(results, data_type)

def benchmark_false_positive_rate(expected_n: int, max_n: int, step: int, hash_funcs_list: list, word_list: list) -> None:

    """this function evaluates the false positive rate of the as the number of inserted elements in 
    the filter approaches the expected capacity of the bloom filter.
    Args:
        expected_n(int): expected capacity of filter
        max_n(int): maximum size of filter
        hash_funcs_list: a list of the number of hash functions to use for the bloom filter
        word_list(list): random natural items to be added to the filter

    Returns:
        None: 
    """

    results = []

    word_list_extended = word_list * (max_n // len(word_list) + 1)

    for num_hashes in hash_funcs_list:
        bloom_filter = BloomFilter(expected_n * 10, num_hashes)
        current_results = {'num_inserted': [], 'false_positive_rate': [], 'num_hashes': num_hashes}

        for n in range(0, max_n + 1, step):
            insert_data = word_list_extended[:n]

            # Insert elements
            for item in insert_data:
                bloom_filter.add(item)

            # Calculate false positive rate
            false_positive_rate = bloom_filter.calculate_false_positive_rate()

            current_results['num_inserted'].append(n)
            current_results['false_positive_rate'].append(false_positive_rate)

        results.append(current_results)

    return results

def plot_results(results):
    plt.figure(figsize=(12, 6))

    for result in results:
        plt.plot(result['num_inserted'], result['false_positive_rate'], marker='o', label=f"Hash functions: {result['num_hashes']}")

    plt.xlabel('Number of Elements Inserted')
    plt.ylabel('False Positive Rate')
    plt.title('False Positive Rate vs Number of Elements Inserted')
    plt.legend()
    plt.grid(True)
    plt.show()

# plot_results(results)
