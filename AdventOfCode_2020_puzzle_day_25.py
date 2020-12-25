def main():
    with open('day25input.txt','r') as string:
        file = string.read()
    public_keys = [int(i) for i in file.splitlines()]
    loop_sizes = [0,0]
    print('The program is in process. Please wait a few seconds...\n')
    for i in range(len(public_keys)):
        value = 1
        j = 0
        while value != public_keys[i]:
            value *= 7
            value %= 20201227
            j += 1
        loop_sizes[i] += j
    value = 1
    for j in range(loop_sizes[0]):
        value *= public_keys[1]
        value %= 20201227
    encryption = value
    print(f'The encryption key is: {encryption}')
    
    
    input()
    
if __name__ == "__main__":
    main()