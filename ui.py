#Created by Achyut Bhattarai
#Project 3: Team Management Program: Part 3
#11/19/2023
#This baseball team manager program facilitates player management within a lineup, enabling users to add, remove, move,
# and edit player positions and statistics while displaying a menu-driven interface for seamless navigation.

import datetime
import objects
import db

VALID_POSITIONS = ('C', '1B', '2B', '3B', 'SS', 'LF', 'CF', 'RF', 'P')


def display_menu(current_date, game_date):
    print("=" * 60)
    print("Baseball Team Manager")
    print(f"CURRENT DATE: {current_date}")

    if game_date is None:
        game_date_input = input("Enter the game date (YYYY-MM-DD): ")
        try:
            game_date = datetime.datetime.strptime(game_date_input, '%Y-%m-%d').date()
        except ValueError:
            print("Invalid date format. Using default date.")
            game_date = None

    if game_date is not None:
        if game_date >= current_date:
            days_until_game = (game_date - current_date).days
            print(f"DAYS UNTIL GAME: {days_until_game}")
    print("\nMENU OPTIONS")
    print("1 – Display lineup")
    print("2 – Add player")
    print("3 – Remove player")
    print("4 – Move player")
    print("5 – Edit player position")
    print("6 – Edit player stats")
    print("7 - Exit program")
    print("\nPOSITIONS")
    print('C, 1B, 2B, 3B, SS, LF, CF, RF, P')
    print("=" * 60)
    print()

def display_lineup(lineup):
    print("Player                                 POS    AB    H    AVG")
    print("-" * 60)
    for i, player in enumerate(lineup, start=1):
        hits = player.hits
        at_bats = player.at_bats
        avg = round(hits / at_bats, 3) if at_bats > 0 else 0.000
        print(f"{i} {player.getFullName():<31} {player.position:>6} {at_bats:>6} {hits:>6} {avg:8.3f}")

def add_player(lineup):
    while True:
        first_name = input("First Name: ")
        last_name = input("Last Name: ")
        position = input("Position (C, 1B, 2B, 3B, SS, LF, CF, RF, P): ")

        if position not in VALID_POSITIONS:
            print("Invalid position. Please choose a valid position.")
            continue

        at_bats = int(input("At bats: "))
        hits = int(input("Hits: "))

        if hits > at_bats or at_bats < 0 or hits < 0:
            print("Invalid input. Please enter valid positive integers for at bats and hits.")
            continue

        new_player = objects.Player(first_name, last_name, position, at_bats, hits)
        lineup.append(new_player)
        print(f"{new_player.getFullName()} was added.\n")
        db.add_player_to_db(new_player)
        break


def remove_player(lineup):
    #if not isinstance(lineup, objects.Lineup):
        #raise TypeError("lineup must be an instance of LineUp")
    while True:
        try:
            index = int(input("Enter a lineup number to remove: ")) - 1

            if 0 <= index < len(lineup):
                player_to_remove = lineup[index]
                lineup.pop(index)  # Remove the player
                if player_to_remove:
                    print(f"{player_to_remove.getFullName()} was deleted!\n")

                    # Call the function to delete the player from the database
                    db.delete_player_from_db(player_to_remove.playerID)
                else:
                    print("No player found at this index.")
                break
            else:
                print("Invalid lineup number.")
        except ValueError:
            print("Invalid input. Please enter a valid lineup number.")


def move_player(lineup):
    while True:
        try:
            from_index = int(input("Enter the current lineup number to move: ")) - 1
            if 0 <= from_index < len(lineup):
                to_index = int(input("Enter the new lineup number: ")) - 1
                tempPlayer = lineup[from_index]
                lineup[from_index] = lineup[to_index]
                lineup[to_index] = tempPlayer
                print("Player was moved.\n")

                # Call the function to update batting order in the database
                db.update_bat_order_in_db(lineup)
                break
            else:
                print("Invalid lineup number.")
        except ValueError:
            print("Invalid input. Please enter valid lineup numbers.")


def edit_player_position(lineup):
    while True:
        try:
            current_lineup_number = int(input("Enter a lineup number to edit: ")) - 1
            players_with_position = [player for player in lineup if player.position in VALID_POSITIONS]
            if 0 <= current_lineup_number < len(players_with_position):
                player = players_with_position[current_lineup_number]
                print(f"You selected {player.getFullName()}: Position={player.position}")
                new_position = input("Enter a new Position: ")
                if new_position in VALID_POSITIONS:
                    player.position = new_position
                    print(f"{player.getFullName()} was updated.\n")

                    # Call the function to update player's position in the database
                    db.update_player_position_in_db(player)
                    break
                else:
                    print("Invalid position. Please choose a valid position.")
            else:
                print("Invalid lineup number.")
        except ValueError:
            print("Invalid input. Please enter a valid lineup number.")

def edit_player_stats(lineup):
    while True:
        try:
            current_lineup_number = int(input("Enter a lineup number to edit stats: ")) - 1
            if 0 <= current_lineup_number < len(lineup):
                player = lineup[current_lineup_number]
                print(f"You selected {player.getFullName()}: At bats={player.at_bats}, Hits={player.hits}")
                new_at_bats = input("Enter new At bats: ")
                new_hits = input("Enter new Hits: ")

                if not new_at_bats.isdigit() or not new_hits.isdigit():
                    print("Invalid input. Please enter valid positive integers for At bats and Hits.")
                    continue

                new_at_bats = int(new_at_bats)
                new_hits = int(new_hits)

                if new_hits > new_at_bats or new_at_bats < 0 or new_hits < 0:
                    print("Invalid input. Please enter valid positive integers for At bats and Hits.")
                    continue

                player.at_bats = new_at_bats
                player.hits = new_hits
                print(f"{player.getFullName()} stats were updated.\n")

                # Call the function to update player's stats in the database
                db.update_player_stats_in_db(player)
                break
            else:
                print("Invalid lineup number.")
        except ValueError:
            print("Invalid input. Please enter a valid lineup number.")




def main():
    current_date = datetime.datetime.now().date()
    game_date = None  # Initialize game_date as None

    lineup = db.get_players()
    display_menu(current_date, game_date)

    while True:
        print()
        command = input("Menu Option: ")

        if command == "1":
            display_lineup(lineup)
        elif command == "2":
            add_player(lineup)
        elif command == "3":
            remove_player(lineup)
        elif command == "4":
            move_player(lineup)
        elif command == "5":
            edit_player_position(lineup)
        elif command == "6":
            edit_player_stats(lineup)
        elif command == "7":
            #db.write_baseball_players_data(lineup)
            print("Bye!")
            break
        else:
            print("Invalid option. Please try again.")
            display_menu(current_date, game_date)

if __name__ == "__main__":
    main()
