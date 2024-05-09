from typing import List
import heapq


class Twitter:

    def __init__(self):
        self.follow_map = {}

        self.count = 0
        self.tweets = {}


    def postTweet(self, userId: int, tweetId: int) -> None:
        if userId not in self.tweets:
            self.tweets[userId] = []

        self.tweets[userId].append((-self.count, tweetId))
        self.count += 1


    def getNewsFeed(self, userId: int) -> List[int]:
        if userId in self.follow_map:
            followers = list(self.follow_map[userId])
        else:
            followers = []

        followers.append(userId)

        tweets_list = []

        for user in followers:
            if user in self.tweets:
                for post in self.tweets[user]:
                    heapq.heappush(tweets_list, post)
        
        followers = []
        for _ in range(10):
            if tweets_list:
                followers.append(heapq.heappop(tweets_list)[1])

        return followers


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId not in self.follow_map:
            self.follow_map[followerId] = set([])

        self.follow_map[followerId].add(followeeId)


    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followerId in self.follow_map and followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        



obj = Twitter()
obj.postTweet(1,4)
obj.postTweet(2,5)
obj.unfollow(1,2)
print(obj.getNewsFeed(1))