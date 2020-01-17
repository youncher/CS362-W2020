"""
Created on Fri Jan 17 2020

@author: youncher
"""
import testUtility

# Get player names
player_names = testUtility.get_player_names()

# number of curses and victory cards
nV = 12 if len(player_names) > 2 else 8 # Number Victory cards
nC = -10 + 10 * len(player_names) # Number Curse cards

# Box of potential cards
box = testUtility.create_box(nV, nC)

# Sets supplies and their values
supply_order = testUtility.get_supply_order()

# Pick 10 cards from box to be in the supply
supply = testUtility.create_supply(box)

# Add required cards
testUtility.add_required_supplies(supply, nV, nC, player_names)

# Costruct the Player objects
players = testUtility.construct_players(player_names)
print(players)
testUtility.play_game(supply, supply_order, players)

testUtility.final_score(players)