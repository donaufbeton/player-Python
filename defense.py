from main import BoardAction, Base, PathConfig
from enum import Enum

class EDeviceState(Enum):
    IDLE = 0
    ATTACK = 1
    UPGRADE = 2
    RETREAT = 3

class EActionType(Enum):
    UPGRADE = 0
    ATTACK = 1

class ActionWrapper():
    def __init__(self, action_type : EActionType, action_instance : BoardAction, targeted_base : Base, targeted_player : str, remaining_incerception_time : float):
        self.action_type = action_type
        self.action_instance = action_instance
        self.targeted_base = targeted_base
        self.targeted_player = targeted_player
        self.remaining_incerception_time = remaining_incerception_time

def calculate_travel_loss(distance, path_config : PathConfig):
    return max(((distance - path_config.grace_period) * path_config.death_rate), 0)

def classify_actions(actions : list[BoardAction], all_bases : list[Base]):
    base_dict = {base.uid : base for base in all_bases}
    action_classification = {}
    for action in actions:
        target_base = base_dict[action.dest]
        if target_base not in action_classification.keys():
            action_classification[target_base] = []
        action_classification[target_base].append(
            ActionWrapper(
                EActionType.UPGRADE if base_dict[action.src].player == base_dict[action.dest] else EActionType.ATTACK,
                action,
                base_dict[action.dest],
                base_dict[action.dest].player,
                action.progress.distance - action.progress.traveled,
            )
        )
    return action_classification

# calculate strength on target when successfull
def get_attacks_on_allies(own_player_id, allied_bases : list[Base], classified_actions : dict[Base, ActionWrapper]):
    for base in allied_bases:
        critical_actions : list[ActionWrapper] = [wrapper for wrapper in classified_actions[base] if wrapper.action_type == EActionType.ATTACK]
        if len(critical_actions) == 0:
            pass
        else:
            impact_timeline = list(map(lambda x: (x.remaining_incerception_time, x.action_instance.amount), critical_actions))
            impact_timeline = sorted(impact_timeline, lambda x: x[0])
            # estmate casualties per instance & calculate survivors

def get_joink_targets():
    pass

def conquer():
    pass