




def check_upgrade(bases):
    # Check Minimum Level of Bases
    threshold=len(bases)
    bases_to_be_upgraded = []

    for base in enumerate(bases):
        if(base.level < threshold):
            bases_to_be_upgraded.append(base)
    return bases_to_be_upgraded


def upgrade(bases):

    upgrade_bases = [] 
    for base in bases: 
        if base.population >= base.units_until_upgrade:
            upgrade_bases.append()

    return upgrade_bases 

