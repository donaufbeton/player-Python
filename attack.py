import math

from models.base import Base

player="peach"
grace_period = 10
own_bases, enemy_bases = get_own_and_enemy_bases(bases)

def get_distance(x_1, y_1, z_1, x_2, y_2, z_2):
    return math.floor(math.sqrt((x_1-x_2)**2 + (y_1-y_2)**2 + (z_1-z_2)**2))

# Würde ich ändern und hier direct 
def get_own_and_enemy_bases(bases):
    own_bases=[]
    enemy_bases = []

    for base in bases:
        if(base.player == player):
            own_bases.append(base)
        else:
            enemy_bases.append(base)

    
    return own_bases, enemy_bases



def nearest_enemies(bases):
    
    #own_base, enemy_base, distance
    distance_map={}
    
    


    for own_base in own_bases:
        distance_map[own_base] = {}
        for enemy_base in enemy_bases:
            distance_map[own_base][enemy_base] = get_distance(own_base.Position.x, own_base.Position.y, own_base.Position.z,
             enemy_base.Position.x, enemy_base.Position.y, enemy_base.Position.z)



    return distance_map      


def attack_possible(bases):
   
   
    distance_map = nearest_enemies(bases)
    
    return 0
    

    


if __name__ == "__main__":
    print(get_distance(0,0,1,0,0,2))