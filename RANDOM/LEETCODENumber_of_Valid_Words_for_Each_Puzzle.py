#attempt3: TOOK HINT
#Approach :
#Create words into buckets with each buckets signalling the sorted sequence for
#set of characters of a word.
#Then for each element of the powerset of the puzzle, search for it in
#the buckets and add the answers
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        #<=7 otherwise not present in puzzle according to constraints
        words = [sorted(set(i)) for i in words if len(set(i))<=7]
        buckets = {}
        for i in words:
            word = "".join(i)
            if word not in buckets:
                buckets[word] = 0
            buckets[word] += 1
        ans = [0 for i in range(len(puzzles))]
        for i in range(len(puzzles)):
            firstch = puzzles[i][0]
            puzzle = "".join(sorted(puzzles[i][1:]))
            lenp = len(puzzle)
            for p in range(1<<lenp):
                permute = bin(p)[2:]
                permute = "0"*(lenp-len(permute)) + permute
                permute = "".join(sorted([puzzle[i] for i in range(lenp) if permute[i]=="1"] + [firstch]))
                ans[i] += buckets[permute] if permute in buckets else 0
        return ans

#attempt1 and 2: TLE:
#Approach was to for each puzzle ka each character keep the indices as a set
#Then for each word's each character check the intersection of the sets
#for the first constraint in each of the found puzzle indices check if the given
#word contains the first letter of the puzzle
'''
class Solution:
    def findNumOfValidWords(self, words: List[str], puzzles: List[str]) -> List[int]:
        di = {}
        for i in "qwertyuiopasdfghjklzxvcbnm":
            di[i] = set()
        for index in range(len(puzzles)):
            puzzle = puzzles[index]
            for char in puzzle:
                di[char].add(index)
        ans = [0 for i in range(len(puzzles))]
        for index in range(len(words)):
            word = words[index]
            ansh = di[word[0]]
            i = 1
            word = set(word)
            for i in word:
                ansh = ansh & di[i]
            for puzindex in ansh:
                if puzzles[puzindex][0] in word:
                    ans[puzindex] += 1
        return ans
'''
