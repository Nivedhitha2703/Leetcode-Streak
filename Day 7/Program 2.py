class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:

        # Merge the two lists
        new_lst = nums1 + nums2

        # Sort the merged list
        new_lst.sort()

        # Find total length
        length = len(new_lst)

        # Find middle index
        mid = length // 2

        # If length is odd
        if length % 2 == 1:
            return float(new_lst[mid])

        # If length is even
        else:
            return (new_lst[mid - 1] + new_lst[mid]) / 2
