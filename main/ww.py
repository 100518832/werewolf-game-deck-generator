import random


class DeckGenerator:

    def __init__(self):
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

    def deck_generation(self,
                        n_people=10,
                        target=0,
                        threshold=0,
                        forced_roles=[],
                        black_listed=[],
                        ):

        '''
        :param n_people: int, default: 10, controls the number of cards to be placed into a deck
        :param target: int, default: 0, this controls the sum of all the weights (points) of the cards in a deck
        :param threshold: int, this allows the generator to return a deck with a total point value target +/- threshold
        :param forced_roles: list, shape: len =< n, this will force certain roles to be played into deck. Forced roles
        can override existing rules on roles not being played together.
        :param black_listed: list, shape: no restriction, all roles that will not be placed into a deck during selection
        :return: deck, List, a list of strings, each corresponding to a specific card / role in the deck.
        '''

        if type(n_people) != int:
            raise TypeError('n_people must be of type int, type {} found instead'.format(type(n_people)))

        elif type(target) != int:
            raise TypeError('target must be of type int, type {} found instead'.format(type(target)))

        elif type(threshold) != int:
            raise TypeError('threshold must be of type int, type {} found instead'.format(type(threshold)))

        elif type(forced_roles) != list:
            raise TypeError('forced_roles must be of type list, type {} found instead'.format(type(forced_roles)))

        elif type(black_listed) != list:
            raise TypeError('black_listed must be of type list, type {} found instead'.format(type(black_listed)))

        elif len(black_listed) >= len(self.cards):
            raise IndexError('length, {}, for black_listed can not be greater than number of possible unique roles'.format(len(black_listed)))

        elif len(forced_roles) > n_people:
            raise IndexError('length, {}, for forced roles can not be greater than n_people'.format(len(forced_roles)))

        roles = []
        black_listed = list(set(black_listed))

        for name in self.cards:
            if name['limit'] > 0 or name['name'] in forced_roles:
                if name['name'] not in black_listed:
                    roles.append(name['name'])

        deck_points = None
        target_range = list(range(target - threshold, target + threshold + 1))

        while deck_points not in target_range or deck_points is None:

            deck = []
            deck_points = 0

            for forced_role in forced_roles:
                deck.append(forced_role)

            while len(deck) < n_people:

                role_error = False
                role = random.choice(roles)

                role_info = {}

                for a in range(0, len(self.cards)):
                    if self.cards[a]['name'] == role:
                        role_info = self.cards[a]

                if role in black_listed:
                    continue

                if deck.count(role) == role_info['limit']:  # if the # unique roles in the deck are equal too the role limit, then we can can not add this card

                    role_error = True

                if role_error is True:
                    continue

                for exclusion in self.card_exclusions[role]:  # exclusion is a single role
                    if exclusion in deck:
                        role_error = True
                        break

                if role_error is True:
                    continue

                for inclusions in self.card_inclusions[role]:  # inclusions is a nested list, card_inclusions[role] is a list of lists
                    if 'None' in inclusions:  # if this role does not require any other cards to be added, it can be appeneded to the deck
                        break

                    absent_inclusions = []

                    for inclusion in inclusions:  # inclusion is a single role that must come with the selected role, and inclusions in a list of roles
                        if inclusion in deck:
                            continue

                        if inclusion not in deck:
                            absent_inclusions.append(inclusion)

                    if len(absent_inclusions) + len(deck) + 1 <= n_people:
                        for a in absent_inclusions:  # a is a role
                            deck.append(a)
                        break

                    if len(absent_inclusions) + len(deck) + 1 > n_people:
                        role_error = True

                if role_error is True:
                    continue

                deck.append(role)

            deck_points = 0
            for role in deck:
                for card in self.cards:
                    if card['name'] == role:
                        deck_points += card['weight']

        if deck is None:
            raise ValueError('Result Deck is None')

        elif type(deck) != list:
            raise TypeError('deck must be of type list, type {} found instead'.format(type(deck)))

        elif len(deck) != n_people:
            raise IndexError('Length, {}, for deck invalid. Length of deck must be equal to n_people'.format(len(deck)))

        elif sum([card['weight'] for card in self.cards if card['name'] in deck]) not in list(range(target-threshold, target+threshold+1)):
            raise ValueError('Point value of deck does not fall within the target range.')

        return deck



