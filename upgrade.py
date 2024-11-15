from models.player_action import PlayerAction


def upgrade_low_bases(bases):
    # Check Minimum Level of Bases
    threshold=len(bases)
    actions = []
    for base in bases:
        if(base.level < threshold and base.population >= base.units_until_upgrade):
            actions.append(PlayerAction(base.id, base.id, base.units_until_upgrade))
    return actions 










