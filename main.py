#7,7 map -->  https://etc.usf.edu/clipart/42600/42671/grid_42671_lg.gif


class Map(object):
    def __init__(self, max_size=[6,6], monster_locations=[[2, 2],[4, 4]], players={}):
        self.size = {'X':[0,max_size[0]],'Y':[0,max_size[1]]}
        self.players = players
        self.monster_locations = monster_locations

    def generate_map(self):
        for cell_x in range(self.size['X'][0],self.size['X'][1]):
            #print('~~~~~~~~~~~~~~~~')
            for cell_y in range(self.size['Y'][0],self.size['Y'][1]):
                #print([cell_x,cell_y])
                if [cell_x,cell_y] in self.monster_locations:
                    face = '👾'
                elif [cell_x,cell_y] in self.player_locations():
                    index = self.player_locations().index([cell_x,cell_y])
                    face =  self.players_icons()[index]
                else:
                    face = '--'
                print(f' {face} ', end="")
            print('\n')

    def player_locations(self):
        return [self.players[n].location for n in self.players]
        
    def players_icons(self):
        return [self.players[n].icon for n in self.players]
        
#for i in range(0,6):
#    print(' - ', end="")
    


class Error(Exception):
   """Base class for other exceptions"""
   pass

class PlayerAlreadyRegistered(Error):
   """A player with that name already exists. Can't add it"""
   pass

class Player(object):
    def __init__(self,name,starting_location,armor,weapon,strenght, stamina,icon,map):
        self.name = name
        self.armor = armor
        self.weapon = weapon
        self.strenght = strenght
        self.level = stamina
        self.icon = icon
        
        self.location = starting_location
        self.map = map
        
        self.register_in_the_map(self.name)
        
    def register_in_the_map(self,name):
        if name not in self.map.players:
            self.map.players[name] = self
        else:
            raise PlayerAlreadyRegistered 
            
    def get_name(self):
        return self.name
        
    def attack(self,player):
        self.weapon.attack(player)
        
    def get_location(self):
        return self.location
        
    def newpos(self,move):
        coord_change = {'N':(0,1), 'S':(0,-1), 'W':(-1,0), 'E':(1,0) }
        move = coord_change[move]
        self.location[0] = self.location[0] + move[0]
        self.location[1] = self.location[1] + move[1]
        return True

        
    def hit(self):
        pass

#class NPC(Player):
#    pass
#    
#class Humans(Player):
#    pass
        
class Weapons(object):
    def __init__(self,weapon_name,weapon_strenght, weapon_use_level):
        self.name = weapon_name
        self.strenght = weapon_strenght
        self.level = weapon_level
        
    def attack(self,player):
        if self.level > 0:
            self.level = self.level -1
            return self.strenght
        else:
            return 0
            
            
#More unicode icons: https://emojipedia.org/

m1 = ['Alien',[2,2],30,'Tentacules',10, 10,'👾']

m2 = {"name":'Shark',"starting_location":[4,4],"armor":5,"weapon":'mouth',"strenght":13, "stamina":10, 'icon': '🦈'}

p1 = ['David',[0,0],30,'axe',10, 10,'🚂']   
p2 = {"name":'Mark',"starting_location":[5,5],"armor":20,"weapon":'knife',"strenght":11, "stamina":10, 'icon':'🏎️'} 
p3 = ['Elliot',[0,5],10,'sword',30, 10,'🚎']   
p4 = {"name":'Marco',"starting_location":[5,0],"armor":5,"weapon":'dagger',"strenght":13, "stamina":10, 'icon': '🚴'}
p5 = ['Felicity',[3,3],40,'shield',14, 10,'🛩️']   
 
l =  [p1,p2,p3,p4,p5]

map = Map()

list_of_players = []
for player in l:
    if type(player) == type([]): 
        list_of_players.append(Player(*player, map=map))
    elif type(player) == type({}):
        list_of_players.append(Player(**player,map=map))
    else:
        print('incorrect input for player')

#print(list_of_players)
#print(map.player_locations())
#print(map.players['David'].location)
map.generate_map()
map.players['David'].newpos('N')
print(map.players['David'].location)
map.generate_map()

#print(map.players['David'])
#print(map.player_locations().index([3,3]))
