"""CS 61A Presents The Game of Hog."""

from dice import six_sided, four_sided, make_test_dice
from ucb import main, trace, interact

GOAL_SCORE = 100  # The goal of Hog is to score 100 points.
FIRST_101_DIGITS_OF_PI = 31415926535897932384626433832795028841971693993751058209749445923078164062862089986280348253421170679

######################
# Phase 1: Simulator #
######################


def roll_dice(num_rolls, dice=six_sided):
    """Simulate rolling the DICE exactly NUM_ROLLS > 0 times. Return the sum of
    the outcomes unless any of the outcomes is 1. In that case, return 1.

    num_rolls:  The number of dice rolls that will be made.
    dice:       A function that simulates a single dice roll outcome.
    """
    # These assert statements ensure that num_rolls is a positive integer.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls > 0, 'Must roll at least once.'
    # BEGIN PROBLEM 1
    "*** YOUR CODE HERE ***"
    flag = False
    sum_sco = 0
    while num_rolls > 0:
        out_round = dice()
        num_rolls -= 1
        sum_sco += out_round
        if out_round == 1:
            flag = True
    if flag:
        return 1
    else:
        return sum_sco
    # END PROBLEM 1


def free_bacon(score):
    """Return the points scored from rolling 0 dice (Free Bacon).

    score:  The opponent's current score.
    """
    assert score < 100, 'The game should be over.'
    pi = FIRST_101_DIGITS_OF_PI

    # Trim pi to only (score + 1) digit(s)
    # BEGIN PROBLEM 2
    "*** YOUR CODE HERE ***"
    i = 0
    while i < 100-score:
        pi //= 10  # 将 pi 右移一位，相当于去掉最右边的一位
        i += 1
    # END PROBLEM 2
    return pi % 10 + 3


def take_turn(num_rolls, opponent_score, dice=six_sided):
    """Simulate a turn rolling NUM_ROLLS dice, which may be 0 (Free Bacon).
    Return the points scored for the turn by the current player.

    num_rolls:       The number of dice rolls that will be made.
    opponent_score:  The total score of the opponent.
    dice:            A function that simulates a single dice roll outcome.
    """
    # Leave these assert statements here; they help check for errors.
    assert type(num_rolls) == int, 'num_rolls must be an integer.'
    assert num_rolls >= 0, 'Cannot roll a negative number of dice in take_turn.'
    assert num_rolls <= 10, 'Cannot roll more than 10 dice.'
    assert opponent_score < 100, 'The game should be over.'
    # BEGIN PROBLEM 3
    "*** YOUR CODE HERE ***"
    if num_rolls==0:
        return free_bacon(opponent_score)
    else:
        return roll_dice(num_rolls,dice)
    # END PROBLEM 3


def extra_turn(player_score, opponent_score):
    """Return whether the player gets an extra turn."""
    return (pig_pass(player_score, opponent_score) or
            swine_align(player_score, opponent_score))


def swine_align(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Swine Align.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> swine_align(30, 45)  # The GCD is 15.
    True
    >>> swine_align(35, 45)  # The GCD is 5.
    False
    """
    # BEGIN PROBLEM 4a
    "*** YOUR CODE HERE ***"
    if player_score == 0 or opponent_score == 0:
        return False
    def gcd(x,y):
        if(x%y==0):
            return y
        else:
            return gcd(y,x%y)
    GCD=gcd(player_score,opponent_score)

    if(GCD>=10):
        return True
    else:
        return False
    # END PROBLEM 4a


def pig_pass(player_score, opponent_score):
    """Return whether the player gets an extra turn due to Pig Pass.

    player_score:   The total score of the current player.
    opponent_score: The total score of the other player.

    >>> pig_pass(9, 12)
    False
    >>> pig_pass(10, 12)
    True
    >>> pig_pass(11, 12)
    True
    >>> pig_pass(12, 12)
    False
    >>> pig_pass(13, 12)
    False
    """
    # BEGIN PROBLEM 4b
    "*** YOUR CODE HERE ***"
    diff=opponent_score-player_score
    if 3>diff and diff >0:
        return True
    else:
        return False
    # END PROBLEM 4b


def other(who):
    """Return the other player, for a player WHO numbered 0 or 1.

    >>> other(0)
    1
    >>> other(1)
    0
    """
    return 1 - who


def silence(score0, score1):
    """Announce nothing (see Phase 2)."""
    return silence


def play(strategy0, strategy1, score0=0, score1=0, dice=six_sided,
         goal=GOAL_SCORE, say=silence):
    """Simulate a game and return the final scores of both players, with Player
    0's score first, and Player 1's score second.
    """
    who = 0  # Who is about to take a turn, 0 (first) or 1 (second)
    scores = [score0, score1]
    strategies = [strategy0, strategy1]
    
    while scores[who] < goal:
        num_roll = strategies[who](scores[who], scores[1-who])
        score = take_turn(num_roll, scores[1-who], dice)
        scores[who] += score
        score0, score1 = scores
        say = say(score0, score1)
        # Check if extra turn is awarded
        while(extra_turn(scores[who], scores[1-who])):
            num_roll = strategies[who](scores[who], scores[1-who])
            score = take_turn(num_roll, scores[1-who], dice)
            scores[who] += score
            score0, score1 = scores
            say = say(score0, score1)
            if scores[who] >= goal:
                break

        if scores[who] >= goal:
            break
        
        who = other(who)  # Switch to the other player

    return score0, score1

def total(s0, s1):
     print(s0 + s1)
     return echo

def echo(s0, s1):
     print(s0, s1)
     return total
def always_roll(x,y):
    return 1
s0, s1 = play(always_roll, always_roll, dice=make_test_dice(2, 5), goal=10, say=echo)