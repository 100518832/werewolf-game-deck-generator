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

```
forced_roles = ['villager','villager','werewolf','seer']
black_listed = ['lone_wolf','cub_wolf']
deck = card_selection(10,0,1, forced_roles, black_listed)
>>> (['villager', 'villager', 'werewolf', 'seer', 'sorceress', 'villager', 'diseased', 'cupid', 'cult_leader', 'lycan'], 1)
```
The output is a tuple containing a list of the deck roles, and the score of the deck. As you can see our optional string arguments passed to the function ```card_selection``` were ``` 'villager', 'villager', 'werewolf', 'seer' ``` , and therefore these roles were forced into the deck; however, forced roles are added to the deck before the selection process. This means that you can bypass roles that normally can not be played together as long as they are both forced to the ```deck``` as optional string arguments.  

There are 4 dictionaries within the ww.py script:

```
card_points = {'good':{'villager':1, 'witch':4, 'pacifist':-1, 'p.i':3, 'prince':3, 'seer':7, 'spellcaster':1, 'tough_guy':3, 'lycan':-1, 'mason':2, 'old_hag':1, 'mayor':2, 'troublemaker':-3, 
                       'village_idiot':2, 'apprentice_seer':4, 'aura_seer':3, 'bodyguard':3, 'cult_leader':1, 'cupid':-3, 'diseased':3, 'doppelganger':-2, 'drunk':4, 'ghost':2, 'hunter':3 }, 
                'bad':{'werewolf':-6, 'wolf_cub':-8, 'sorceress':-3, 'tanner':-2, 'vampire':-7, 'cursed':-3, 'lone_wolf':-5, 'minion':-6 }
                }

card_limits = {'villager':12, 'witch':1, 'pacifist':1, 'p.i':0, 'prince':0, 'seer':1, 'spellcaster':0, 'tough_guy':1, 'lycan':1, 'mason':2, 'old_hag':1, 'mayor':1, 'troublemaker':0,
                       'village_idiot':1, 'apprentice_seer':1, 'aura_seer':0, 'bodyguard':1, 'cult_leader':1, 'cupid':1, 'diseased':1, 'doppelganger':1, 'drunk':1, 'ghost':0, 'hunter':1,
                'werewolf':8, 'wolf_cub':1, 'sorceress':1, 'tanner':0, 'vampire':0, 'cursed':1, 'lone_wolf':1, 'minion':1
                }

card_inclusions = {'villager':[['None']], 'witch':[['None']], 'pacifist':[['None']], 'p.i':[[]], 'prince':[[]], 'seer':[[]], 'spellcaster':[[]], 'tough_guy':[[]], 'lycan':[[]], 'mason':[['mason']], 'old_hag':[[]], 'mayor':[['villager']], 'troublemaker':[[]], 
                       'village_idiot':[['None']], 'apprentice_seer':[['seer'],['aura_seer']], 'aura_seer':[[]], 'bodyguard':[[]], 'cult_leader':[[]], 'cupid':[[]], 'diseased':[[]], 'doppelganger':[[]], 'drunk':[[]], 'ghost':[[]], 'hunter':[[]], 
                'werewolf':[[]], 'wolf_cub':[['werewolf'],['lone_wolf']], 'sorceress':[['seer']], 'tanner':[[]], 'vampire':[[]], 'cursed':[[]], 'lone_wolf':[['werewolf']], 'minion':[[]] 
                }

card_exclusions = {'villager':[], 'witch':[], 'pacifist':['village_idiot'], 'p.i':['seer','apprentice_seer','aura_seer'], 'prince':['mayor'], 'seer':['aura_seer','p.i'], 'spellcaster':[], 'tough_guy':[], 'lycan':[], 'mason':[], 'old_hag':[], 'mayor':['prince','cult_leader'], 'troublemaker':[], 
                       'village_idiot':['pacifist'], 'apprentice_seer':['aura_seer', 'p.i','sorceress'], 'aura_seer':['seer','apprentice_seer','p.i'], 'bodyguard':[], 'cult_leader':['mayor','prince'], 'cupid':[], 'diseased':['vampire'], 'doppelganger':[], 'drunk':[], 'ghost':[], 'hunter':[], 
                'werewolf':['vampire'], 'wolf_cub':['vampire'], 'sorceress':['aura_seer'], 'tanner':[], 'vampire':['werewolf','wolf_cub','cursed','diseased','minion'], 'cursed':['vampire'], 'lone_wolf':[], 'minion':['vampire']
                }
```
The dict ```card_points```  contains a nested dictionary of good and bad roles, to define the teams. Every role card you wish to play with, or have, should be in this dictionary at some point (and the other 3 too). If you want to break up the roles into more teams; some ```bad``` roles are actually against each other ```bad``` roles (i.e, vampires vs werewolves, or lone wolf vs werewolves). This dictionary is used to keep track of all possible cards, and their point values for calculating the deck value.

If you wish to further organize this dictionary into more nested dictionaries please know you will have to adjust the following lines:

```
good_roles = list(card_points['good'].copy().keys())
bad_roles = list(card_points['bad'].copy().keys())
roles = bad_roles + good_roles
```
The dict ```card_limits``` controls how many of each role can be in a deck at a single time (this can be overridden with forced roles). As such, cards you do not have, or do not want to play with, should have a value of zero. Cards with a value of zero will not be added to the deck.

The dict ```card_inclusions``` is more complicated than the other. This dictionary ensures that if a role that has be selected as a candidate to be added to the deck, that either the other cards required to be played are either already in the deck, or can be added to the deck (given their is room, and no exclusions apply to the cards to be included). In this dictionary the keys are the candidate card we are going to add, and the items is a list of lists. The reason there are nested lists, is that a single card may require two roles to be added, or only one other role to be added. 

Lets use an example:

```
'apprentice_seer':[['seer'],['aura_seer']], 'aura_seer':[[]]
```
The above snippet is from the ```card_inclusions``` dict, and shows that the apprentice_seer key has a list as an item, if we look inside this list we see that there are two lists. So the apprentice_seer, either requires that the aura_seer or seer be in, or added, to the deck; however; the aura_seer, does not require any other cards to be added.

The final dict ``` card_exclusions ``` is simple. The key corresponds to the candidate role selected, and the item is a list of cards, that can not already be in the deck if this card is to be added. 

Feel free to add your own cards to each of the dictionaries, your own limits, exclusions, or inclusions. 
