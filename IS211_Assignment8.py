import argparse, sys
import random
from Game import Game, TimedGameProxy
from Player import PlayerFactory

# random.seed(0)  # was giving same number so i commented it out
WIN_SCORE = 100


def create_players(p_1, p_2, timed=False):
    factory = PlayerFactory()
    p1 = factory.get_player(p_1)
    p2 = factory.get_player(p_2)
    start_game(p1, p2, timed)


def start_game(p1, p2, timed):
    game = Game(p1, p2)
    timer = TimedGameProxy(timed)

    while True:
        for player in game.get_players():
            if player.get_player_name() == 'human':
                print(player.get_player_name(), ' Player')
                score = 0
                ask_user = None
                while True:
                    ask_user = input("type and enter \'r\' for keep rolling or \'h\' for hold.")
                    if ask_user.lower() not in ('h', 'r'):
                        timer.add_time(game)
                        pass
                    elif ask_user == 'h':
                        player.add_total_score()
                        timer.add_time(game)
                        display_stats(player, score, False, timer)
                        player.clear_turn_score()
                        break
                    elif ask_user == 'r':
                        score = roll_dice()
                        if score == 1:
                            player.clear_turn_score()
                            timer.add_time(game)
                            display_stats(player, score, False, timer)
                            break
                        else:
                            player.add_turn_score(score)
                            timer.add_time(game)
                            display_stats(player, score, False, timer)
                            if player.get_total_score() + player.get_turn_score() >= WIN_SCORE:
                                print(player.get_player_name(), ' Player WON!!!')
                                game.reset_game()
                                sys.exit()
                            continue
                        break

            elif player.get_player_name() == 'computer':
                print(player.get_player_name(), ' Player')
                while True:
                    score = roll_dice()
                    if score == 1:
                        timer.add_time(game)
                        display_stats(player, score, False, timer)
                        player.clear_turn_score()
                        break
                    elif player.get_turn_score() >= 25 or player.get_turn_score() + player.get_total_score() >= WIN_SCORE:
                        player.add_turn_score(score)
                        if player.get_total_score() + player.get_turn_score() >= WIN_SCORE:
                            print(player.get_player_name(), ' Player WON!!!')
                            game.reset_game()
                            sys.exit()
                        player.add_total_score()
                        timer.add_time(game)
                        display_stats(player, score, False, timer)
                        player.clear_turn_score()
                        break
                    elif player.get_turn_score() < 25:
                        player.add_turn_score(score)
                        timer.add_time(game)
                        display_stats(player, score, False, timer)
                        continue


def display_stats(player, score, lost_turn, timer):
    if lost_turn:
        print(player.get_player_name(), ' Player')
        print(
            "LOST TURN __ Rolled: {}, Total lost: {}, Total Score: {}, time {}".format(score,
                                                                                player.get_turn_score(),
                                                                                player.get_total_score(), timer.display_time()))
    else:
        print(player.get_player_name(), ' Player')
        print("{} Dice Rolled: {}, Turn Total: {}, Current total: {}, time {} ".format(player.get_player_name(), score,
                                                                               player.get_turn_score(),
                                                                               player.get_turn_score() + player.get_total_score(), timer.display_time()))


def roll_dice():
    return random.randint(1, 6)


parser = argparse.ArgumentParser()
parser.add_argument("--player1")
parser.add_argument("--player2")
parser.add_argument("--timed")
args = parser.parse_args()
if not args.player1 or not args.player2:
    print('Please provide 2 player using --player1 and --player2 flag')  # start game with default 2 players
elif args.player1 and args.player2 and args.timed:
    create_players(args.player1, args.player2, args.timed)  # start game with time
elif args.player1 and args.player2 and not args.timed:
    create_players(args.player1, args.player2)  # start game without time
else:
    print('Error')
