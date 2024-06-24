# concepts-of-data-science
This repo hosts contents of my concept of data science course project

# Project Description

This project aims to evaluate the implementaion and testing of the inner workings of a bloom filter algorithm. It also evaluates the use of supercomputer capabilities to test insertion and lookup of huge number of elements to the bloom filter.
# Implemenation
We used an object oriented approach to build two custom classess, one which implemented the bloom filter algorithm (BloomFilter), and another which implemented a family of custom hash functions  while ensuring there are littile to no correlations for the different hash functions, thus reducing the risk of hash function collisions.

Benchamarking was done in two steps:
1: evaluation of the lookup and insertion time of the bloom filter algorithm, which made use of of the implemented function 'benchmark_custom_bloom_filter'. 
2: evalaution of the false positive rate as a function of the number of items added to the bloom filter

# Time complexity
The Bloom filter implementation demonstrates impressive efficiency in terms of both time and space complexity. The insertion (add) and query (check) operations have a time complexity of 𝑂(num_hashes), where num_hashes represents the number of hash functions used. Each operation requires hashing the input multiple times and either setting or checking the corresponding bits in the bit array. Since hashing and bit manipulation are constant-time operations, the time complexity remains low, ensuring that both insertion and lookup operations are performed swiftly.

# Space complexity
The space complexity of a Bloom filter is determined by the size of the bit array used to store the filter. Additionally, the space complexity includes the storage required for the k hash functions, but this is usually negligible compared to the size of the bit array.

Overall, the Bloom filter offers a highly efficient and scalable solution for set membership tests, balancing low time complexity for operations with a manageable space requirement. Its probabilistic nature, which allows for controlled false positive rates, makes it suitable for applications needing rapid insertion and lookup operations with minimal memory usage.

# False Positive rate
As elements are inserted into the Bloom filter, the false positive rate remains relatively low. This phase corresponds to the number of elements being well within the expected capacity of the Bloom filter. As the number of inserted elements approaches the expected capacity , the false positive rate begins to increase. This is because the likelihood of hash collisions increases, leading to more false positives. When the number of inserted elements exceeds the expected capacity, the false positive rate rises significantly. This rapid increase highlights the limitation of the Bloom filter, as it becomes saturated and hash collisions become very common.
# Compression Rate
The compression rate of a Bloom filter refers to its ability to represent a set of elements compactly while still providing probabilistic guarantees about membership queries. Specifically, it quantifies how much memory the Bloom filter saves compared to a more traditional data structure, like a hash table, that might be used to achieve similar functionality. This measures the space efficiency compared to traditional data structures. Overall, the compression rate of the implemented bloom filter drops significantly as the number of elememts approaches the expected number of elements for the given blom filter.

# Conclusion 
Overall, the implemented algorithm shows the bloom filter is an efficient data structure with insertion and lookup time of O(k), where k is the number of hash functions. There are several approach of optimizing the algorihm depending the needs of the data structure, for a scenario where the false positive rate is a big issue, the optimize size of the algorith can be estimated as a function of the false positive rate and the number of hash functions, with the downside of having a data structure with a limited capacity of items it can hold. Another approach is to procide a large bloomfilter capacity, which could be the right approach given the relatively low cost of memory. It should be noted that the higher the number of hash functions used, the time required to add large amount of data increases as well, however, this does not affect the insertion or lookup time for individual elements which depends solely on the number of hash funtions.


