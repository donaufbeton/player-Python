from main import BoardAction, Base, PathConfig
from enum import Enum

class EDeviceState(Enum):
    LURE = 0
    ATTACK = 1
    UPGRADE = 2
    RETREAT = 3

class EActionType(Enum):
    UPGRADE = 0
    ATTACK = 1

class ActionWrapper():
    def __init__(self, action_type : EActionType, action_instance : BoardAction, targeted_base : Base, remaining_incerception_time : float):
        self.action_type = action_type
        self.action_instance = action_instance
        self.targeted_base = targeted_base
        self.remaining_incerception_time = remaining_incerception_time

def calculate_travel_loss(distance, path_config : PathConfig):
    return max(((distance - path_config.grace_period) * path_config.death_rate), 0)

def classify_actions(actions : list[BoardAction], all_bases : list[Base]):
    base_dict = {base.uid : base for base in all_bases}
    action_classification = {}
    for action in actions:
        if base_dict[action.src].player == base_dict[action.dest]:
            action_classification[action.uuid] = {
                'type' : EActionType.UPGRADE,
                ''
                'targeted_base' : base_dict[action.dest],
                'targeted_player' : base_dict[action.dest].player,
                'remaining_interception_time' : action.progress.distance - action.progress.traveled
            }
        else:
            action_classification[action.uuid] = ActionWrapper(
                EActionType.ATTACK,
                base_dict[action.dest],
                base_dict[action.dest].player
            )
            
            {
                'type' : EActionType.ATTACK,
                'targeted_base' : base_dict[action.dest],
                'targeted_player' : base_dict[action.dest].player,
                'remaining_interception_time' : action.progress.distance - action.progress.traveled
            }
    return action_classification

# calculate strength on target when successfull
def calculate_strength_on_finish(action_classification):

    pass