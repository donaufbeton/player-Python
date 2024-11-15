from typing import List
from models.game_state import GameState
from models.base import Base 
from models.player_action import PlayerAction


def upgrade_low_bases(bases):
    # Check Minimum Level of Bases
    threshold=len(bases) + 1 
    actions = []
    for base in bases:
        if(base.level < threshold):
            if (base.population >= base.units_until_upgrade):
                actions.append(PlayerAction(base.id, base.id, base.units_until_upgrade))
            else:
                actions.append(PlayerAction(base.id, base.id, min(base.population,5)))
    return actions 

def get_own_and_enemy_bases(bases : list[Base], player):
    own_bases=[]
    enemy_bases=[]

    for base in bases:
        if(base.player == player):
            own_bases.append(base)
        else:
            enemy_bases.append(base)

    
    return own_bases, enemy_bases


def decide(gameState: GameState) -> List[PlayerAction]:

    player = 1000
    # Upgrade if possible
    own_bases, enemy_bases = get_own_and_enemy_bases(gameState.bases, player)
    actions = upgrade_low_bases(own_bases)
    return [actions]
