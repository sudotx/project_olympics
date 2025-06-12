import random
import json
import os

# for project 2
JSON_FILE = "sorting_hat_data.json"

"""
      :::::::::  :::::::::   ::::::::  ::::::::::: :::::::::: :::::::: :::::::::::           ::::::::  :::     :::   :::  :::   :::   ::::::::: ::::::::::: ::::::::   :::::::: 
     :+:    :+: :+:    :+: :+:    :+:     :+:     :+:       :+:    :+:    :+:              :+:    :+: :+:     :+:   :+: :+:+: :+:+:  :+:    :+:    :+:    :+:    :+: :+:    :+: 
    +:+    +:+ +:+    +:+ +:+    +:+     +:+     +:+       +:+           +:+              +:+    +:+ +:+      +:+ +:+ +:+ +:+:+ +:+ +:+    +:+    +:+    +:+        +:+         
   +#++:++#+  +#++:++#:  +#+    +:+     +#+     +#++:++#  +#+           +#+              +#+    +:+ +#+       +#++:  +#+  +:+  +#+ +#++:++#+     +#+    +#+        +#++:++#++   
  +#+        +#+    +#+ +#+    +#+     +#+     +#+       +#+           +#+              +#+    +#+ +#+        +#+   +#+       +#+ +#+           +#+    +#+               +#+    
 #+#        #+#    #+# #+#    #+# #+# #+#     #+#       #+#    #+#    #+#              #+#    #+# #+#        #+#   #+#       #+# #+#           #+#    #+#    #+# #+#    #+#     
###        ###    ###  ########   #####      ########## ########     ###               ########  ########## ###   ###       ### ###       ########### ########   ########       
"""


def sorting_hat(cohort, houses):
    sorted_houses = {house: [] for house in houses}
    min_members = 4 if len(cohort) < len(houses) * 4 else 4

    for house in houses:
        for _ in range(min_members):
            if cohort:
                student = random.choice(cohort)
                sorted_houses[house].append(student)
                cohort.remove(student)

    for student in cohort:
        chosen_house = random.choice(houses)
        sorted_houses[chosen_house].append(student)

    return sorted_houses


def display_scoreboard(scores):
    print("\nCurrent Scoreboard:")
    sorted_scores = sorted(scores.items(), key=lambda x: x[1], reverse=True)
    for team, score in sorted_scores:
        print(f"{team}: {score}")


def add_score(scores):
    print("Available teams:")
    for index, team in enumerate(scores.keys(), 1):
        print(f"{index}. {team}")

    try:
        team_number = int(input("Enter team number to add score: "))
        if 1 <= team_number <= len(scores):
            team = list(scores.keys())[team_number - 1]
            points = int(input("Enter points to add: "))
            scores[team] += points
            print(f"Added {points} points to {team}")
        else:
            print("Invalid team number.")
    except ValueError:
        print("Invalid input. Please enter a number.")


def view_teams(sorted_houses):
    if sorted_houses:
        for house, students in sorted_houses.items():
            print(f"{house}: {students}")
    else:
        print("No students have been sorted yet.")


def save_data(sorted_houses, scores):
    data = {"sorted_houses": sorted_houses, "scores": scores}
    with open(JSON_FILE, "w") as f:
        json.dump(data, f)


def load_data():
    if os.path.exists(JSON_FILE):
        with open(JSON_FILE, "r") as f:
            data = json.load(f)
        return data["sorted_houses"], data["scores"]
    return None, None


def main_menu():
    """
    main menu for the program
    """
    # cohort = [
    #     "OhEhm471",
    #     "Alameenl2024",
    #     "olasco163",
    #     "Delight-dev123",
    #     "Wayne-ux0",
    #     "Abrahamalejowo",
    #     "Heis-him99",
    #     "Fakunlea1",
    #     "Saadski",
    #     "BakarTheWise",
    #     "yetty2020",
    #     "AradBee",
    #     "hee-sholar",
    #     "hope-stack",
    #     "emmanuel67-m",
    #     "drazdev365",
    #     "Kaycee449",
    #     "hee-sholar",
    #     "yetty2020",
    #     "khairahxx",
    #     "hope-stack",
    #     "AradBee",
    #     "UthmanHusain",
    #     "Olwanifemi-ja",
    # ]
    # houses = ["Team 1", "Team 2", "Team 3", "Team 4", "Team 5", "Team 6"]

    cohort = [
        "Olwanifemi-ja",
        "UthmanHusain",
        "khairahxx",
        "hee-sholar",
        "Loki-59",
        "Lovelyy-G",
        "Babiony",
        "Fegor"
    ]
    houses = ["Team 1", "Team 2"]

    # 1st 30
    # 2nd 20
    # 3rd 10

    # style 10
    # creativity 10
    # git 10
    # bonus 10

    sorted_houses, scores = load_data()
    if sorted_houses is None:
        sorted_houses = None
        scores = {house: 0 for house in houses}

    while True:
        print("\n1. Sort into groups")
        print("2. View scoreboard")
        print("3. View teams and members")
        print("4. Add scores to a team")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            if sorted_houses is None:
                sorted_houses = sorting_hat(cohort.copy(), houses)
                for house, members in sorted_houses.items():
                    print(f"\n{house}:")
                    for member in members:
                        print(f"  -> {member}")
                save_data(sorted_houses, scores)
            else:
                print("Already been sorted.")
        elif choice == "2":
            display_scoreboard(scores)
        elif choice == "3":
            view_teams(sorted_houses)
        elif choice == "4":
            add_score(scores)
            save_data(sorted_houses, scores)
        elif choice == "5":
            save_data(sorted_houses, scores)
            print("See ya")
            break
        else:
            print("Invalid choice. Please try again.")


if __name__ == "__main__":
    main_menu()
