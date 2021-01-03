from collections import defaultdict 
def main():
    with open('day21input.txt','r') as string:
        file = string.read()
    food = file.splitlines()
    for i, line in enumerate(food):
        food[i] = [line[:line.index(' (contains')].split(' '), line[line.index('contains')+9:-1].split(', ')]
    allergens = defaultdict(list)
    allergens_sorted = defaultdict(list)
    for i in range(len(food)):
        for allergen in food[i][1]:
            allergens[allergen].append(food[i][0])
    for allergen in allergens:
        for line in allergens[allergen]:
            for ingredient in line:
                in_all = True
                for otherline in allergens[allergen]:
                    if otherline != line:
                        if ingredient not in otherline:
                            in_all = False
                            break
                if in_all and ingredient not in allergens_sorted[allergen]:
                    allergens_sorted[allergen].append(ingredient)
    all_are_found = False
    while not all_are_found:
        all_are_found = True
        for allergen in allergens_sorted:
            if len(allergens_sorted[allergen]) == 1:
                ingredient = allergens_sorted[allergen][0]
                for other_allergen in allergens_sorted:
                    if other_allergen != allergen:
                        if ingredient in allergens_sorted[other_allergen]:
                            del allergens_sorted[other_allergen][allergens_sorted[other_allergen].index(ingredient)]
            else:
                all_are_found = False
    allergens = []
    for allergen in sorted(allergens_sorted):
        allergens.append(allergens_sorted[allergen][0])
    counter = 0
    for i in range(len(food)):
        for ingredient in food[i][0]:
            if ingredient not in allergens:
                counter += 1
    print(f'--Part 1-- The answer is: {counter}')
    canonical_dangerous_ingredient_list = ''
    for allergen in allergens:
        canonical_dangerous_ingredient_list += allergen + ','
    print(f'--Part 2-- The answer is: {canonical_dangerous_ingredient_list[:-1]}')
    input()
if __name__ == "__main__":
    main()
