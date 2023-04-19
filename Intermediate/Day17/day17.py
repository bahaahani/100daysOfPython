#day 17 quiz game using OOP

#mini tutorial

class User:
    
    def __init__(self,user_id,username):
        self.id = user_id
        self.username = username
        self.followers = 0
    def follow(self,user):
        user.followers += 1
        self.following += 1


user_1 = User("01","ali")
user_2 = User("123","bahaa")

user_1.follow(user_2)

