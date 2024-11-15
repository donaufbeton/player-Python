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










