class Solution:
    def trap(self,height):
        """
        42.接雨水
        """
        n =len(height)
        ans = 0
        left = 0
        right = n -1
        pre_max = suf_max = 0
        while left < right:
            pre_max = max(pre_max,height[left])
            suf_max = max(suf_max,height[right])
            if pre_max < suf_max:
                ans += pre_max - height[left]
                left += 1
            else:
                ans += suf_max - height[right]
                right -= 1
        return ans
solution = Solution()

test1= [0,1,0,2,1,0,1,3,2,1,2,1]
test2 = [4,2,0,3,2,5]
result1 = solution.trap(test1)
result2 = solution.trap(test2)
print("测试1的结果为: ",result1)
print("测试2的结果为: ",result2)

# class Solution:
#     def trap(self, height: List[int]) -> int:
#         n = len(height) # 数组长度
#         pre_max = [0] * n    # 创建大小为n数组，记录前缀最大值
#         pre_max[0] = height[0]  
#         for i in range(1,n):
#             pre_max[i] = max(pre_max[i-1],height[i])    # 上一个前缀最大值与当前高度 取最大值
#         suf_max = [0] * n
#         suf_max[-1] = height[-1]    # 最后一项等于数组最后一项
#         for i in range(n-2, -1, -1):
#             suf_max[i] = max(suf_max[i+1],height[i])

#         ans = 0 
#         for h,pre,suf in zip(height,pre_max,suf_max):
#             ans += min(pre,suf) - h
#         return ans
# # 时间复杂度 O(n)
# # 空间复杂度 O(n)

