#attempt1: TOOK HELP Utterly clueless
class Solution:
    def sumOfDistancesInTree(self, n: int, edges: List[List[int]]) -> List[int]:
        graph={}
        if n==1:
            return [0]
        for u,v in edges:
            if u not in graph:
                graph[u]=set()
            if v not in graph:
                graph[v]=set()
            graph[u].add(v)
            graph[v].add(u)
        
        count=[1]*n
        sum_sub_tree=[0]*n
        def initdfs(root,parent):
            for child in graph[root]:
                if child!=parent:
                    initdfs(child,root)
                    count[root]+=count[child]
                    sum_sub_tree[root]+=sum_sub_tree[child]+count[child]
        initdfs(0,-1)
        ans=[0]*n
        ans[0]=sum_sub_tree[0]
        def dfsfinal(root,parent):
            for child in graph[root]:
                if child!=parent:
                    ans[child]=ans[root]-count[child]+n-count[child]
                    dfsfinal(child,root)
        dfsfinal(0,-1)
        #print(count)
        #print(sum_sub_tree)
        return ans
        