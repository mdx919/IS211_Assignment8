import argparse
import random
from Game import Game


# random.seed(0) was giving same number so i commented it out

def create_players(p1, p2, timed):
    factory = Factory()

def start_game(num_players):
    game_over = False
    g1 = Game(num_players)

    print('NEW GAME!!')
    while not game_over:
        for player in g1.get_players():
            hold = False
            score = roll_dice()
            while not hold:
                if score == 1:
                    hold = True
                    print('Player#', player.get_player_name())
                    print('Oops, better luck next turn!')
                    print(
                        "Dice Rolled: {}, Turn Total lost: {}, Last total: {}, ".format(score, player.get_turn_score(),
                                                                                        player.get_total_score()))
                    player.clear_turn_score()
                else:
                    player.add_turn_score(score)
                    current_total = player.get_total_score() + player.get_turn_score()
                    print('Player#', player.get_player_name())
                    print("Dice Rolled: {}, Turn Total: {}, Current total: {}, ".format(score, player.get_turn_score(),
                                                                                        current_total))
                    if current_total >= 20:
                        print('GAME OVER!!!')
                        print('Player# {} WON with score of {}'.format(player.get_player_name(), current_total))
                        g1.reset_game()
                        start_game(num_players)
                    ask_user = None
                    while True:
                        ask_user = input("type and enter \'r\' for keep rolling or \'h\' for hold.")
                        if ask_user.lower() not in ('h', 'r'):
                            pass
                        else:
                            break

                    if ask_user == 'h':
                        player.add_total_score()
                        hold = True
                    elif ask_user == 'r':
                        score = roll_dice()
                        continue


def roll_dice():
    return random.randint(1, 6)


parser = argparse.ArgumentParser()
# parser.add_argument("--numPlayers")
parser.add_argument("--player1")
parser.add_argument("--player2")
args = parser.parse_args()
if not args.player1 or not args.player2:
    print('Please provide 2 player using --player1 and --player2 flag')  # start game with default 2 players
else:
    start_game(int(args.numPlayers))  # start game with numPlayers
