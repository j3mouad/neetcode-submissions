class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        ZeroLocation = -1
        product = 1
        for idx, num in enumerate(nums):
            if num == 0 and ZeroLocation == -1  :
                ZeroLocation = idx
            elif num == 0 and ZeroLocation >= 0:
                return [0]*len(nums)
            else:
                product *= num
        if ZeroLocation >= 0:
            products = [0]*len(nums)
            products[ZeroLocation] = product
        else:
            products = [product]*len(nums)
            for idx, num in enumerate(nums):
                products[idx] //= num
        return products
