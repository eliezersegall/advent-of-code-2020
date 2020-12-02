def main():
    with open('day2puzzle.txt','r') as string:
        str = string.read()
    valid_counter_1 = 0
    valid_counter_2 = 0
    threes_divider_counter = 0 #with it I will make a seperate list inside the main list for each password with its policy
    list = [['','','','']]
    n = 0
    for i in str:
        if (i != ' ') and (i != ':') and (i != '-') and (i != '\n'):
            list[n][threes_divider_counter] += i
        elif (i == ' ') or (i == '-'):
            threes_divider_counter += 1
        if (i == '\n'):
            threes_divider_counter = 0
            n += 1
            list.append(['','','',''])

    for i in range(len(list)):
        min = int(list[i][0])
        max = int(list[i][1])
        letter = list[i][2]
        letter_counter = 0
        for k in list[i][3]:
            if (k == letter):
                letter_counter += 1
        if (letter_counter >= min) and (letter_counter <= max):
            valid_counter_1 += 1
    
    for i in range(len(list)):
        position_1 = int(list[i][0])
        position_2 = int(list[i][1])
        letter = list[i][2]
        letter_position_counter = 0
        if letter == list[i][3][position_1 - 1]:
            letter_position_counter+=1
        if letter == list[i][3][position_2 - 1]:
            letter_position_counter+=1
        if letter_position_counter == 1:
            valid_counter_2 += 1
    print ('number of valid passwords according to first policy: %d' % (valid_counter_1))
    print ('number of valid passwords according to second policy: %d' % (valid_counter_2))
    input()
if __name__ == "__main__":
    main()
