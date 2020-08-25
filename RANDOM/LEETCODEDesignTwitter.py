from heapq import heapify,heappush,heappop,nsmallest
class userclass:
    def __init__(self):
        self.tweets=[]
        self.friends=set()

class Twitter:
    
    def __init__(self):
        self.users={}     
        self.time=0
        
    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.users:
            self.users[userId]=userclass()
            self.users[userId].friends.add(userId)
        heappush(self.users[userId].tweets,(self.time,tweetId))
        self.time-=1
        #print(self.users)
        
    def getNewsFeed(self, userId: int) -> List[int]:
        l=[]
        if userId in self.users:
            for i in self.users[userId].friends:
                l+=self.users[i].tweets
            if userId not in self.users[userId].friends:
                l+=self.users[userId].tweets
            heapify(l)
            k= nsmallest(min(10,len(l)),l)
            return [i[1] for i in k]         
        else:
            return []
        

    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.users:
            self.users[followerId]=userclass()
            self.users[followerId].friends.add(followerId)
        if followeeId not in self.users:
            self.users[followeeId]=userclass()
            self.users[followeeId].friends.add(followeeId)
        self.users[followerId].friends.add(followeeId)  

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.users:
            if followeeId in self.users[followerId].friends:
                self.users[followerId].friends.remove(followeeId)
        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
