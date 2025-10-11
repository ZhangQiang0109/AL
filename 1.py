class Solution:
    def twoSum(self,nums,target):
        seen = {} # key value存储下标、值
        for i,num in enumerate(nums):   # i是下标 num是值
            y = target - num
            if y in seen:
                return [seen[y],i]  # 返回y 的位置，num的位置,注意用[]括起来
            seen[num] = i   # 记录num出现的位置
        return []
    
solution = Solution()   # 创建实例
nums1 = [2,7,11,15]
target1 = 9
result1 = solution.twoSum(nums1,target1)
print("示例1的结果是:",result1)