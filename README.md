# werewolf

Random deck generator for the party game 'werewolf' 

This script includes the following features:
1) A variable, target , which corresponds to the game's point system (the sum of points should equal 0 in a deck)
```
target = 0 # variable
```
2) A variable, n_people, which corresponds to the number of roles to be dealt, or number of cards in the deck
```
n_people = 10 # variable
```
3) A variable, threshold, which will control the range at which an 'acceptable' deck target value is reached
```
threshold = 1 # variable
```
  b) Each role card has a given int point value which can be negative or positive; the sum the points in the deck should equal the target
 
4) A list of strings, ```forced_roles```, is a list that is passed to the main function that ensures the roles inside the list are added 

5) A list of strings, ```black_listed```, is a list that is passed to the main function that ensures the roles inside the list are not added
There are 3 dictionaries within the ww.py script:

```
        self.cards = cards = [
            {'name': 'villager', 'team': 'good', 'weight': 1, 'limit': 12, 'des': ''},
            {'name': 'witch', 'team': 'good', 'weight': 4, 'limit': 1, 'des': ''},
            {'name': 'pacifist', 'team': 'good', 'weight': -1, 'limit': 1, 'des': ''},
            {'name': 'p.i', 'team': 'good', 'weight': 3, 'limit': 1, 'des': ''},
            {'name': 'prince', 'team': 'good', 'weight': 3, 'limit': 1, 'des': ''},
            {'name': 'seer', 'team': 'good', 'weight': 7, 'limit': 1, 'des': ''},
            {'name': 'spellcaster', 'team': 'good', 'weight': 1, 'limit': 1, 'des': ''},
            {'name': 'tough_guy', 'team': 'good', 'weight': 3, 'limit': 1, 'des': ''},
            {'name': 'lycan', 'team': 'good', 'weight': -1, 'limit': 1, 'des': ''},
            {'name': 'mason', 'team': 'good', 'weight': 2, 'limit': 3, 'des': ''},
            {'name': 'old_hag', 'team': 'good', 'weight': 1, 'limit': 1, 'des': ''},
            {'name': 'mayor', 'team': 'good', 'weight': 2, 'limit': 1, 'des': ''},
            {'name': 'troublemaker', 'team': 'good', 'weight': -3, 'limit': 1, 'des': ''},
            {'name': 'village_idiot', 'team': 'good', 'weight': 2, 'limit': 1, 'des': ''},
            {'name': 'apprentice_seer', 'team': 'good', 'weight': 4, 'limit': 1, 'des': ''},
            {'name': 'aura_seer', 'team': 'good', 'weight': 3, 'limit': 1, 'des': ''},
            {'name': 'bodyguard', 'team': 'good', 'weight': 3, 'limit': 1, 'des': ''},
            {'name': 'cult_leader', 'team': 'good', 'weight': 1, 'limit': 1, 'des': ''},
            {'name': 'cupid', 'team': 'good', 'weight': -3, 'limit': 1, 'des': ''},
            {'name': 'diseased', 'team': 'good', 'weight': 3, 'limit': 1, 'des': ''},
            {'name': 'doppelganger', 'team': 'good', 'weight': -2, 'limit': 1, 'des': ''},
            {'name': 'drunk', 'team': 'good', 'weight': 4, 'limit': 1, 'des': ''},
            {'name': 'ghost', 'team': 'good', 'weight': 2, 'limit': 1, 'des': ''},
            {'name': 'hunter', 'team': 'good', 'weight': 3, 'limit': 1, 'des': ''},
            {'name': 'werewolf', 'team': 'bad', 'weight': -6, 'limit': 8, 'des': ''},
            {'name': 'wolf_cub', 'team': 'bad', 'weight': -8, 'limit': 1, 'des': ''},
            {'name': 'sorceress', 'team': 'bad', 'weight': -3, 'limit': 1, 'des': ''},
            {'name': 'tanner', 'team': 'bad', 'weight': -2, 'limit': 1, 'des': ''},
            {'name': 'vampire', 'team': 'bad', 'weight': -7, 'limit': 4, 'des': ''},
            {'name': 'cursed', 'team': 'bad', 'weight': -3, 'limit': 1, 'des': ''},
            {'name': 'lone_wolf', 'team': 'bad', 'weight': -5, 'limit': 1, 'des': ''},
            {'name': 'minion', 'team': 'bad', 'weight': -6, 'limit': 1, 'des': ''},
        ]

        self.card_inclusions = card_inclusions = {
            'villager': [['None']],
            'witch': [['None']],
            'pacifist': [['None']],
            'p.i': [[]],
            'prince': [[]],
            'seer': [[]],
            'spellcaster': [[]],
            'tough_guy': [[]],
            'lycan': [[]],
            'mason': [['mason']],
            'old_hag': [[]],
            'mayor': [['villager']],
            'troublemaker': [[]],
            'village_idiot': [['None']],
            'apprentice_seer': [['seer'], ['aura_seer']],
            'aura_seer': [[]],
            'bodyguard': [[]],
            'cult_leader': [[]],
            'cupid': [[]],
            'diseased': [[]],
            'doppelganger': [[]],
            'drunk': [[]],
            'ghost': [[]],
            'hunter': [[]],
            'werewolf': [[]],
            'wolf_cub': [['werewolf'], ['lone_wolf']],
            'sorceress': [['seer']],
            'tanner': [[]],
            'vampire': [[]],
            'cursed': [[]],
            'lone_wolf': [['werewolf']],
            'minion': [[]]
        }

        self.card_exclusions = card_exclusions = {
            'villager': [],
            'witch': [],
            'pacifist': ['village_idiot'],
            'p.i': ['seer', 'apprentice_seer', 'aura_seer'],
            'prince': ['mayor'],
            'seer': ['aura_seer', 'p.i'],
            'spellcaster': [],
            'tough_guy': [],
            'lycan': [],
            'mason': [],
            'old_hag': [],
            'mayor': ['prince', 'cult_leader'],
            'troublemaker': [],
            'village_idiot': ['pacifist'],
            'apprentice_seer': ['aura_seer', 'p.i', 'sorceress'],
            'aura_seer': ['seer', 'apprentice_seer', 'p.i'],
            'bodyguard': [],
            'cult_leader': ['mayor', 'prince'],
            'cupid': [],
            'diseased': ['vampire'],
            'doppelganger': [],
            'drunk': [],
            'ghost': [],
            'hunter': [],
            'werewolf': ['vampire'],
            'wolf_cub': ['vampire'],
            'sorceress': ['aura_seer'],
            'tanner': [],
            'vampire': ['werewolf', 'wolf_cub', 'cursed', 'diseased', 'minion'],
            'cursed': ['vampire'],
            'lone_wolf': [],
            'minion': ['vampire']
        }
```
The dict ```card_points```  contains a nested dictionary of good and bad roles, to define the teams. Every role card you wish to play with, or have, should be in this dictionary at some point (and the other 3 too). If you want to break up the roles into more teams; some ```bad``` roles are actually against each other ```bad``` roles (i.e, vampires vs werewolves, or lone wolf vs werewolves). This dictionary is used to keep track of all possible cards, and their point values for calculating the deck value.


