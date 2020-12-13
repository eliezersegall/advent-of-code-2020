def main():
    with open('day13input.txt','r') as string:
        file = string.read()
    two_lines = file.splitlines()
    earliest_timestamp = int(two_lines[0])
    busses = two_lines[1].split(',')
    while 'x' in busses:
        busses.remove('x')
    list_of_mods = []
    for i in range(len(busses)):
        busses[i] = int(busses[i])
        stamp_cycle = 0
        while stamp_cycle < earliest_timestamp:
            stamp_cycle += busses[i]
        list_of_mods.append(stamp_cycle - earliest_timestamp)
    earliest_bus = busses[list_of_mods.index(min(list_of_mods))]
    minutes = min(list_of_mods)
    print(f'--PART 1-- The answer is {earliest_bus} * {minutes} = {earliest_bus * minutes}')

    # PART 2
    
    busses = two_lines[1].split(',')
    list_of_exact_minute_stamps = []
    for i in range(len(busses)):
        if busses[i] != 'x':
            busses[i] = int(busses[i])
            list_of_exact_minute_stamps.append(i)
    while 'x' in busses:
        busses.remove('x')
    mixed_list = []
    for i in range(len(busses)):
        mixed_list.append([busses[i], list_of_exact_minute_stamps[i]])
    not_found = True
    i = 756261400000000 + max(busses) - (756261400000000 % max(busses)) # after a loooooooooooong run of the loop, I have placed this number for my input so the loop won't run too much... not the best solution, but you can always wait several hours... XD
    print(mixed_list)
    print(i)
    while not_found:
        for j in mixed_list:
            if (i - list_of_exact_minute_stamps[busses.index(max(busses))] + j[1]) % j[0] != 0:
                i += max(busses)
                not_found = True
                break
            else:
                not_found = False
    print(f'--PART 2-- The answer is {i - list_of_exact_minute_stamps[busses.index(max(busses))]}')
                
                

        
    

    input()
if __name__ == "__main__":
    main()
