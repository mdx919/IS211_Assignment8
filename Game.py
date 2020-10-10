from Player import Player


class Game:
    players = []

    def __init__(self, num_players):
        for num in range(num_players):
            p = Player(num + 1)
            self.players.append(p)

    def get_players(self):
        return self.players

    def reset_game(self):
        self.players = []


