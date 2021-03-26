#attempt1:for k==1, we can have rotation and take the minimum of that
#else: it is sorted(S) because any two adjacent places can be swapped and hence
#on rotation, it is always possible to get sorted(S)
class Solution:
    def orderlyQueue(self, S: str, K: int) -> str:
        if K==1:
            return min(S[i:]+S[:i] for i in range(len(S)))
        return "".join(sorted(S))
