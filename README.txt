Nick Schwartz
FiveThirtyEight's Riddler from 2/3/2017

Can You Rule Riddler Nation?
https://fivethirtyeight.com/features/can-you-rule-riddler-nation/

This is an attempt to find an army that will "Rule Riddler Nation." The idea is
simple: randomly generate armies to fight each other, then observe which armies
win the most.

The code in riddler_nation.py runs these simulations and outputs the armies
with the most wins (see the code comments in this file for more details). Some
of the more successful armies are shown in the some_winners.txt file; each line
of the file shows a distribution of soldiers (from less important to more
important castles) followed by the number of wars that particular lineup won
during the simulations.

Admittedly, this strategy has a flaw. These simulations determine which lineups
are best against *randomly generated* armies. In the real contest, the opposing
armies will be created by many different people using many different tactics,
and they certainly will not be random.