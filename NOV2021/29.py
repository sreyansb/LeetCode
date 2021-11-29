#attempt1: DFS on email
class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        di_emails = {}
        connected_emails = {}
        n = len(accounts)
        for i in range(n):
            #di_name[i] = set(accounts[i][1:])
            for email in accounts[i][1:]:
                di_emails[email] = accounts[i][0]
                if email not in connected_emails:
                    connected_emails[email] = set()
                for rel_email in accounts[i][1:]:
                    if rel_email != email:
                        connected_emails[email].add(rel_email)
        ans = []
        
        def dfs(email,visited):
            visited.add(email)
            for i in connected_emails[email]:
                if i not in visited:
                    dfs(i,visited)
        
        allvisited = set()
        for i in connected_emails:
            if i not in allvisited:
                visited = set()
                dfs(i,visited)
                allvisited = allvisited|visited
                ans.append([di_emails[i]]+sorted(visited))
        return ans

