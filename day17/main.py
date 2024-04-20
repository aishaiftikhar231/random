# class User:
#     def __init__(self, user_id, username):
#         self.id =user_id
#         self.userid=username
#         self.follower=0
#         self.following=0
#
#     def follow(self,user):
#         user.follower+=1
#         self.following+=1
#
#
# user_1=User("009","angela")
# user_2=User("009","angela")
# print(user_1.id)
# user_1.follow(user_2)
# print(user_1.follower)
# print(user_1.following)
# print(user_2.follower)
# print(user_2.following)

import turtle as t
import random

tim = t.Turtle()
t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color



def draw_spirograph(size_of_gap):
    for _ in range(int(360 / size_of_gap)):
        tim.color(random_color())
        tim.circle(100)
        tim.setheading(tim.heading() + size_of_gap)

draw_spirograph(5)