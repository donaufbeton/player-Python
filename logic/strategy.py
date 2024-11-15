from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction
from attack import get_own_and_enemy_bases 
from upgrade import upgrade_low_bases


def decide(gameState: GameState) -> List[PlayerAction]:

    player = 1000
    # Upgrade if possible
    own_bases, enemy_bases = get_own_and_enemy_bases(gameState.bases, player)
    actions = upgrade_low_bases(own_bases)

    return [actions]
