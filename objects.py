#Created by Achyut Bhattarai
#Project 3: Team Management Program: Part 3
#11/19/2023
#This module module defines classes for individual baseball players and team lineups, encapsulating player details and lineup management
# functionalities for the baseball team manager program.


class Player:
    Id = 1

    def __init__(self, first_name, last_name, position, at_bats, hits):
        self.playerID = Player.Id
        self.batOrder = Player.Id
        self.first_name = first_name
        self.last_name = last_name
        self.position = position
        self.at_bats = at_bats
        self.hits = hits
        Player.Id = Player.Id + 1

    def getFullName(self):
        return f"{self.first_name} {self.last_name}"

    def getBattingAvg(self):
        try:
            avg = float(self.hits) / float(self.at_bats)
            return round(avg, 3)
        except ZeroDivisionError:
            return 0.0



class Lineup:
    def __init__(self):
        self.__players = []

    def add_player(self, player):
        self.players.append(player)

    def remove_player(self, index):
        if 0 <= index < len(self.players):
            removed_player = self.players.pop(index)
            return removed_player
        return None

    def get_player(self, lineup_number):
        if 0 < lineup_number <= len(self.players):
            return self.players[lineup_number - 1]
        return None

    def move_player(self, from_index, to_index):
        if 0 <= from_index < len(self.players) and 0 <= to_index < len(self.players):
            player_to_move = self.players.pop(from_index)
            self.players.insert(to_index, player_to_move)

    def __len__(self):
        return len(self.players)

    def __iter__(self):
        return iter(self.players)