class Solution:
    def largestNumber(self, nums: List[int]) -> str:
        str_num = [str(num) for num in nums]
        len_num = len(str_num)

        for i in range(len_num):
            max_index = i
            for j in range(i+1,len_num):
                if str_num[max_index] + str_num[j] < str_num[j] + str_num[max_index]:
                    max_index = j
            if max_index != i:
                str_num[max_index],str_num[i] = str_num[i],str_num[max_index] 
        result = "".join(num for num in str_num)
        if result[0] == "0":
            return "0"
        return result
