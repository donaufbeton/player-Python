import math

from models.base import Base, Position

#noch abändern
player=3




def get_distance(x_1, y_1, z_1, x_2, y_2, z_2):
    return math.floor(math.sqrt((x_1-x_2)**2 + (y_1-y_2)**2 + (z_1-z_2)**2))

def get_distance(a : Position, b : Position):
    return math.floor(math.sqrt((a.x-b.x)**2 + (y_1-y_2)**2 + (z_1-z_2)**2))

# Würde ich ändern und hier direct 
def get_own_and_enemy_bases(bases):
    own_bases=[]
    enemy_bases=[]

    for base in bases:
        if(base.player == player):
            own_bases.append(base)
        else:
            enemy_bases.append(base)

    
    return own_bases, enemy_bases



def nearest_enemies(own_bases, enemy_bases):
    
    #own_base, enemy_base, distance
    distance_map={}
    

    for own_base in own_bases:
        distance_map[own_base] = {}
        for enemy_base in enemy_bases:
            distance_map[own_base][enemy_base] = get_distance(own_base.Position.x, own_base.Position.y, own_base.Position.z,
            enemy_base.Position.x, enemy_base.Position.y, enemy_base.Position.z)
           
    
    #nach distance_map sortieren

    return distance_map      


def attack_possible(distance_map):
   
    bases_where_attack_possible = []
    grace_period = 10
    for base in distance_map:
        for enemy_base in distance_map[base]:
            distance = distance_map[base][enemy_base]

            if (distance < grace_period and base.population > enemy_base.population):
                bases_where_attack_possible.append()


    
    
    return bases_where_attack_possible
    

    


if __name__ == "__main__":

    own_bases, enemy_bases=get_own_and_enemy_bases(Base)
    distance_map = nearest_enemies(own_bases, enemy_bases)

    print(get_distance(0,0,1,0,0,2))