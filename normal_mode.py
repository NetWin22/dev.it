import os
import sys
import subprocess
import random

balance = 0
username = "User"
company_name = "Company"
last_game_name = ""
last_game_price = 0
last_game_earnings = 0
last_game_sold = 0
last_game_rating = 0.0
year = 1997
fans = 0
level = 0.1
balance_text = "0"
developers = 1
month_next = 0
month = 0
month_text = "January"

os.system('cls' if os.name == 'nt' else 'clear')
print ("Welcome to Dev.it! before starting this adventure, please write here your name!")
print("")
username = input()
os.system('cls' if os.name == 'nt' else 'clear')
print(f"Great {username}! What about the name of your company?")
print("")
company_name = input()
os.system('cls' if os.name == 'nt' else 'clear')
print("I love that! Okay, then I think you are ready to start, enjoy the game!")
print("A wait, before I go, how many money you want to start with?")
print("---")
print("1.  $50.000")
print("2.  $75.000")
print("3.  $100.000")
print("")

while True:
    try:
        balance_choice = int(input())
    except ValueError:
        print("Use a number")
        continue
        
    if balance_choice == 1:
        balance = 50000
        break
    elif balance_choice == 2:
        balance = 75000
        break
    elif balance_choice == 3:
        balance = 100000
        break
    else:
        print("Invalid choice, please retry.")

def ui_refresh():
    global fans
    os.system('cls' if os.name == 'nt' else 'clear')
    fans = int(fans)
    print(f"Balance: ${balance_text}     Developers: {developers}     Company Name: {company_name}     Fans: {fans}     Year: {year}     Month: {month}     Level: {level * 10}")
    print("---")
    print("History Log:")
    print("")

def hire_dev():
    global balance, level, developers, month, history
    ui_refresh()
    base_cost = 5000
    developer_cost = base_cost * (1 + developers * 0.2)
    developer_cost *= random.uniform(0.9, 1.1)
    developer_cost = round(developer_cost, 2)
    dev_cost_text = f"{developer_cost:,}".replace(",",".")
    print(f"The new developer will cost you ${developer_cost}. Want to hire him?")
    print("[Y/N]")
    choice = input()
    if choice == "Y" or choice == "y":
        balance -= developer_cost
        developers += 1
        month += 1
        history += f"\nYou hired a developer for ${developer_cost}."
    else:
        print("Okay :)")

