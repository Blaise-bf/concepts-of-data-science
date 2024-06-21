# concepts-of-data-science
This repo hosts contents of my concept of data science course project

# Project Description

This project aims to evaluate the implementaion and testing of the inner workings of a bloom filter algorithm. It also evaluates the use of supercomputer capabilities to test insertion and lookup of huge number of elements to the bloom filter.
# Implemenation
We used an object oriented approach to build two custom classess, one which implemented the bloom filter algorithm (BloomFilter), and another which implemented a family of custom hash functions (9 functions) while ensuring there are littile to no correlations for the different has functions, thus reducing the risk of hash function collisions.

Benchamarking was done in two steps:
1: evaluation of the lookup and insertion time of the bloom filter algorithm, which made use of of the implemented function 'benchmark_custom_bloom_filter'. 
2: evalaution of the false positive rate as a function of the number of items added to the bloom filter