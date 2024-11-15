import math

from models.base import Base, Position
from itertools import product

#noch abändern
player=3

def get_distance(a : Position, b : Position):
    return math.floor(math.sqrt((a.x-b.x)**2 + (a.y-b.y)**2 + (a.z-b.z)**2))

def prioritize_opponents(own_bases : list[Base], enemy_bases : list[Base]):
    src_dst_map = {}
    for src in own_bases:
        distances = [(dst, get_distance(src, dst)) for dst in enemy_bases]
        distances.sort(lambda x: x[1])
        src_dst_map[src] = distances
    return src_dst_map

def calculate_casualties(distance):
    pass

# Würde ich ändern und hier direct 
def get_own_and_enemy_bases(bases : list[Base]):
    own_bases=[]
    enemy_bases=[]

    for base in bases:
        if(base.player == player):
            own_bases.append(base)
        else:
            enemy_bases.append(base)

    
    return own_bases, enemy_bases


def nearest_enemies(own_bases : list[Base], enemy_bases : list[Base]):
    #own_base, enemy_base, distance
    distance_map={}
    

    for own_base in own_bases:
        distance_map[own_base] = {}
        for enemy_base in enemy_bases:
            distance_map[own_base][enemy_base] = get_distance(own_base.position, enemy_base.position)
           
    
    #nach distance_map sortieren

    return distance_map      


    


if __name__ == "__main__":

    own_bases, enemy_bases=get_own_and_enemy_bases(Base)
    distance_map = nearest_enemies(own_bases, enemy_bases)

    # print(get_distance(0,0,1,0,0,2))