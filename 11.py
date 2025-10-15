class Solution:
    def maxArea(self,height):
        """
        11.盛最多水的容器
        """
        left = 0
        right = len(height)-1   # 指向数组的最后一个下标
        ans = 0     # 初始化答案
        while left < right:     # 两个指针没有相遇
            area = (right-left) * min(height[left],height[right])   # 构成面积
            ans = max(ans,area) #更新答案最大值
            if height[left] < height[right]:    #左边矮
                left += 1   # 把左边去掉，向右移动（哪边短移动哪边）
            else:
                right -= 1
        return ans
# 时间复杂度 O(n)
# 空间复杂度 O(1)

solution = Solution()   # 实例

test1 = [1,8,6,2,5,4,8,3,7]
result1 = solution.maxArea(test1)

test2 = [1,1]
result2 = solution.maxArea(test2)

print("测试1的结果为: ",result1)
print("测试2的结果为: ",result2)

        