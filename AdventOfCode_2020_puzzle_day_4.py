def main():
    with open('D:\ztmDevelop\AdventOfCode_2020\day4input.txt','r') as string:
        str = string.read()
    list = str.split('\n\n')
    list_of_dicts = [] 
    for i in range(len(list)):
        list[i] = list[i].replace('\n',' ') # making list of fixed passports with no in-lines.
        list[i] = list[i].split(' ')# making each passport into a seperate list, thus making list of lists.
        list_of_dicts.append({})
        for k in range(len(list[i])):
            list_of_dicts[i][list[i][k][:3]] = list[i][k][4:]# trandforming all passports from lists to dicts and storing them all in a new list.
    part_1_valid_counter = 0
    part_2_valid_counter = 0
    checker = True
    for i in range(len(list_of_dicts)):
        checker = True
        if (len(list_of_dicts[i]) == 8) or (len(list_of_dicts[i]) == 7) and not('cid' in list_of_dicts[i].keys()):
            part_1_valid_counter += 1
            if not(1920 <= int(list_of_dicts[i]['byr']) <= 2002):
                checker = False
            if not(2010 <= int(list_of_dicts[i]['iyr']) <= 2020):
                checker = False
            if not(2020 <= int(list_of_dicts[i]['eyr']) <= 2030):
                checker = False
            if not((list_of_dicts[i]['hgt'].endswith('cm')) and (150 <= int(list_of_dicts[i]['hgt'][:-2]) <= 193)) and not((list_of_dicts[i]['hgt'].endswith('in')) and (59 <= int(list_of_dicts[i]['hgt'][:-2]) <= 76)):
                checker = False
            if not(list_of_dicts[i]['hcl'].startswith('#')):
                checker = False
            elif not(len(list_of_dicts[i]['hcl']) == 7):
                checker = False
            else:
                for k in range(6):
                    if not('a' <= list_of_dicts[i]['hcl'][k+1] <= 'f') and not('0' <= list_of_dicts[i]['hcl'][k+1] <= '9'):
                        checker = False
            if (list_of_dicts[i]['ecl'] != 'amb') and (list_of_dicts[i]['ecl'] != 'blu') and (list_of_dicts[i]['ecl'] != 'brn') and (list_of_dicts[i]['ecl'] != 'gry') and (list_of_dicts[i]['ecl'] != 'grn') and (list_of_dicts[i]['ecl'] != 'hzl') and (list_of_dicts[i]['ecl'] != 'oth'):
                checker = False
            if (len(list_of_dicts[i]['pid']) != 9):
                checker = False
            elif not(list_of_dicts[i]['pid'].isnumeric()):
                checker = False
            if checker == True:
                part_2_valid_counter += 1
    print('There are %d valid passports according to part 1.' % part_1_valid_counter)
    print('There are %d valid passports according to part 2.' % part_2_valid_counter)
    input()
if __name__ == "__main__":
    main() 