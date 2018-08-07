import random
import json

from Room import Room
import ww
from flask import Flask, jsonify, abort, request, render_template
from flask_cors import CORS, cross_origin
from flask_socketio import SocketIO, send, join_room, leave_room

app = Flask(__name__)
CORS(app)
socketio = SocketIO(app)


@socketio.on('message')
def handleMessage(msg):
    print('Message: ' + msg)
    send(msg, broadcast=True)


@socketio.on('join')
def join(data):
    username = data['username']
    roomName = data['room']

    for room in currentRooms:
        if roomName == room.name:
            join_room(roomName)
            room.addMember(request.sid, username)
            send(username + ' has entered the room.', room=roomName)
            return
    send(username + ' tried to enter a invalid room', broadcast=True)


@socketio.on('modJoin')
def modJoin(data):
    room = Room(data['name'] + str(random.randint(1, 999)), request.sid)
    currentRooms.append(room)
    join_room(room.name)
    send(data['name'] + ' has created the room ' + room.name, broadcast=True)


@socketio.on('genDeck')
def genDeck(data):
    for room in currentRooms:
        if room.isOwner(request.sid):
            selected = ww.card_selection(len(room.players), 0, 5, [], [], room.players)
            send(str(selected), room=request.sid)
            for key, value in selected.items():
                send("Your role is:" + value, room=key)


@socketio.on('disconnect')
def disconnect():
    for room in currentRooms:
        if room.owner == request.sid:
            send(room.name + " has been closed", broadcast=True)
            currentRooms.remove(room)


@app.route('/')
def index():
    return render_template('index.html')


if __name__ == '__main__':
    socketio.run(app)

# Will contain a object containing the name of the room and a list of players
currentRooms = []

cards = [
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

card_inclusions = {
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

card_exclusions = {
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


@app.route('/deck/<int:n_people>/<int:target>/<int:threshold>', methods=['GET', 'POST'])
def card_selection(n_people, target, threshold):
    global card_exclusions, card_inclusions, cards

    request_body = request.get_json()

    if not request.json:
        abort(400)

    forced_roles = request_body['forced_roles']
    black_listed = request_body['black_listed']

    roles = []

    for name in cards:

        if name['limit'] > 0 or name['name'] in forced_roles:

            if name['name'] not in black_listed:
                roles.append(name['name'])

    deck_points = None
    target_range = list(range(target - threshold, target + threshold + 1))

    while deck_points not in target_range:

        deck = []
        deck_points = 0

        for forced_role in forced_roles:
            deck.append(forced_role)

        while len(deck) < n_people:

            role_error = False
            role = random.choice(roles)

            role_info = {}

            for a in range(0, len(cards)):

                if cards[a]['name'] == role:
                    role_info = cards[a]

            if role in black_listed:
                continue

            if deck.count(role) == role_info['limit']:
                role_error = True

            if role_error is True:
                continue

            for exclusion in card_exclusions[role]:

                if exclusion in deck:
                    role_error = True

                    break

            if role_error is True:
                continue

            for inclusions in card_inclusions[role]:

                if 'None' in inclusions:
                    break

                absent_inclusions = []

                for inclusion in inclusions:

                    if inclusion in deck:
                        continue

                    if inclusion not in deck:
                        absent_inclusions.append(inclusion)

                if len(absent_inclusions) + len(deck) + 1 <= n_people:

                    for a in absent_inclusions:
                        deck.append(a)

                    break

                if len(absent_inclusions) + len(deck) + 1 > n_people:
                    role_error = True

            if role_error is True:
                continue

            deck.append(role)

            for b in range(0, len(deck)):

                for c in range(0, len(cards)):

                    if deck[b] == cards[c]['name']:
                        deck_points = deck_points + cards[c]['weight']

    return jsonify(deck)


@app.route('/roles')
def roles():
    global cards

    return jsonify(cards)
