def decimalToBinary(num):  
    bin_num =  bin(num).replace("0b", "0" * (36  - len(bin(num).replace("0b", ""))))
    return bin_num
    
def binaryToDecimal(binary): 
    binary1 = binary 
    decimal, i, n = 0, 0, 0
    while(binary != 0): 
        dec = binary % 10
        decimal = decimal + dec * pow(2, i) 
        binary = binary//10
        i += 1
    return decimal

def mask_change(current_mask, given_value):
    listed_value = [char for char in given_value]
    for char in range(len(current_mask)):
        if current_mask[char] != 'X':
            listed_value[char] = current_mask[char] 
    return binaryToDecimal(int(''.join(listed_value)))

def mask_change_part_2(current_mask, given_value):
    listed_value = [char for char in given_value]
    for char in range(len(current_mask)):
        if current_mask[char] == 'X' or current_mask[char] == '1':
            listed_value[char] = current_mask[char] 
    listed_value = ''.join(listed_value)
    X_counter = 0
    for i in range(len(listed_value)):
        if listed_value[i] == 'X':
            X_counter += 1
    list_of_adresses = [listed_value] + [listed_value]
    X_number = 1
    while X_number <= X_counter:
        for i in range(0, len(list_of_adresses) // 2):
            list_of_adresses[i] = list_of_adresses[i].replace('X', '0', 1)
        for i in range(len(list_of_adresses) // 2, len(list_of_adresses)):
            list_of_adresses[i] = list_of_adresses[i].replace('X', '1', 1)
        X_number += 1
        if X_number <= X_counter:
            list_of_adresses = list_of_adresses * 2
    return list_of_adresses

def main():
    with open('day14input.txt','r') as string:
        file = string.read()
    lines = file.splitlines()
    mask = ''
    memory = {}
    for i in lines:
        if i.startswith('mask'):
            mask = i[7:]
        else:
            key = i[4:i.index(']')]
            value = mask_change(mask, decimalToBinary(int(i[i.index('= ')+2:])))
            memory[key] = value
    sum = 0
    for i in memory:
        sum += memory[i]
    print(sum)
    
    # PART 2
    
    mask = ''
    memory = {}
    for i in lines:
        if i.startswith('mask'):
            mask = i[7:]
        else:
            key_adresses = mask_change_part_2(mask, decimalToBinary(int(i[4:i.index(']')])))
            value = int(i[i.index('= ')+2:])
            for i in key_adresses:
                memory[i] = value
    sum = 0
    for i in memory:
        sum += memory[i]
    print(sum)

    input()
if __name__ == "__main__":
    main()
