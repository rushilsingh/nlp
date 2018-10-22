Usage:
python count_clusters.py <filename> <length>

Here, <filename> is the name of the file containing the text to be processed. <length> refers to the length in terms of number of words of the clusters we want to find repetitions for.

For example 'hello world' is a 2 word cluster, so if length is set to 2, all occurrences of 'hello world' (and other clusters of length 2) will be counted and added to a dictionary. The dictionary will have the clusters as keys, and the number of occurrences as values.
