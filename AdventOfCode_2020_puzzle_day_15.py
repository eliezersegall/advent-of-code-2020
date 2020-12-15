def main():
    puzzle_input = '0,8,15,2,12,1,4'
    num_list = puzzle_input.split(',')
    print('Solution is in process. Please wait several seconds...')
    for i in range(30000000 - len(num_list)):
        num_list.append('')
    seen = {}
    for i in range(len(num_list)):
        seen[num_list[i]] = i
    for i in range(len(puzzle_input.split(',')), len(num_list)):
        if  num_list[i-1] in seen.keys():
            num_list[i] += str(i - 1 - seen[num_list[i-1]])
            seen[num_list[i-1]] = i-1
            '''for j in range(i-2,-1,-1):
                if num_list[j] == num_list[i-1]:
                    anymore = True
                    nearest_position = j
                    break'''  
        else:
            num_list[i] = '0'
            seen[num_list[i-1]] = i-1
    print(f'2020th number is: {num_list[2020-1]}')
    print(f'30000000th number is: {num_list[30000000-1]}')
        
    

    input()
if __name__ == "__main__":
    main()
