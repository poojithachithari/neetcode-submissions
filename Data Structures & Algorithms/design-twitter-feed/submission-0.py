class Twitter:

    def __init__(self):
        self.tweets = {}
        self.following = {}
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []
        self.tweets[userId].append((self.time,tweetId))
        self.time += 1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        followers= self.following.get(userId,set())
        followers.add(userId)

        for uid in followers:
            if uid in self.tweets:
                for t, tid in self.tweets[uid][-10:]:
                    heapq.heappush(heap,(-t,tid))
        feed = []
        while heap and len(feed)<10:
            feed.append(heapq.heappop(heap)[1])
        return feed


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId == followeeId:
            return
        if followerId not in self.following:
            self.following[followerId] = set()
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.following:
            self.following[followerId].discard(followeeId)
        
