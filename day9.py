# Day 9

# Students grades
students_Scores = {
    "Bahaa": 99,
    "Muneera": 100,
    "Sara": 98,
    "Ahmed": 77,
    "Ali": 46,
    "Hussain": 85,
    "Hussam": 64,
}

for student in students_Scores:
    if students_Scores[student] > 90:
        print(f"{student} got an A")
        students_Scores[student] = "Outstanding"
    elif students_Scores[student] > 80:
        print(f"{student} got an B")
        students_Scores[student] = "Exceeds Expectations"
    elif students_Scores[student] > 70:
        print(f"{student} got an C")
        students_Scores[student] = "Acceptable"
    elif students_Scores[student] > 60:
        print(f"{student} got an D")
        students_Scores[student] = "Pass"
    else:
        print(f"{student} got an F")
        students_Scores[student] = "Fail"

print(students_Scores)

# Nesting
capitals = {
    "France": "Paris",
    "Germany": "Berlin",
}
# Nesting a List in a Dictionary
travel_log = {
    "France:": ["paris", "Lille", "Dijon"],
    "Germany:": ["Berlin", "Hamburg", "Stuttgart"],
}

capitals = {
    "France": ["Paris", "Lille", "Dijon"],
    "Germany": ["Berlin", "Hamburger", "Stuttgart"]
}
# Nesting Dictionary in a Dictionary
travel_log = {

    "France": {
        "cities_visited": ["paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    "Germany": {
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
}

travel_log = {
    "France": {
        "cities_Visited": ["Berlin", "hamburger", "stuttgart"],
        "total_visits": 5,
    },
}

# Nesting Dictionaries in Lists
travel_log = [
    {
        "country": "France",
        "cities_visited": ["paris", "Lille", "Dijon"],
        "total_visits": 12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburg", "Stuttgart"],
        "total_visits": 5,
    },
]

travel_log = [
    {
        "country": "France",
        "cities_visited": ["paris", "Lilly", "Django"],
        "total_visits":12,
    },
    {
        "country": "Germany",
        "cities_visited": ["Berlin", "Hamburger", "stgattugart"],
        "total_visits":5,
    },
]


# Silent Auction Program
logo = '''
                         ___________
                         \         /
                          )_______(
                          |"""""""|_.-._,.---------.,_.-._
                          |       | | |               | | ''-.
                          |       |_| |_             _| |_..-'
                          |_______| '-' `'---------'` '-'
                          )"""""""(
                         /_________\\
                       .-------------.
                      /_______________\\
'''

print(logo)
isContinue = True
bid_dictionary = {
    "name": 0,
}


def find_highest_bidder(bids_dictionary):
    maxbid = 0
    for person in bid_dictionary:
        if bid_dictionary[person] > maxBid:
            maxBid = bid_dictionary[person]
    print(f"the highest bidder is {maxBid}")


while isContinue:
    name = input("Enter your name")
    bid_dictionary[name] = input("Input your bid")

    result = input(
        "Do you want to add more bids Say 'yes' to continue or 'No' to exit")
    if result == "no":
        break
find_highest_bidder(bids_dictionary=bid_dictionary)
print(bid_dictionary)
