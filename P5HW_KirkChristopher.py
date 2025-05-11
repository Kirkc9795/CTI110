#Christopher Kirk
#04/23/2025
#P5HW_UsingAI
#Making a battle game using AI

import random


all_characters = []

def create_characters(limit=1):
    for i in range(limit):
        name = input("Enter character's name: ")
        attack = int(input(f"Enter {name}'s Attack: "))
        intellect = int(input(f"Enter {name}'s Intellect: "))
        speed = int(input(f"Enter {name}'s Speed: "))
        character = {
            'name': name,
            'attack': attack,
            'intellect': intellect,
            'speed': speed
        }
        all_characters.append(character)
        print(f"{name} has been created🔥.\n")

def display_characters():
    print('-------- ALL CHARACTERS --------')
    if not all_characters:
        print("No characters available.\n")
        return
    for i, char in enumerate(all_characters, start=1):
        print(f"{i}. Name: {char['name']}, Attack: {char['attack']}, "
              f"Intellect: {char['intellect']}, Speed: {char['speed']}")
    print()

def battle(char1, char2):
    char1 = char1.copy()
    char2 = char2.copy()
    char1['hp'] = 100
    char2['hp'] = 100

    print(f"⚔\n===⚔️ Battle Start: {char1['name']} vs {char2['name']} ⚔️ ===\n")

    
    if char1['speed'] > char2['speed']:
        attacker, defender = char1, char2
    else:
        attacker, defender = char2, char1

    while char1['hp'] > 0 and char2['hp'] > 0:
        damage = attacker['attack'] - (defender['intellect'] // 2)
        damage = max(1, damage + random.randint(-3, 3))
        defender['hp'] -= damage
        
    
        display_hp = max(0, defender['hp'])
        
        print(f"{attacker['name']} attacks {defender['name']} for {damage} damage! "
              f"{defender['name']} HP: {display_hp}")

        if defender['hp'] <= 0:
            print(f"\n{defender['name']} has been defeated! {attacker['name']} wins!🥇\n")
            break

        attacker, defender = defender, attacker
        
    while True:
        end_game_choice = input("Do you want to end the game? (yes/no): ")
        if end_game_choice in ['y', 'n']:
            if end_game_choice == 'y':
                print("Goodbye!")
                exit()  
            elif end_game_choice == 'n':
                print("Returning to the game menu.")
                return  
        else:
            print("Please enter 'y' or 'n'.")


def run_menu():
    while True:
        print("\n=== Game Menu ===")
        print("1. Create Character")
        print("2. Show All Characters")
        print("3. Battle")
        print("4. Exit")

        choice = input("Choose an option (1-4): ")

        if choice == '1':
            create_characters()
        elif choice == '2':
            display_characters()
        elif choice == '3':
            if len(all_characters) < 2:
                print("You need at least 2 characters to run the game logic.\n")
                continue
            display_characters()

            first = int(input("Select the first character (by number): ")) - 1
            second = int(input("Select the second character (by number): ")) - 1
            if first == second:
                print("Please select two different characters.\n")
                continue
            battle(all_characters[first], all_characters[second])
        elif choice == '4':
            confirm = input("Are you sure you want to end the game? (yes/no): ")
            if confirm == 'yes':
                print("Goodbye!")
                break
            else:
                print("Returning to the game menu.")
        else:
            print("Invalid choice. Please select a number from the menu.")


def main():
    print("Welcome to the Character Battle Game!")
    run_menu()

if __name__ == "__main__":
    main()
