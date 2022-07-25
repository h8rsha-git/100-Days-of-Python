# class -> blueprint for creating objects
# name for classes -> PascalCase

class User:
    # all functions require "self" parameter

    def __init__(self, id, username):
        print("New user created")
        self.id = id
        self.username = username
        # providing default values
        self.followers = 0
        self.following = 0

    def follow(self,user):
        user.followers += 1
        self.following += 1


# creating attributes manually -> prone to error
user_1 = User("001","angela")
user_2 = User("002","harsha")
print(user_2.username)

user_1.follow(user_2)
print(user_1.followers)
print(user_1.following)
print(user_2.followers)
print(user_2.following)

