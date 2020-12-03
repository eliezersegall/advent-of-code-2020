def tree_encounter_count(slope, map):
    """AdventOfCode day 3 - tree encounter puzzle
    This function will count and will RETURN a number of how many tree we will encounter
    based on: the puzzle input (aka the trees' map), the chosen slope
    and of course, the fact that we start at the top-left corner 
    and traverse the map all the way to the bottom.
    :param slope: Two numbers which indicates the amount of right steps and down steps
    we take before each encounter
    :type slope: tuple
    :param map: The AdventOfCode puzzle input seperate to a list
    :type map: list
    :return: The number of trees we will encounter in the chosen slope.
    :rtype: int"""
    tree_counter = 0
    step_counter = 0
    for i in range(0,len(map) - slope[1],slope[1]):
        step_counter += slope[0]
        if map[i+slope[1]][step_counter % len(map[0])] == '#':
            tree_counter += 1
    return (tree_counter)

def main():
    with open('D:\ztmDevelop\day3input.txt','r') as string:
        str = string.read()
    list = ['']
    counter = 0
    for i in str:
        if i != '\n':
            list[counter] += i
        else:
            counter += 1
            list.append('')
    SLOPE_1_1 = (1,1)
    SLOPE_3_1 = (3,1)
    SLOPE_5_1 = (5,1)
    SLOPE_7_1 = (7,1)
    SLOPE_1_2 = (1,2)
    slope_1_1_tree_num = (tree_encounter_count(SLOPE_1_1, list))
    slope_3_1_tree_num = (tree_encounter_count(SLOPE_3_1, list))
    slope_5_1_tree_num = (tree_encounter_count(SLOPE_5_1, list))
    slope_7_1_tree_num = (tree_encounter_count(SLOPE_7_1, list))
    slope_1_2_tree_num = (tree_encounter_count(SLOPE_1_2, list))
    slopes_tree_nums_product = ((slope_1_1_tree_num) * (slope_3_1_tree_num) * (slope_5_1_tree_num) * (slope_7_1_tree_num) * (slope_1_2_tree_num))
    print('slope: right 1, down 1: %d trees will be encountered.' % (slope_1_1_tree_num))
    print('slope: right 3, down 1: %d trees will be encountered.' % (slope_3_1_tree_num))
    print('slope: right 5, down 1: %d trees will be encountered.' % (slope_5_1_tree_num))
    print('slope: right 7, down 1: %d trees will be encountered.' % (slope_7_1_tree_num))
    print('slope: right 1, down 2: %d trees will be encountered.' % (slope_1_2_tree_num))
    print("\nAll tree encounters\' numbers multiplied: %d * %d * %d * %d * %d = %d" % ((slope_1_1_tree_num), (slope_3_1_tree_num), (slope_5_1_tree_num), (slope_7_1_tree_num), (slope_1_2_tree_num), (slopes_tree_nums_product)))
    input()
if __name__ == "__main__":
    main()