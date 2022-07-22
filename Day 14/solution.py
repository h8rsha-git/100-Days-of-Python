# all import at once
import click
from art import logo,vs
import random
from game_data import data

# helper functions
def get_celeb_a():
  return random.choice(data)

def get_celeb_b(celeb_a):
  b = random.choice(data)
  while b == a:
    b = random.choice(data)
  return b
  
def get_data(celeb):
  return f"{celeb['name']}, {celeb['description']}, from {celeb['country']}. "

def get_answer(celeb_a_followers, celeb_b_followers):
  if celeb_a_followers > celeb_b_followers:
    return 'A'
  else:
    return 'B'

def get_followers(celeb):
  return celeb['follower_count']

def get_logo():
  click.clear()
  print(logo)

def get_comparison_info(celeb_a, celeb_b):
  print(f"Compare A: {get_data(celeb_a)}")
  print(vs)
  print(f"Against B: {get_data(celeb_b)}")
  
# main logic
score = 0

a = get_celeb_a()
b = get_celeb_b(a)

game_over = False

while not game_over:
  get_logo()
  if score > 0:
    print(f"You are right! Current score: {score}")
  get_comparison_info(a,b)

  a_followers = get_followers(a)
  b_followers = get_followers(b)

  # input user answer, compare values, update a and b
  correct_answer = get_answer(a_followers, b_followers)
  user_answer = input("Who has more followers? Type 'A' or 'B': ")
  
  if correct_answer == user_answer:
    score += 1
    a = b
    b = get_celeb_b(a)
  else:
    get_logo()
    game_over = True
    print(f"Sorry, that's wrong. Final score: {score}")