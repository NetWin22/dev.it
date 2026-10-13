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
    global last_game_name, last_game_price, balance, last_game_sold, last_game_earnings, year, level, developers, month, fans
    ui_refresh()
    print("Game Name?:\n")
    game_name = input()
    print("\nPrice?\n")
    
    while True:
        try:
            game_price = int(input())
        except ValueError:
            print("Use a number")
            continue
        break

        
    last_game_name = game_name
    last_game_price = game_price
    print("\nHow much you want to spend to make this game?\n")
    
    while True:
        try:
            budget = int(input())
        except ValueError:
            print("Use a number")
            continue
        break
        
    balance -= budget
    #copies_sold = ((balance * budget) / 1000) * game_price * random.randint(3, 15 * level)   -- old formula
    #copies_sold = int(((budget / 10) * (60 / game_price if game_price > 0 else 1) * random.uniform(3, 15 * level * developers))) -- old formula
    quality = ((budget / 10000) ** 0.5 * (1 + level * 0.15) * (1 + developers * 0.05))
    price_factor = max(0.15, 1.5 - game_price / 40)
    luck = random.uniform(0.7, 1.3)
    copies_sold = max(0, int(500 * quality * price_factor * (1 + fans / 1000) * luck))
    fans += round((copies_sold * 0.05), 0)
    last_game_sold = copies_sold
    last_game_earnings = copies_sold * game_price
    balance += last_game_earnings
    month += random.randint(4, 12)
    return

balance_text = f"{balance:,}".replace(",",".")
history = f"You founded your company, {company_name}!\n${balance_text} were added to your account balance!\nLet's make your first game! Write [new_game] to make a new game. And remember, write [help] for the command list!"

ui_refresh()
print(f"{history}")

while True:
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
        last_game_price = f"{last_game_price:,}".replace(",",".")
        last_game_earnings = f"{last_game_earnings:,}".replace(",",".")
        last_game_sold = f"{last_game_sold:,}".replace(",",".")
        history += f"\nThe game {last_game_name} was published at ${last_game_price}. You earned {last_game_earnings} by selling {last_game_sold} copies!"
    elif command == "help":
        history += f"\n\nnew_game : Make and publish a new game.\nhire_dev : Hire a developer.\nclear : Clear the history log."
        ui_refresh()
    elif command == "hire_dev":
        hire_dev()
    elif command == "clear":
        history = ""
        ui_refresh()


