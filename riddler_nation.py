# riddler_nation.py
#
# Nick Schwartz
#
# Feb. 2017
#
# An attempt to win FiveThirtyEight's "Riddler Nation Battle Royale"
# with computer simulation.
#
# https://fivethirtyeight.com/features/can-you-rule-riddler-nation/

import random

# Some constants
NUM_CASTLES = 10
TOTAL_SOLDIERS = 100
NUM_TRIALS = 10000000
MIN_WIN_STREAK = 100

# Returns a random valid army (i.e. has the correct number of
# soldiers distributed amongst the correct number of castles)
#
# NOTE: This function occasionally puts '-1' soldiers at a
# castle. These armies should be ignored.
def create_random_army():
    army = []

    # Start off with somewhere between 0 and
    # TOTAL_SOLDIERS / NUM_CASTLES at each castle
    for i in range(NUM_CASTLES):
        army.append(random.randint(0, TOTAL_SOLDIERS / NUM_CASTLES))

    # Clearly, we mose likely won't have enough soldiers after
    # the initial population, so we will multiple each castle
    # by a boost
    boost_factor = (1.0 * TOTAL_SOLDIERS) / sum(army)
    for k in range(len(army)):
        army[k] = (int) (round(army[k] * boost_factor, 0))

    # Add or subtract a few miscellaneous soliders until we
    # have the proper amount
    while sum(army) != TOTAL_SOLDIERS:
        if sum(army) < TOTAL_SOLDIERS:
            army[random.randint(0, NUM_CASTLES - 1)] += 1
        else:
            army[random.randint(0, NUM_CASTLES - 1)] -= 1

    return army

# Simulates a war between two armies. Returns the scores that
# each of the armies earns based on which castles they won.
def have_war(army_1, army_2):
    score_1 = 0
    score_2 = 0

    # For each castle, determine who won. Then increment
    # their score appropriately
    for i in range(NUM_CASTLES):
        if army_1[i] > army_2[i]:
            score_1 += i + 1
        elif army_1[i] < army_2[i]:
            score_2 += i + 1
        # If the number of soldiers is tied, split the points
        else:
            score_1 += (1.0 * (i + 1)) / 2.0
            score_2 += (1.0 * (i + 1)) / 2.0

    return score_1, score_2

# In the main code, we want to run many simulations and see
# which soldier distributions tend to win.

# 'wins' will keep track of the best distributions
wins = {}

# 'current_streak' keeps track of the current win streak
# for the current version of 'my_army'
current_streak = 0

for j in range(NUM_TRIALS):
    # If we just lost, make a new army
    if current_streak == 0:
        my_army = create_random_army()

    # Create a random opponent
    their_army = create_random_army()

    # Have the war
    my_score, their_score = have_war(my_army, their_army)

    # Did we win?
    if my_score > their_score:
        current_streak += 1
    else:
        current_streak = 0

    # If this version of 'my_army' has won many wars in a row,
    # record this distribution of soldiers and the number of
    # wars it has won
    if current_streak >= MIN_WIN_STREAK:
        wins[str(my_army)] = current_streak

# Print out the best armies and how many wars they won
for key in wins:
    print key, wins[key]
