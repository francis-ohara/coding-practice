"""Problem: returning a sorted union of 2 presorted lists, then find their sorted intersection using their union. (Can't use sets)"""


def sorted_union(nums1: list[int], nums2: list[int]):
    union = []

    ptr1 = 0
    ptr2 = 0

    while ptr1 < len(nums1) or ptr2 < len(nums2):
        if ptr1 > len(nums1) - 1:
            val1 = float("inf")
        else:
            val1 = nums1[ptr1]
        if ptr2 > len(nums2) - 1:
            val2 = float("inf")
        else:
            val2 = nums2[ptr2]

        if ptr1 == 0 and ptr2 == 0:
            if val1 < val2:
                union.append(val1)
                ptr1 += 1
            elif val1 > val2:
                union.append(val2)
                ptr2 += 1
            else:
                union.append(val1)
                ptr1 += 1
                ptr2 += 1
        else:
            if val1 == union[-1]:
                ptr1 += 1
                continue
            if val2 == union[-1]:
                ptr2 += 1
                continue
            if val1 < val2:
                union.append(val1)
                ptr1 += 1
            elif val1 > val2:
                union.append(val2)
                ptr2 += 1
            else:
                union.append(val1)
                ptr1 += 1
                ptr2 += 1
    return union


arr1 = [1, 2, 2, 3]
arr2 = [3, 3, 4, 4, 4, 7, 9]
print(sorted_union(arr1, arr2))

