#attempt2:taking a string and not taking it
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr=[set(i) for i in arr if len(i)==len(set(i))]
        n=len(arr)
        maxi=0
        visited=[{""}]
        for i in range(n):
            k=len(visited)
            for j in range(k):
                if not(visited[j]&arr[i]):
                    visited.append(arr[i]|visited[j])
                    maxi=max(maxi,len(visited[-1])-1)
        return maxi

#attempt1:many TLEs
'''
class Solution:
    def maxLength(self, arr: List[str]) -> int:
        arr=[set(i) for i in arr if len(i)==len(set(i))]
        n=len(arr)
        def dfs(index,visited=set()):
            #print(arr[index])
            if index>=n:
                return 0
            if arr[index]&visited or index==n-1:
                if not(index):
                    return len(arr[index])
                if not(arr[index]&visited):
                    return len(visited|arr[index])
                return len(visited)
            maxi=0
            for i in range(index+1,n):
                maxi=max(maxi,dfs(i,visited|arr[index]))
            for i in range(index+1,n):
                maxi=max(maxi,dfs(i,visited))
            return maxi
        return dfs(0)
'''
