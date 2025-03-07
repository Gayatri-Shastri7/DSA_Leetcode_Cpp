class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        if len(nums1) < len(nums2):
            nums1,nums2 = nums2,nums1
        res = []
        nums1 = sorted(nums1)
        nums2 = sorted(nums2)
        for i in nums2:
            l,r = 0,len(nums1)-1
            while l <=r:
                m = l+(r-l)//2
                if nums1[m] == i:
                    del nums1[m]
                    res.append(i)
                    break
                else:
                    if nums1[m] < i:
                        l = m + 1
                    else:
                        r = m - 1
        return res

        