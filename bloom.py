import hashlib
import mmh3
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from scipy.stats import chi2_contingency

class CustomBloomFilterHashFunctions:
    """
    A class to implement custom hash functions for Bloom Filters using hashlib and mmh3.
    """

    def __init__(self, size: int, num_hashes: int):
        """initialize custom bloom filter class

        Args:
            size (int): capacityof bloom filter
            num_hashes (int): number of hash functions
        """
        self.size = size
        self.num_hashes = num_hashes
        # Algorithms to use for 
        self.hash_algorithms = ['md5', 'sha1', 'sha256', 'sha512', 'blake2b']

    def _hashlib_hash(self, item: str, algorithm: str) -> int:
        """
        Hash function using hashlib.
        """
        hash_func = getattr(hashlib, algorithm)
        hash_val = int(hash_func(item.encode('utf-8')).hexdigest(), 16)
        return hash_val % self.size

    def _mmh3_hash(self, item: str, seed: int) -> int:
        """
        Hash function using mmh3.
        """
        hash_val = mmh3.hash(item, seed)
        return hash_val % self.size

    def get_hashes(self, item: str) -> list:
        """Generate multiple custom hash values for the given item."""
        hashes = []
        seeds = list(range(self.num_hashes))
        for i in range(self.num_hashes):
            if i < len(self.hash_algorithms):
                hashes.append(self._hashlib_hash(item, self.hash_algorithms[i]))
            else:
                hashes.append(self._mmh3_hash(item, seeds[i]))
        return hashes

    def check_uniformity_with_chisquare(self, items: list) -> None:
        """
        Check for uniformity of hash functions using Chi-Squared test.
        """
        # Collect all hash values
        hash_values = []
        for item in items:
            hash_values.append(self.get_hashes(item))

        # Convert to numpy array for easier manipulation
        hash_values = np.array(hash_values)

        # Perform Chi-Squared test for each hash function
        for i in range(hash_values.shape[1]):
            observed_freq, _ = np.histogram(hash_values[:, i], bins=min(self.size, 10))
            expected_freq = np.ones(len(observed_freq)) * len(items) / len(observed_freq)
            chi2, p_value = chi2_contingency([observed_freq, expected_freq])[:2]
            print(f'Hash Function {i + 1}: Chi2 = {chi2:.2f}, p-value = {p_value:.2f}')

        # Plot histogram for visualization
        n_hashes = hash_values.shape[1]
        ncols = 3
        nrows = (n_hashes + ncols - 1) // ncols

        plt.figure(figsize=(15, 7))
        for i in range(n_hashes):
            plt.subplot(nrows, ncols, i + 1)
            plt.hist(hash_values[:, i], bins=min(self.size // 10, 10), edgecolor='black')
            plt.title(f'Hash Function {i + 1}')
        plt.tight_layout()
        plt.show()

        # Check for independence using correlation matrix
        corr_matrix = np.corrcoef(hash_values.T)
        plt.figure(figsize=(10, 8))
        sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', vmin=-1, vmax=1)
        plt.title('Correlation Matrix of Hash Functions')
        plt.show()

class BloomFilter:
    """
    This creates a custom bloom filter class with functionality to 
    add and check elements inserted.
    """

    def __init__(self, size: int, num_hashes: int) -> None:
        """initialize bloom filter class

        Args:
            size (int): size of bloom fiter
            num_hashes (int): number of hash functions
        """
        self.size = size
        self.bit_array = [0] * size
        self.hash_functions = CustomBloomFilterHashFunctions(size, num_hashes)
        self.num_hashes = num_hashes
        self.n = 0

    def add(self, item: str) -> None:
        """checks 

        Args:
            item (str): item to add in bloom filter
        """
        # Get the hash positions and set them to 1 in the bit array
        positions = self.hash_functions.get_hashes(item)
        for pos in positions:
            self.bit_array[pos] = 1
        self.n += 1

    def check(self, item: str) -> bool:
        """this method checks if given string is in a bloom filter

        Args:
            item (str): abritray string

        Returns:
            bool: returns true if item in filter and false otherwise
        """
        # Check if all positions calculated by hash functions are set to 1
        positions = self.hash_functions.get_hashes(item)

        if all(self.bit_array[pos] for pos in positions):
            return True
        else:
            return False

    def calculate_false_positive_rate(self) -> float:
        """
        This method calculates false positive rate based on the number 
        of items added to the bloom filter as well as the number of hash functions and the
        size of the bloom filter data structure.
        """
        size = self.size
        number_of_elements = self.n
        return (1.0 - ((1.0 - 1.0 / size) ** (self.num_hashes * number_of_elements))) ** self.num_hashes

    def calculate_compression_rate(self) -> float:
        """This function checks the compression rate of the bloom filter as 
        a function of the number of elements added to the data structure.

        Returns:
            float: compression rate
        """
        theoretical_min_size = self.n * np.log2(np.e)
        return self.size / theoretical_min_size
