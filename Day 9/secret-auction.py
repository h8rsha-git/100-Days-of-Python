from replit import clear
#HINT: You can call clear() to clear the output in the console.
import art

print(art.logo)

print("Welcome to the secret auction program.")

bid_done = False
winner_dict = {"name": "No Winner", "bid": 0}

while not bid_done:
  name = input("What is your name?: ")
  bid = int(input("What's your bid?: $"))
  if winner_dict["bid"] < bid:
    winner_dict["name"] = name
    winner_dict["bid"] = bid
  others = input("Are there any other bidders? Type 'yes' or 'no'.\n")
  if others == "yes":
    clear()
  else:
    bid_done = True

#print(participants)
print(f"The winner is {winner_dict['name']} with a bid of ${winner_dict['bid']}.")