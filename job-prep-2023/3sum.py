from typing import List, Tuple
from itertools import combinations


def _same_tuple(t1: Tuple, t2, Tuple) -> bool:

    return True

def sum3_1(nums: List[int]) -> List[List[int]]:
    # Get all triplets
    combo3 = combinations(nums, 3)
    # Constraint 1: unique triplets
    list_tup3 = [tuple(i) for i in combo3]
    unique_tup3 = list(set(list_tup3))

    # Constraint 2: sum to 0
    list_t3_sum_zero = []
    for t3 in unique_tup3:
        if sum(t3) == 0:
            list_t3_sum_zero.append(t3)
    return list_t3_sum_zero


if __name__ == '__main__':
    nums1 = [0, 1, 1]
    out1 = sum3_1(nums1)
    print(out1)

    nums2 = [-1, 0, 1, 2, -1, -4]
    out2 = sum3_1(nums2)
    print(out2)
