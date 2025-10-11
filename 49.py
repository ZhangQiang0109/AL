class Solution:
    def groupAnagrams(self,strs):
        """字母异位词分组"""
        d = {}
        for word in strs:
            s = ''.join(sorted(word))
            if s in d:
                d[s].append(word)   # s d word是变量
            else:
                d[s] = [word]
        
        return list(d.values())

solution = Solution() # 添加括号创建实例
test = ['eat','tea','tan','ate','nat','bat']
result = solution.groupAnagrams(test)
print("测试1的结果为: ", result)
