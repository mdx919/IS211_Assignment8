class Player:
    def __init__(self, player_name):
        self.player_name = player_name
        self.total_score = 0
        self.turn_score = 0

    def get_total_score(self):
        return self.total_score

    def add_total_score(self):
        self.total_score += self.turn_score
        self.turn_score = 0

    def add_turn_score(self, score):
        self.turn_score += score

    def get_player_name(self):
        return self.player_name

    def clear_turn_score(self):
        self.turn_score = 0

    def get_turn_score(self):
        return self.turn_score


class ComputerPlayer(Player):
    def play(self, total_score):
        if 100 - total_score < 25:
            return False
        else:
            return True


class PlayerFactory:
    def get_player(self, player_name):
        if player_name.lower() == 'human':
            return Player(player_name)
        elif player_name.lower() == 'computer':
            return ComputerPlayer(player_name)
