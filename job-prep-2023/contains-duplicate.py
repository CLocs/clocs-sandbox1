from typing import List


def contains_duplicate1(nums: List[int]) -> bool:
    unique_values = []
    for n in nums:
        if n in unique_values:
            return True
        else:
            unique_values.append(n)
    return False


def contains_duplicates2(nums: List[int]) -> bool:
    for i in range(len(nums)):
        n = nums.pop()
        if n in nums:
            return True
    return False


def contains_duplicates3(nums: List[int]) -> bool:
    unique = set()
    for i in nums:
        if i in unique:
            return True
        else:
            unique.add(i)
    return False


def contains_duplicates4(nums: List[int]) -> bool:
    uniques = set(nums)
    if len(uniques) != len(nums):
        return True
    else:
        return False


def contains_duplicates5(nums: List[int]) -> bool:
    return len(set(nums)) != len(nums)


if __name__ == '__main__':
    nums1 = [1, 2, 3, 1]
    out1 = contains_duplicate1(nums1)
    print(f"Got test1 right: {out1 == True}")

    nums2 = [1, 2, 3, 4]
    out2 = contains_duplicate1(nums2)
    print(f"Got test2 right: {out2 == False}")
