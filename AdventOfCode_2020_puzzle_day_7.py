def main():
    with open('D:\ztmDevelop\AdventOfCode_2020\day7input.txt','r') as string:
        file = string.read()
    list = file.splitlines()
    checked_containers = []
    in_check_containers = []
    new_containers = []
    for i in list:
        if (i.find('shiny gold') != -1) and not(i.startswith('shiny gold')):
            new_containers.append(i[:i.index(' bags contain')])
            checked_containers.append(i[:i.index(' bags contain')])
    while new_containers != []:
        in_check_containers += new_containers
        new_containers = []
        for i in in_check_containers:
            for k in list:
                if (k.find(i) != -1) and not(k.startswith(i)):
                    found_any = True
                    if k[:k.index(' bags contain')] not in checked_containers:
                        checked_containers.append(k[:k.index(' bags contain')])
                    if k[:k.index(' bags contain')] not in new_containers:
                        new_containers.append(k[:k.index(' bags contain')])
        in_check_containers = []
    print("part 1's answer: %d bags\n" % len(checked_containers))
    for i in range(len(checked_containers)):
        print(' %d : %s' % (i+1, checked_containers[i]))
    
    # part 2

    for i in list:
        if (i.find('shiny gold') != -1) and (i.startswith('shiny gold')):
            shiny_gold_bag_rule = i
    bag_counter = 0
    shiny_gold_bag_inside_in_check = []
    shiny_gold_bag_inside_new = []
    shiny_gold_bag_inside_checked = []
    for i in range(len(shiny_gold_bag_rule)):
        if shiny_gold_bag_rule[i].isnumeric():
            bag_counter +=  int(shiny_gold_bag_rule[i])
            shiny_gold_bag_inside_new.append(shiny_gold_bag_rule[i:shiny_gold_bag_rule.index(' bag', i)])
            shiny_gold_bag_inside_checked.append(shiny_gold_bag_rule[i:shiny_gold_bag_rule.index(' bag', i)])
    while shiny_gold_bag_inside_new != []:
        shiny_gold_bag_inside_in_check += shiny_gold_bag_inside_new
        shiny_gold_bag_inside_new = []
        for i in shiny_gold_bag_inside_in_check:
            for k in list:
                if (k.find(i[i.index(' ')+1:]) != -1) and (k.startswith(i[i.index(' ')+1:])):
                    for l in range(len(k)):
                        if k[l].isnumeric():
                            bag_counter += (int(k[l]) * int(i[:i.index(' ')]))
                            shiny_gold_bag_inside_checked.append(str(int(k[l]) * int(i[:i.index(' ')])) + k[l+1:k.index(' bag', l+1)])
                            shiny_gold_bag_inside_new.append(str(int(k[l]) * int(i[:i.index(' ')])) + k[l+1:k.index(' bag', l+1)])
        shiny_gold_bag_inside_in_check = []
    print("\n\npart 2's answer: %d\n" % bag_counter)
    for i in range(len(shiny_gold_bag_inside_checked)):
        print(' %d : %s' % (i+1, shiny_gold_bag_inside_checked[i]))

    input()
if __name__ == "__main__":
    main()
