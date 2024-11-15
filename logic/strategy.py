from typing import List
from models.game_state import GameState
from models.player_action import PlayerAction


def decide(gameState: GameState) -> List[PlayerAction]:
    # TODO: place your logic here

    player = 1000
    own_bases, enemy_bases = get_own_and_enemy_bases(game_state.bases, player)
    actions = upgrade_base(check_upgrade(own_bases))

    return [actions]
