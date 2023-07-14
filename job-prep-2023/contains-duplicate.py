from typing import List


def contains_duplicate1(nums: List[int]) -> bool:
    unique_values = []
    for n in nums:
        if n in unique_values:
            return True
        else:
            unique_values.append(n)
    return False

if __name__ == '__main__':
    nums = [1,2,3,1]
    out1 = contains_duplicate1(nums)
    print(f"Got test1 right: {out1 == True}")

    nums = [1,2,3,4]
    out2 = contains_duplicate1(nums)
    print(f"Got test2 right: {out2 == False}")
