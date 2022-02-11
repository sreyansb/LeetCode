#attempt1:
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s1 = {}
        count_s2 = {}
        len_s1 = len(s1)
        len_s2 = len(s2)
        for i in s1:
            if i not in count_s1:
                count_s1[i] = 0
            count_s1[i] += 1
        if len_s1>len_s2:
            return False
        for i in range(len_s1):
            if s2[i] not in count_s2:
                count_s2[s2[i]] = 0
            count_s2[s2[i]] += 1
        if count_s1 == count_s2:
            return True
        for i in range(len_s1,len_s2):
            chartodel = s2[i-len_s1]
            if count_s2[chartodel] == 1:
                del count_s2[chartodel]
            else:
                count_s2[chartodel] -= 1
            chartouse = s2[i]
            if chartouse not in count_s2:
                count_s2[chartouse] = 0
            count_s2[chartouse] += 1
            if count_s2 == count_s1:
                return True
        return False
            
