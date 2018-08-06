import struct

class Room(object):
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.players = {}

    def isOwner(self,id):
        if id == self.owner:
            return True
        else:
            return False
    def addMember(self,playerid,playername):
        self.players[playerid] = playername
