#better answer: If you have maxfreq, some elements would have
#0<=elefrequency<=maxfrequency. No need of heap
'''
from collections import Counter, defaultdict
class FreqStack:

    def __init__(self):
        self.maxFreq = 0
        self.freqMapper = defaultdict(list)
        self.c = Counter()

    def push(self, x: int) -> None:
        self.c[x] += 1
        if self.c[x] > self.maxFreq:
            self.maxFreq = self.c[x]
        self.freqMapper[self.c[x]].append(x)
    def pop(self) -> int:
        x = self.freqMapper[self.maxFreq].pop()
        if len(self.freqMapper[self.maxFreq]) == 0:
            self.maxFreq -= 1
        self.c[x] -= 1
        return x
'''

#attempt2:
from heapq import heappush,heappop
class FreqStack:

    def __init__(self):
        self.eles={}#holds the elements and their counts
        self.freq={}#delete the element from previous frequency and add to new frequency
        self.freqarr=[0]#heap which holds the sorted frequencies for easy popping
        
    def push(self, x: int) -> None:
        if x not in self.eles:
            self.eles[x]=0
            self.freq[0]=[x]
            self.freqarr.append(0)
        #self.freqarr.remove(-self.eles[x])
        self.eles[x]+=1
        if self.eles[x] not in self.freq:
            self.freq[self.eles[x]]=[]
        self.freq[self.eles[x]].append(x)
        heappush(self.freqarr,-self.eles[x])
        #print(self.eles,self.freq,self.freqarr)

    def pop(self) -> int:
        freq_to_pop=-1*heappop(self.freqarr)
        #print(freq_to_pop)
        self.eles[self.freq[freq_to_pop][-1]]-=1
        #heappush(self.freqarr,-1*self.eles[self.freq[freq_to_pop][-1]])
        return self.freq[freq_to_pop].pop()

#attempt1: WA Dont know why
'''
from heapq import heappush,heappop
class FreqStack:

    def __init__(self):
        self.eles={}#holds the elements and their counts
        self.freq={}#delete the element from previous frequency and add to new frequency
        self.freqarr=[0]#heap which holds the sorted frequencies for easy popping
        
    def push(self, x: int) -> None:
        if x not in self.eles:
            self.eles[x]=0
            self.freq[0]=[x]
            self.freqarr.append(0)
        #self.freqarr.remove(-self.eles[x])
        self.eles[x]+=1
        if self.eles[x] not in self.freq:
            self.freq[self.eles[x]]=[]
        self.freq[self.eles[x]].append(x)
        heappush(self.freqarr,-self.eles[x])
        #print(self.eles,self.freq,self.freqarr)

    def pop(self) -> int:
        freq_to_pop=-1*heappop(self.freqarr)
        #print(freq_to_pop)
        self.eles[self.freq[freq_to_pop][-1]]-=1
        #heappush(self.freqarr,-1*self.eles[self.freq[freq_to_pop][-1]])
        return self.freq[freq_to_pop].pop()
        


# Your FreqStack object will be instantiated and called as such:
# obj = FreqStack()
# obj.push(x)
# param_2 = obj.pop()
'''
