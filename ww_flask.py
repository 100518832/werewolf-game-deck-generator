
from flask import Flask
from flask import jsonify
from flask_cors import CORS, cross_origin

app = Flask(__name__)
CORS(app)
import random

#card_points = {'good':{'villager':1, 'witch':4, 'pacifist':-1, 'p.i':3, 'prince':3, 'seer':7, 'spellcaster':1, 'tough_guy':3, 'lycan':-1, 'mason':2, 'old_hag':1, 'mayor':2, 'troublemaker':-3,
#                       'village_idiot':2, 'apprentice_seer':4, 'aura_seer':3, 'bodyguard':3, 'cult_leader':1, 'cupid':-3, 'diseased':3, 'doppelganger':-2, 'drunk':4, 'ghost':2, 'hunter':3 },
#                'bad':{'werewolf':-6, 'wolf_cub':-8, 'sorceress':-3, 'tanner':-2, 'vampire':-7, 'cursed':-3, 'lone_wolf':-5, 'minion':-6 }
#                }

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



#card_limits = {'villager':12, 'witch':1, 'pacifist':1, 'p.i':0, 'prince':0, 'seer':1, 'spellcaster':0, 'tough_guy':1, 'lycan':1, 'mason':2, 'old_hag':1, 'mayor':1, 'troublemaker':0,
#                       'village_idiot':1, 'apprentice_seer':1, 'aura_seer':0, 'bodyguard':1, 'cult_leader':1, 'cupid':1, 'diseased':1, 'doppelganger':1, 'drunk':1, 'ghost':0, 'hunter':1,
#                'werewolf':8, 'wolf_cub':1, 'sorceress':1, 'tanner':0, 'vampire':0, 'cursed':1, 'lone_wolf':1, 'minion':1
#                }

card_inclusions = {'villager':[['None']], 'witch':[['None']], 'pacifist':[['None']], 'p.i':[[]], 'prince':[[]], 'seer':[[]], 'spellcaster':[[]], 'tough_guy':[[]], 'lycan':[[]], 'mason':[['mason']], 'old_hag':[[]], 'mayor':[['villager']], 'troublemaker':[[]],
                       'village_idiot':[['None']], 'apprentice_seer':[['seer'],['aura_seer']], 'aura_seer':[[]], 'bodyguard':[[]], 'cult_leader':[[]], 'cupid':[[]], 'diseased':[[]], 'doppelganger':[[]], 'drunk':[[]], 'ghost':[[]], 'hunter':[[]],
                'werewolf':[[]], 'wolf_cub':[['werewolf'],['lone_wolf']], 'sorceress':[['seer']], 'tanner':[[]], 'vampire':[[]], 'cursed':[[]], 'lone_wolf':[['werewolf']], 'minion':[[]]
                }

card_exclusions = {'villager':[], 'witch':[], 'pacifist':['village_idiot'], 'p.i':['seer','apprentice_seer','aura_seer'], 'prince':['mayor'], 'seer':['aura_seer','p.i'], 'spellcaster':[], 'tough_guy':[], 'lycan':[], 'mason':[], 'old_hag':[], 'mayor':['prince','cult_leader'], 'troublemaker':[],
                       'village_idiot':['pacifist'], 'apprentice_seer':['aura_seer', 'p.i','sorceress'], 'aura_seer':['seer','apprentice_seer','p.i'], 'bodyguard':[], 'cult_leader':['mayor','prince'], 'cupid':[], 'diseased':['vampire'], 'doppelganger':[], 'drunk':[], 'ghost':[], 'hunter':[],
                'werewolf':['vampire'], 'wolf_cub':['vampire'], 'sorceress':['aura_seer'], 'tanner':[], 'vampire':['werewolf','wolf_cub','cursed','diseased','minion'], 'cursed':['vampire'], 'lone_wolf':[], 'minion':['vampire']
                }

# n_people = 10 # variable, number of players, or cards in the deck
# target = 0 # variable, the target point value of the returned deck
# threshold = 1 # variable, the 'margin' of freedom for returned deck values

@app.route('/deck/<int:n_people>/<int:target>/<int:threshold>/<string:forced_roles>/<string:black_listed>')
def card_selection(n_people, target, threshold, forced_roles, black_listed): # argv takes optional string arguments for specified cards we want

    global card_exclusions, card_inclusions, card_limits, card_points, cards

    forced_roles = forced_roles.split(' ')
    black_listed = black_listed.split(' ')
    
    roles = []
    for name in cards:
        if name['name'] > 0 or name['name'] in forced_roles:
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

    return jsonify(deck)


@app.route('/roles')
def roles():

    global cards

    return jsonify(cards)
