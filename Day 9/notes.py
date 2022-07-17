# Dictionary

programming_dictionary = {
  "Bug": "An error in a program that prevents the program from running as expected.", 
  "Function": "A piece of code that you can easily call over and over again."
}

# Retrieving items from dictionary 
print(programming_dictionary["Bug"])

# Adding new items to dictionary
programming_dictionary["Loop"] = "The action of doing something over and over again"

print(programming_dictionary)

# Wipe an existing dictionary
# programming_dictionary = {}
# print(programming_dictionary)

# Edit an item in dictionary
programming_dictionary["Bug"] = "A moth in your computer"
print(programming_dictionary)

# Loop through a dictionary
for key in programming_dictionary:
  print(key) # just gives you the keys
  print(f"{key} : {programming_dictionary[key]}")

#----------------------------------------------------------------
  
# Nesting
  
capitals = {
  "France": "Paris",
  "Germany": "Berlin"
}

# Nesting a list in dictionary
travel_log_1 ={
  "France": ["Paris", "Lillie", "Dijon"],
  "Germany": ["Berlin", "Hamburg"]
}

["A", "B", ["C", "D"]]

# Nesting Dictionary in Dictionary
travel_log_2 ={
  "France": {
    "cities_visited" : ["Paris", "Lillie", "Dijon"],
    "total_visits": 12
  },
  "Germany": {
    "cities_visited" : ["Berlin", "Hamburg"],
    "total_visits": 5
  }
}

# Nesting Dictionary in list
travel_log_3 =[
  {
    "country": "France", 
    "cities_visited" : ["Paris", "Lillie", "Dijon"],
    "total_visits": 12
  },
  {
    "country": "Germany",
    "cities_visited" : ["Berlin", "Hamburg"],
    "total_visits": 5
  }
]
