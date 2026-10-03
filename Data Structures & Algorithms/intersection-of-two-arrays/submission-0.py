class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        #initalize two pointers one for nums1 and nums2 
        set1 = set(nums1) #(1,2)
        set2 = set(nums2) #(2,2)

        rest = []
        for num in set1:
            if num in set2:
                rest.append(num)
        return rest

        


        