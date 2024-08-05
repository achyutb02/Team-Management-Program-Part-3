import sqlite3
from contextlib import closing
from objects import Player

conn = None
DB_FILE = "player_db.sqlite"


def connect():
    global conn
    if not conn:
        conn = sqlite3.connect(DB_FILE)
        conn.row_factory = sqlite3.Row
    return conn



def close(connection):
    if connection:
        connection.close()



def get_players():
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM Player")
        rows = cursor.fetchall()
        players = []
        for row in rows:
            player = Player(
                row['firstName'], row['lastName'], row['position'],
                row['atBats'], row['hits']
            )
            players.append(player)
        return players
    except sqlite3.Error as e:
        print("Error fetching players:", e)
    #finally:
        #close(conn)

def get_player(playerID):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM Player WHERE playerID = ?", (playerID,))
    row = cursor.fetchone()
    close(conn)
    if row:
        return Player(row['playerID'], row['batOrder'], row['firstName'], row['lastName'], row['position'],
                      row['atBats'], row['hits'])
    else:
        return None

def add_player_to_db(player):
    try:
        with sqlite3.connect('player_db.sqlite') as conn:
            cursor = conn.cursor()
            cursor.execute(
                "INSERT INTO Player (playerID, batOrder, firstName, lastName, position, atBats, hits) VALUES (?, ?, ?, ?, ?, ?, ?)",
                (player.playerID, player.batOrder, player.first_name, player.last_name, player.position, player.at_bats, player.hits)
            )
            conn.commit()
    except sqlite3.Error as e:
        print("Error adding player to the database:", e)






def delete_player_from_db(playerID):
    try:
        conn = connect()
        cursor = conn.cursor()
        cursor.execute("DELETE FROM Player WHERE playerID = ?", (playerID,))
        conn.commit()
    except sqlite3.Error as e:
        print("Error deleting player from the database:", e)
    #finally:
        #if conn:
            #close(conn)






def update_bat_order_in_db(lineup):
    conn = connect()
    cursor = conn.cursor()
    for player in lineup:
        cursor.execute("UPDATE Player SET batOrder = ? WHERE playerID = ?", (player.batOrder, player.playerID))
    conn.commit()
    #close(conn)


def update_player_position_in_db(player):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute("UPDATE Player SET position = ? WHERE playerID = ?", (player.position, player.playerID))
    conn.commit()
    #close(conn)

def update_player_stats_in_db(player):
    conn = connect()
    cursor = conn.cursor()
    cursor.execute(
        "UPDATE Player SET atBats = ?, hits = ? WHERE playerID = ?",
        (player.at_bats, player.hits, player.playerID)
    )
    conn.commit()
    #close(conn)

def main():
    # code to test the get_players function
    players = get_players()
    if players is not None:
        for player in players:
            print(player.playerID, player.batOrder, player.first_name, player.last_name,
                  player.position, player.at_bats, player.hits, player.getBattingAvg())
    else:
        print("Code is needed for the get_players function.")


if __name__ == "__main__":
    main()