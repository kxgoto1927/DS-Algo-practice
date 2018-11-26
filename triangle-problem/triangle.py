class Solution(object):
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """
        for i in range(len(triangle)-1,-1,-1):
            
            if i > 0:
                
                for j in range(1,len(triangle[i])):
                    if (triangle[i][j-1] + triangle[i-1][j-1]) < (triangle[i][j] + triangle[i-1][j-1]):
                        triangle[i-1][j-1] = triangle[i][j-1] + triangle[i-1][j-1]
                    else:
                        triangle[i-1][j-1] = triangle[i][j] + triangle[i-1][j-1]
        return triangle[0][0]



test = Solution()

triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

print(test.minimumTotal(triangle))