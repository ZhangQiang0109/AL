class Solution:
    def longestConsecutive(self,nums):
        """
        最长连续序列
        要求时间复杂度为O(n)
        """
        st = set(nums)  # 把nums转成哈希集合
        ans = 0
        for x in st:  # 遍历哈希集合
            if x-1 in st:   #如果x不是序列的起点，直接跳过
                continue
            # x是序列的起点
            y = x + 1
            while y in st:
                y += 1
            # 循环结束，y-1是最后一个在哈希集合中的数
            ans = max(ans, y-x)
        return ans



solution = Solution()   # 创建实例


test1 = [100,4,200,1,3,2]
result = solution.longestConsecutive(test1)
print("测试1的结果为: ",result)

test2 = [0,3,7,2,5,8,4,6,0,1]
result = solution.longestConsecutive(test2)
print("测试2的结果为: ",result)

test3= [1,0,1,2]
result = solution.longestConsecutive(test3)
print("测试3的结果为: ",result)