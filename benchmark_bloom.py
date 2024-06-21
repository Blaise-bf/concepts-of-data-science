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

        print(f'inserting {n} elements in bloom filter')
        start_time = time.time()
        for item in insert_data:
            bloom_filter.add(item)
        insertion_time = time.time() - start_time

        print(f'looking up {n} elements in bloom filter')
        start_time = time.time()
        for item in lookup_data:
            bloom_filter.check(item)
        lookup_time = time.time() - start_time

        results['size'].append(n)
        results['insertion_time'].append(insertion_time)
        results['lookup_time'].append(lookup_time)



       
    return results

# get benchmark results
results = benchmark_custom_bloom_filter()


def plot_results(results) -> None:
    """plots benchmarking results

    Args:
        results (dict): a dictionary of different sizes,
          and their respective insertion and lookup times
        
    """
    plt.figure(figsize=(18, 6))

    plt.subplot(1, 2, 1)
    plt.plot(results['size'], results['insertion_time'], marker='o')
    plt.xlabel('Number of Elements')
    plt.ylabel('Insertion Time (s)')
    plt.title('Insertion Time vs Number of Elements')

    plt.subplot(1, 2, 2)
    plt.plot(results['size'], results['lookup_time'], marker='o')
    plt.xlabel('Number of Elements')
    plt.ylabel('Lookup Time (s)')
    plt.title('Lookup Time vs Number of Elements')


    plt.tight_layout()
    plt.savefig('bloom_benchmark.png')
    plt.close()

# Plot bench mark results
plot_results(results)

def benchmark_false_positive_rate(expected_n, max_n, step):
    """This function performs evaluation of the false positive rate
    as a function of the number of elements being added to the bloom filter

    Args:
        expected_n (int): expected number of elements
        max_n (int): maximum number of elements
        step (int): step size for number of elements

    Returns:
        dict: dicionary of number of elements inserted and the false positive rate
    """
    size = expected_n * 10  # Size of the Bloom filter
    bloom_filter = BloomFilter(size)
    results = {'num_inserted': [], 'false_positive_rate': []}
    
    word_list_extended = word_list * (max_n // len(word_list) + 1)

    for n in range(0, max_n + 1, step):
        insert_data = word_list_extended[:n]

        # Insert elements
        for item in insert_data:
            bloom_filter.add(item)

        # Calculate false positive rate
        false_positive_rate = bloom_filter.calculate_false_positive_rate()

        results['num_inserted'].append(n)
        results['false_positive_rate'].append(false_positive_rate)

    return results
expected_n = 1000
max_n = 3000
step = 100
results = benchmark_false_positive_rate(expected_n, max_n, step)
