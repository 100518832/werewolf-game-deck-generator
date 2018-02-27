import random

cards = [
        {'name':'villager',         'team':'good',  'weight':1,     'limit':12,     'des':''},
        {'name':'witch',            'team':'good',  'weight':4,     'limit':1,      'des':''},
        {'name':'pacifist',         'team':'good',  'weight':-1,    'limit':1,      'des':''},
        {'name':'p.i',              'team':'good',  'weight':3,     'limit':1,      'des':''},
        {'name':'prince',           'team':'good',  'weight':3,     'limit':1,      'des':''},
        {'name':'seer',             'team':'good',  'weight':7,     'limit':1,      'des':''},
        {'name':'spellcaster',      'team':'good',  'weight':1,     'limit':1,      'des':''},
        {'name':'tough_guy',        'team':'good',  'weight':3,     'limit':1,      'des':''},
        {'name':'lycan',            'team':'good',  'weight':-1,    'limit':1,      'des':''},
        {'name':'mason',            'team':'good',  'weight':2,     'limit':3,      'des':''},
        {'name':'old_hag',          'team':'good',  'weight':1,     'limit':1,      'des':''},
        {'name':'mayor',            'team':'good',  'weight':2,     'limit':1,      'des':''},
        {'name':'troublemaker',     'team':'good',  'weight':-3,    'limit':1,      'des':''},
        {'name':'village_idiot',    'team':'good',  'weight':2,     'limit':1,      'des':''},
        {'name':'apprentice_seer',  'team':'good',  'weight':4,     'limit':1,      'des':''},
        {'name':'aura_seer',        'team':'good',  'weight':3,     'limit':1,      'des':''},
        {'name':'bodyguard',        'team':'good',  'weight':3,     'limit':1,      'des':''},
        {'name':'cult_leader',      'team':'good',  'weight':1,     'limit':1,      'des':''},
        {'name':'cupid',            'team':'good',  'weight':-3,    'limit':1,      'des':''},
        {'name':'diseased',         'team':'good',  'weight':3,     'limit':1,      'des':''},
        {'name':'doppelganger',     'team':'good',  'weight':-2,    'limit':1,      'des':''},
        {'name':'drunk',            'team':'good',  'weight':4,     'limit':1,      'des':''},
        {'name':'ghost',            'team':'good',  'weight':2,     'limit':1,      'des':''},
        {'name':'hunter',           'team':'good',  'weight':3,     'limit':1,      'des':''},
        {'name':'werewolf',         'team':'bad',   'weight':-6,    'limit':8,      'des':''},
        {'name':'wolf_cub',         'team':'bad',   'weight':-8,    'limit':1,      'des':''},
        {'name':'sorceress',        'team':'bad',   'weight':-3,    'limit':1,      'des':''},
        {'name':'tanner',           'team':'bad',   'weight':-2,    'limit':1,      'des':''},
        {'name':'vampire',          'team':'bad',   'weight':-7,    'limit':4,      'des':''},
        {'name':'cursed',           'team':'bad',   'weight':-3,    'limit':1,      'des':''},
        {'name':'lone_wolf',        'team':'bad',   'weight':-5,    'limit':1,      'des':''},
        {'name':'minion',           'team':'bad',   'weight':-6,    'limit':1,      'des':''},
        ]

card_inclusions = {
                   'villager':        [['None']], 
                   'witch':           [['None']], 
                   'pacifist':        [['None']], 
                   'p.i':             [[]], 
                   'prince':          [[]], 
                   'seer':            [[]], 
                   'spellcaster':     [[]], 
                   'tough_guy':       [[]], 
                   'lycan':           [[]], 
                   'mason':           [['mason']], 
                   'old_hag':         [[]], 
                   'mayor':           [['villager']], 
                   'troublemaker':    [[]],
                   'village_idiot':   [['None']], 
                   'apprentice_seer': [['seer'],['aura_seer']], 
                   'aura_seer':       [[]], 
                   'bodyguard':       [[]], 
                   'cult_leader':     [[]], 
                   'cupid':           [[]], 
                   'diseased':        [[]], 
                   'doppelganger':    [[]], 
                   'drunk':           [[]], 
                   'ghost':           [[]], 
                   'hunter':          [[]],
                   'werewolf':        [[]], 
                   'wolf_cub':        [['werewolf'],['lone_wolf']], 
                   'sorceress':       [['seer']], 
                   'tanner':          [[]], 
                   'vampire':         [[]], 
                   'cursed':          [[]], 
                   'lone_wolf':       [['werewolf']], 
                   'minion':          [[]]
                }

