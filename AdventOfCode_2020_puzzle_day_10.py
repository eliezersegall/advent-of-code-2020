def main():
    with open('day10input.txt','r') as string:
        file = string.read()
    numbers_list = file.splitlines()
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])
    numbers_list.sort()
    numbers_list.insert(0,0)
    numbers_list.append(numbers_list[-1]+3)
    jolt_1_counter = 0
    jolt_3_counter = 0
    for i in range(1,len(numbers_list)):
        if numbers_list[i] - numbers_list[i-1] == 1:
            jolt_1_counter += 1
        elif numbers_list[i] - numbers_list[i-1] == 3:
            jolt_3_counter += 1
    print(f'1: {jolt_1_counter}  3: {jolt_3_counter}')
    print(f'The answer for part 1 is {jolt_3_counter * jolt_1_counter}')

    # Part 2

    numbers_list = file.splitlines()
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])
    numbers_list.sort()
    numbers_list.insert(0,0)
    numbers_list.append(numbers_list[-1] + 3)
    list_of_opt_nums = []
    for i in range(1, len(numbers_list) - 1):
        if numbers_list[i+1] - numbers_list[i-1] == 2:
            if list_of_opt_nums == []:
                list_of_opt_nums.append([numbers_list[i]])
            else:
                if list_of_opt_nums[-1][-1] == numbers_list[i-1]:
                    list_of_opt_nums[-1].append(numbers_list[i])
                else:
                    list_of_opt_nums.append([numbers_list[i]])
    num_of_valid_ways = 1
    for i in list_of_opt_nums:
        if len(i) == 1:
            num_of_valid_ways *= 2
        elif len(i) == 2:
            num_of_valid_ways *= 4
        elif len(i) == 3:
            num_of_valid_ways *= 7
    print(f'\nThere are {num_of_valid_ways} distinct ways we can arrange the adapters to connect the charging outlet to the device')
        


    input()
if __name__ == "__main__":
    main()
