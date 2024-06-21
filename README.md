# concepts-of-data-science
This repo hosts contents of my concept of data science course project

# Project Description

This project aims to evaluate the implementaion and testing of the inner workings of a bloom filter algorithm. It also evaluates the use of supercomputer capabilities to test insertion and lookup of huge number of elements to the bloom filter.
# Implemenation
We used an object oriented approach to build two custom classess, one which implemented the bloom filter algorithm (BloomFilter), and another which implemented a family of custom hash functions (9 functions) while ensuring there are littile to no correlations for the different has functions, thus reducing the risk of hash function collisions.

Benchamarking was done in two steps:
1: evaluation of the lookup and insertion time of the bloom filter algorithm, which made use of of the implemented function 'benchmark_custom_bloom_filter'. 
2: evalaution of the false positive rate as a function of the number of items added to the bloom filter

# Time complexity
The time complexity of a Bloom filter algorithm is very efficient for both insertion and lookup operations. Specifically, both operations are 𝑂(𝑘), where k is the number of hash functions used. During insertion, each of the k hash functions is applied to the input element to determine the k positions in the bit array that need to be set to 1. Similarly, during a lookup, the same k hash functions are applied to check the corresponding positions in the bit array. Since k is typically a small constant, the time complexity for these operations is essentially O(1) in practice. However, the exact time depends on the efficiency of the hash functions and the speed of accessing the bit array.

# Space complexity
The space complexity of a Bloom filter is determined by the size of the bit array used to store the filter. Additionally, the space complexity includes the storage required for the k hash functions, but this is usually negligible compared to the size of the bit array.

# False Positive rate
As elements are inserted into the Bloom filter, the false positive rate remains relatively low. This phase corresponds to the number of elements being well within the expected capacity of the Bloom filter. As the number of inserted elements approaches the expected capacity , the false positive rate begins to increase. This is because the likelihood of hash collisions increases, leading to more false positives. When the number of inserted elements exceeds the expected capacity, the false positive rate rises significantly. This rapid increase highlights the limitation of the Bloom filter, as it becomes saturated and hash collisions become very common.

