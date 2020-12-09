def main():
    with open('day9input.txt','r') as string:
        file = string.read()
    numbers_list = file.splitlines()
    for i in range(len(numbers_list)):
        numbers_list[i] = int(numbers_list[i])
    invalid_num = 0
    for i in range(25, len(numbers_list)):
        found = False
        preable = []
        for j in range(i - 25, i):
            preable.append(numbers_list[j])
        for k in preable:
            for l in preable:
                if k != l and k + l == numbers_list[i]:
                    found = True
        if not(found):
            print(f'First invalid number is: {numbers_list[i]}')
            invalid_num = numbers_list[i]
            break
            
    # Part 2
    
    for i in range(len(numbers_list)):
        sum = 0
        contiguous_set = []
        for j in range(i, len(numbers_list)):
            while sum < invalid_num:
                sum += numbers_list[j]
                contiguous_set.append(numbers_list[j])
                j += 1
            if sum == invalid_num and len(contiguous_set) > 1:
                print(f'Encryption\'s weakness is: {max(contiguous_set) + min(contiguous_set)}')
            break


    
    
    input()
if __name__ == "__main__":
    main()
