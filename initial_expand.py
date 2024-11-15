from attack import *



def get_nearest_ten_percent(bases, src_dst_map):
    ten_percent_of_bases = len(bases)*0.1
    return src_dst_map[:ten_percent_of_bases]
    

def filter_empty_bases(cut_src_dst_map):
    empty_bases = []
    
    for base in cut_src_dst_map:
        if (base.population == 0):
            empty_bases.append(base)

    return empty_bases






def get_best_base_to_conquer(all_bases, enemy_bases):

    for enemy_base in enemy_bases:
        if (base.population== 0):
            for base         

    pass
    



if __name__ == "__main__":
    print("wawa")
    

