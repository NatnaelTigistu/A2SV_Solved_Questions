class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums)-1
        if(len(nums)==1):
            return nums[0]
        while low<=high:
            mid = (low+high)//2
            if(mid>low and mid<high):
                if(nums[mid-1]<nums[mid] and nums[mid+1]<nums[mid]):
                    return nums[mid+1]
                elif(nums[mid-1]>nums[mid] and nums[mid+1]>nums[mid]):
                    return nums[mid]
                else:
                    if(nums[high]>nums[low]):
                        return nums[low]
                    else:
                        if(nums[mid]>nums[high]):
                            low = mid+1
                        else:
                            high = mid-1
            else:
                if(nums[high]>nums[low]):
                    return nums[low]
                else:
                    return nums[high]