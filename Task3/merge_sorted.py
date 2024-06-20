def merge_arrays(nums1, nums2, n1, n2):
    nums3 = nums1[:n1] + nums2[:n2]
    nums3.sort()
    return nums3

# Driver code
if __name__ == "__main__":
    nums1 = [2,4,6]
    nums2 = [1,3,5]
    n1 = len(nums1)
    n2 = len(nums2)

    nums3 = merge_arrays(nums1, nums2, n1, n2)

    print(*nums3)

