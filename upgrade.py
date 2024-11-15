from models.player_action import PlayerAction


def check_upgrade(bases):
    # Check Minimum Level of Bases
    threshold=len(bases)
    bases_to_be_upgraded = []

    for base in bases:
        if(base.level < threshold):
            bases_to_be_upgraded.append(base)
    return bases_to_be_upgraded 


def upgrade_base(bases):
    actions = []
    for base in bases: 
        if base.population >= base.units_until_upgrade:
            actions.append(PlayerAction(base.id, base.id, base.units_until_upgrade))

    return actions 