card_exclusions = {
                   'villager':[], 
                    'witch':[], 
                    'pacifist':['village_idiot'], 
                    'p.i':['seer','apprentice_seer','aura_seer'], 
                    'prince':['mayor'], 
                    'seer':['aura_seer','p.i'], 
                    'spellcaster':[], 
                    'tough_guy':[], 
                    'lycan':[], 
                    'mason':[], 
                    'old_hag':[], 
                    'mayor':['prince','cult_leader'], 
                    'troublemaker':[],
                    'village_idiot':['pacifist'], 
                    'apprentice_seer':['aura_seer', 'p.i','sorceress'], 
                    'aura_seer':['seer','apprentice_seer','p.i'], 
                    'bodyguard':[], 
                    'cult_leader':['mayor','prince'], 
                    'cupid':[], 
                    'diseased':['vampire'], 
                    'doppelganger':[], 
                    'drunk':[], 
                    'ghost':[], 
                    'hunter':[],
                    'werewolf':['vampire'], 
                    'wolf_cub':['vampire'], 
                    'sorceress':['aura_seer'], 
                    'tanner':[], 
                    'vampire':['werewolf','wolf_cub','cursed','diseased','minion'], 
                    'cursed':['vampire'], 
                    'lone_wolf':[], 
                    'minion':['vampire']
                }

n_people = 12
target = 0
threshold = 0
forced_roles = []
black_listed = []


def card_selection(n_people, target, threshold, forced_roles, black_listed): # argv takes optional string arguments for specified cards we want

    global card_exclusions, card_inclusions, card_limits, card_points, cards

    roles = []
    for name in cards:
        if name['limit'] > 0 or name['name'] in forced_roles:
            if name['name'] not in black_listed:
                roles.append(name['name'])

    deck_points = None
    target_range = list(range(target-threshold,target+threshold+1))

    while deck_points not in target_range:

        deck = []
        deck_points = 0
        
        for forced_role in forced_roles:
            
            deck.append(forced_role)

        while (len(deck) < n_people):

            role_error = False
            role = random.choice(roles)
            
            role_info = {}
            
            for a in range(0,len(cards)):
                if cards[a]['name'] == role:
                    role_info = cards[a]
                    
            
            if role in black_listed:
                continue

            if deck.count(role) == role_info['limit']: # if the # unique roles in the deck are equal too the role limit, then we can can not add this card

                role_error = True

            if role_error is True:
                continue

            for exclusion in card_exclusions[role]: # exclusion is a single role
                if exclusion in deck:

                    role_error = True

                    break

            if role_error is True:
                continue

            for inclusions in card_inclusions[role]: # inclusions is a nested list, card_inclusions[role] is a list of lists
                if 'None' in inclusions: # if this role does not require any other cards to be added, it can be appeneded to the deck
                    break

                absent_inclusions = []

                for inclusion in inclusions: # inclusion is a single role that must come with the selected role, and inclusions in a list of roles
                    if inclusion in deck:
                        continue

                    if inclusion not in deck:

                        absent_inclusions.append(inclusion)

                if len(absent_inclusions) + len(deck) + 1 <= n_people:
                    for a in absent_inclusions: # a is a role

                        deck.append(a)

                    break

                if len(absent_inclusions) + len(deck) + 1 > n_people:

                    role_error = True

            if role_error is True:
                continue

            deck.append(role)
            
            for b in range(0,len(deck)):
                for c in range(0,len(cards)):
                    if deck[b] == cards[c]['name']:
                        deck_points = deck_points + cards[c]['weight']

    return print(deck)

  
def roles():

    global cards

    return cards
