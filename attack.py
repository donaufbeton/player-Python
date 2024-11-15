import math

from models.base import Base, Position
from models.game_config import PathConfig
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

def calculate_casualties(path_config : PathConfig, distance : float):
    return max(((distance - path_config.grace_period) * path_config.death_rate), 0)

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
    


if __name__ == "__main__":

    own_bases, enemy_bases=get_own_and_enemy_bases(Base)


    # print(get_distance(0,0,1,0,0,2))