class User:
    def __init__(self, user_id, username,):
        self.user_id = user_id
        self.username = username
        self.followers = 0
        self.following = 0

    def follow(self, user):
        user.followers+=1
        user.following+=1



user1 = User(1, 'John')
user2 = User(2, 'Mary')
user1.follow(user2)
print(user1.followers)
print(user2.followers)
