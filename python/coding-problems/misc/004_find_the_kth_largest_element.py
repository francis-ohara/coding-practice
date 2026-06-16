# https://www.youtube.com/watch?v=AdG_3GRDUfI

def get_kth_largest(nums: list[int], k: int) -> int:
    sorted_nums = list(sorted(nums, reverse=True))
    return sorted_nums[k-1]


print(get_kth_largest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4))
