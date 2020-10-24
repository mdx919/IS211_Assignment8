from Player import Player
from operator import attrgetter
import sys


class Game:
    players = []

    def __init__(self, p1, p2):
        self.players.append(p1)
        self.players.append(p2)

    def get_players(self):
        return self.players

    def reset_game(self):
        self.players = []

    def max_score(self):
        return max(self.players, key=attrgetter('total_score'))


class TimedGameProxy(Game):
    t = 0
    timed = False

    def __init__(self, timed):
        self.timed = timed

    def add_time(self, game):
        self.t += 1
        if self.timed and self.t >= 60:
            p = game.max_score()
            print("Time Limit passed {} !! {} WON with Total score of {}".format(self.t, p.get_player_name(),
                                                                                 p.get_total_score()))
            sys.exit()

    def display_time(self):
        return self.t
