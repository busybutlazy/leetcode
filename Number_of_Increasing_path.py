class Solution(object):
    def countPaths(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        

cp=Solution().countPaths

grids = [[[1,1],[3,4]],[[1],[2]]]

for g in grids:
    print(cp(g))