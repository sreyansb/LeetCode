#attempt1: Idea is simple: Find the root and each node on the left and each node
#on the right can be potential subtrees ka root
#I did misjudge the question thinking that we had to serialize it
#but no

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        numbers=list(range(1,n+1))
        @lru_cache(None)
        def createtree(start,end):
            if start>end:
                return [None]
            ans=[]
            for i in range(start,end+1):
                ansleft=createtree(start,i-1)
                ansright=createtree(i+1,end)
                for lst in ansleft:
                    for rst in ansright:
                        temp=TreeNode(numbers[i])
                        temp.left=lst
                        temp.right=rst
                        ans.append(temp)
            return ans
        return createtree(0,n-1)
                
            
            
            