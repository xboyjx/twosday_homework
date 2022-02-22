users = {
  "Jonathan": {
    "twitter": "jonnyt",
    "lottery_numbers": [6, 12, 49, 33, 45, 20],
    "home_town": "Stirling",
    "pets": [
    {
      "name": "fluffy",
      "species": "cat"
    },
    {
      "name": "fido",
      "species": "dog"
    },
    {
      "name": "spike",
      "species": "dog"
    }
  ]
  },
  "Erik": {
    "twitter": "eriksf",
    "lottery_numbers": [18, 34, 8, 11, 24],
    "home_town": "Linlithgow",
    "pets": [
    {
      "name": "nemo",
      "species": "fish"
    },
    {
      "name": "kevin",
      "species": "fish"
    },
    {
      "name": "spike",
      "species": "dog"
    },
    {
      "name": "rupert",
      "species": "parrot"
    }
  ]
  },
  "Avril": {
    "twitter": "bridgpally",
    "lottery_numbers": [12, 14, 33, 38, 9, 25],
    "home_town": "Dunbar",
    "pets": [
      {
        "name": "monty",
        "species": "snake"
      }
    ]
  }
}

# 1. Get Jonathan's Twitter handle (i.e. the string `"jonnyt"`)
jonathan_twitter_handle = users["Jonathan"]["twitter"]
print(jonathan_twitter_handle)
# 2. Get Erik's hometown
erik_hometown = users["Erik"]["home_town"]
# 3. Get the array of Erik's lottery numbers
erik_lottery_nos = users["Erik"]["lottery_numbers"]
print(erik_lottery_nos)
# 4. Get the species of Avril's pet Monty
avril_pet_species = users["Avril"]["pets"][0]["species"]
print(avril_pet_species)
# 5. Get the smallest of Erik's lottery numbers
erik_smallest_lotto_no = min(erik_lottery_nos)
print(erik_smallest_lotto_no)
# 6. Return an array of Avril's lottery numbers that are even
avril_lotto_nos = users["Avril"]["lottery_numbers"]
avril_even_lotto_nos = []
for number in avril_lotto_nos:
  if number % 2 == 0:
    avril_even_lotto_nos.append(number)



# 7. Erik is one lottery number short! Add the number `7` to be included in his lottery numbers
users["Erik"]["lottery_numbers"].append(7)

# 8. Change Erik's hometown to Edinburgh
users["Erik"]["home_town"] = "Edinburgh"

# 9. Add a pet dog to Erik called "Fluffy"
fluffy_dog = {"name": "fluffy", "species":"dog"}
users["Erik"]["pets"].append(fluffy_dog)
print(users["Erik"]["pets"])
# 10. Add another person to the users dictionary
users["Jacob"] = 0
print(users)