def new_game():
    global last_game_name, last_game_price, balance
    global last_game_sold, last_game_earnings, last_game_rating
    global year, level, developers, month, fans, history
    ui_refresh()
    game_name = input("Game Name?:\n").strip()
    if not game_name:
        game_name = "Untitled Game"
    while True:
        try:
            game_price = int(input("\nPrice per copy ($)?\n"))
            if game_price <= 0:
                print("Price must be greater than 0.")
                continue
            break
        except ValueError:
            print("Use a number.")
            
    while True:
        try:
            budget = int(input("\nDevelopment budget ($)?\n"))
            if budget < 0:
                print("Budget cannot be negative.")
                continue
            if budget > balance:
                print("You cannot spend more than your current balance.")
                continue
            break
        except ValueError:
            print("Use a number.")

    engines = {
        2: ("Robot Engine", 0, 0.80),
        3: ("Kodaku Engine", 150, 1.00),
        4: ("Real Engine", 300, 1.20)
    }

    print("\nEngine?\n1. Custom One (Not available yet)"
          "\n2. Robot Engine | $0"
          "\n3. Kodaku Engine | $150"
          "\n4. Real Engine | $300")

    while True:
        try:
            choice = int(input())
            if choice == 1:
                print("You haven't developed this engine yet!")
            elif choice in engines:
                engine_name, engine_cost, engine_quality = engines[choice]
                break
            else:
                print("Invalid choice.")
        except ValueError:
            print("Use a number.")
    genres = {
        1: ("Adventure", 1.05),
        2: ("Mystery", 1.00),
        3: ("Horror", 1.10),
        4: ("Shooter", 1.10),
        5: ("Driving", 1.00),
        6: ("Simulator", 0.95),
        7: ("Sandbox", 1.10),
        8: ("RPG", 1.10)
    }

    print("\nGenre?")
    for key, value in genres.items():
        print(f"{key}. {value[0]}")

    while True:
        try:
            choice = int(input())
            if choice in genres:
                genre_name, genre_factor = genres[choice]
                break
            print("Invalid choice.")
        except ValueError:
            print("Use a number.")

    styles = {
        1: ("2D", 0.95),
        2: ("2D Top-Down", 1.00),
        3: ("3D", 1.15),
        4: ("Textual", 0.85)
    }

    print("\nStyle?\n1. 2D\n2. 2D Top-Down\n3. 3D\n4. Textual")

    while True:
        try:
            choice = int(input())
            if choice in styles:
                style_name, style_factor = styles[choice]
                break
            print("Invalid choice.")
        except ValueError:
            print("Use a number.")

    devices = {
        1: ("PC", 400, 1.15),
        2: ("PolyStation", 800, 1.00),
        3: ("Ycircle", 600, 1.05),
        4: ("Nendo", 450, 1.10)
    }

    print("\nDevice?\n1. PC | $400"
          "\n2. PolyStation | $800"
          "\n3. Ycircle | $600"
          "\n4. Nendo | $450")

    while True:
        try:
            choice = int(input())
            if choice in devices:
                device_name, device_cost, device_factor = devices[choice]
                break
            print("Invalid choice.")
        except ValueError:
            print("Use a number.")
    total_cost = budget + engine_cost + device_cost
    if total_cost > balance:
        print(f"\nYou need ${total_cost:,.0f}, but only have "
              f"${balance:,.0f}. Game cancelled.")
        return
        
    budget_quality = min(2.0, (max(budget, 0) / 10000) ** 0.5)
    team_quality = 1 + min(developers, 10) * 0.04
    experience = 1 + min(level, 10) * 0.03
    synergy = 1.0

    if genre_name == "RPG" and style_name in ("2D", "2D Top-Down"):
        synergy = 1.20
    elif genre_name == "Shooter" and style_name == "3D":
        synergy = 1.25
    elif genre_name == "Driving" and style_name == "3D":
        synergy = 1.25
    elif genre_name == "Horror" and style_name in ("2D", "3D"):
        synergy = 1.10
    elif genre_name == "Mystery" and style_name == "Textual":
        synergy = 1.25
    elif genre_name == "Sandbox" and style_name == "3D":
        synergy = 1.20
    elif genre_name == "Simulator" and style_name == "3D":
        synergy = 1.15
    platform_synergy = 1.0

    if device_name == "PC" and style_name == "Textual":
        platform_synergy = 1.20
    elif device_name == "PC" and style_name == "3D":
        platform_synergy = 1.10
    elif device_name == "PolyStation" and style_name == "3D":
        platform_synergy = 1.15
    elif device_name == "Ycircle" and style_name == "2D":
        platform_synergy = 1.15
    elif device_name == "Nendo" and style_name == "2D Top-Down":
        platform_synergy = 1.15
    quality = (budget_quality * engine_quality * genre_factor * style_factor * device_factor * team_quality * experience * synergy)
    if game_price <= 5:
        price_factor = 1.35
    elif game_price <= 15:
        price_factor = 1.20
    elif game_price <= 30:
        price_factor = 1.00
    elif game_price <= 50:
        price_factor = 0.75
    else:
        price_factor = max(0.15, 0.75 - (game_price - 50) * 0.008)
    market_luck = random.uniform(0.45, 1.55)
    event = random.random()
    if event < 0.08:
        market_luck *= 1.8
        event_message = "A surprise hit! Players love your game!"
    elif event < 0.20:
        market_luck *= 0.45
        event_message = "Disaster! Your launch barely attracted attention."
    else:
        event_message = "The game launched under normal market conditions."
    demand = (300 * max(0.1, quality) ** 1.25 * price_factor * platform_synergy * (1 + fans / 500) * market_luck)
    copies_sold = max(0, int(demand))
    earnings = copies_sold * game_price
    profit = earnings - total_cost
    rating_score = (2.5 + (quality - 1.0) * 1.3 + (synergy - 1.0) * 1.5 + (platform_synergy - 1.0) - max(0, game_price - 30) / 35 + random.uniform(-0.7, 0.7))
    rating = round(max(1.0, min(5.0, rating_score)), 1)
    balance -= total_cost
    balance += earnings
    fans_gained = max(0, round(copies_sold * (rating / 5) * 0.05))
    fans += fans_gained
    last_game_name = game_name
    last_game_price = game_price
    last_game_sold = copies_sold
    last_game_earnings = earnings
    last_game_rating = rating
    level += 0.1
    month += random.randint(4, 12)
    
    if profit > 0:
        result = "SUCCESS!"
    elif profit == 0:
        result = "BREAK-EVEN."
    else:
        result = "FLOP!"

    history += (
        f"\n\n{game_name} was published!"
        f"\nGenre: {genre_name} | Style: {style_name}"
        f"\nEngine: {engine_name} | Platform: {device_name}"
        f"\nDevelopment cost: ${total_cost:,.0f}"
        f"\nCopies sold: {copies_sold:,}"
        f"\nRevenue: ${earnings:,.0f}"
        f"\nProfit: ${profit:,.0f}"
        f"\nRating: {'★' * int(rating)}"
        f"{'☆' * (5 - int(rating))} ({rating:.1f}/5.0)"
        f"\nFans gained: {fans_gained}"
        f"\n{event_message}"
        f"\nResult: {result}"
    )

    print("\n" + history)
    input("\nPress Enter to continue...")

balance_text = f"{balance:,}".replace(",",".")
history = f"You founded your company, {company_name}!\n${balance_text} were added to your account balance!\nLet's make your first game! Write [new_game] to make a new game. And remember, write [help] for the command list!"

ui_refresh()
print(f"{history}")

while True:
    balance = round(balance, 2)
    balance_text = f"{balance:,}".replace(",",".")
    if month >= 12:
        month_next = month - 12
        year += 1
        month = month_next
    ui_refresh()
    print(f"{history}\n")
    command = input()
    if command == "new_game":
        new_game()
    elif command == "help":
        history += f"\n\nnew_game : Make and publish a new game.\nhire_dev : Hire a developer.\nclear : Clear the history log."
        ui_refresh()
    elif command == "hire_dev":
        hire_dev()
    elif command == "clear":
        history = ""
        ui_refresh()


