# werewolf
Random deck generator for the party game 'werewolf' 

This script includes the following features:
1) A variable, target , which corresponds to the game's point system (the sum of points should equal 0 in a deck) 
2) A variable, n_people, which corresponds to the number of roles to be dealt, or number of cards in the deck
3) A variable, threshold, which will control the range at which an 'acceptable' deck target value is reached
  b) Each role card has a given int point value which can be negative or positive; the sum the points in the deck should equal the target
4) The user can pass a variable number of optional strings to the card_selection function to force a certain number of roles into the deck

The output is a tuple contining a list of the deck roles, and the score of the deck. 

