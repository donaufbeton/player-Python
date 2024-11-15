import unittest
import uuid
from logic.strategy import decide
from models.base import Base
from models.base_level import BaseLevel
from models.board_action import BoardAction
from models.game import Game
from models.game_config import GameConfig, PathConfig
from models.game_state import GameState
from models.player_action import PlayerAction
from models.position import Position
from models.progress import Progress


from attack import *

"""

class TestStrategy(unittest.TestCase):

    def test_decide(self):
        test_base = Base(0, "test base", 1, 100, 1, 200, Position(0, 0, 0))

        test_game_state = GameState(
            [BoardAction(uuid.uuid4(), 0, 1, 2, 100, Progress(10, 4))],
            [test_base],
            GameConfig([BaseLevel(0, 0, 0)], PathConfig(0, 0)),
            Game(0, 0, 2, 2, 0),
        )

        want = PlayerAction(0, 0, 0)

        result = decide(test_game_state)
        self.assertEqual(str(want), str(result))

"""

class TestNearestEnemy(unittest.TestCase):

    def test_decide(self):

        own_base = Base(1, "peach", 3, 100, 1, 200, Position(1, 1, 1))
        test_base = Base(0, "test base", 0, 100, 1, 200, Position(0, 0, 0))

        test_game_state = GameState(
            [BoardAction(uuid.uuid4(), 0, 1, 2, 100, Progress(10, 4))],
            [test_base],
            GameConfig([BaseLevel(0, 0, 0)], PathConfig(0, 0)),
            Game(0, 0, 2, 2, 0),
        )


        print(nearest_enemies(own_base, test_base))




if __name__ == "__main__":
    unittest.main()
