def max_contig_sum(L):
    """
    
    :param L: a list of integers, at least one positive
    :return: the maximum of a contiguous subsequence in L
    """
    max_sum = 0
    for start_position in range(len(L)+1):
        for end_position in range(start_position, len(L)+1):
            sequence_sum = sum(L[start_position:end_position])
            if max_sum < sequence_sum:
                max_sum = sequence_sum
    return max_sum

list1 = [3, 4, -1, 5, -4]
list2 = [3, 4, -8, 15, -1, 2]

print(max_contig_sum(list1))
print(max_contig_sum(list2))