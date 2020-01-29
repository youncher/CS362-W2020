"""
Created on Fri Jan 17 2020

@author: youncher
"""
import testUtility

# Get player names
player_names = testUtility.get_players()

# number of curses and victory cards
nV = testUtility.get_victory_cards(player_names) #12 if len(player_names) > 2 else 8 # Number Victory cards
nC = testUtility.get_curses(player_names) #-10 + 10 * len(player_names) # Number Curse cards

# Box of potential cards
# box = testUtility.get_boxes(nV) # This is removed for testing purposes
box = {} # Line added to introduce bug for Test Scenario

# Sets supplies and their values
supply_order = testUtility.get_supply_order()

# Pick 10 cards from box to be in the supply
supply = testUtility.get_supply(box)

# Add required cards
testUtility.add_required_supplies(supply, nV, nC, player_names)

# Costruct the Player objects
players = testUtility.construct_players(player_names)
print(players)
testUtility.play_game(supply, supply_order, players)

testUtility.final_score(players)