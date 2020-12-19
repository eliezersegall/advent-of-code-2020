def line_clean(lines_input):
    for line in range(len(lines_input)):
        lines_input[line] = lines_input[line].split(' ')
    for n in range(3):
        for line in range(len(lines_input)):
            i = 0
            while i < len(lines_input[line]):
                if lines_input[line][i].startswith('(') and len(lines_input[line][i]) != 1:
                    lines_input[line].insert(i, '(')
                    lines_input[line][i+1] = lines_input[line][i+1][1:]
                    i += 2
                elif lines_input[line][i].endswith(')') and len(lines_input[line][i]) != 1:
                    lines_input[line].insert(i+1, ')')
                    lines_input[line][i] = lines_input[line][i][:-1]
                    i+= 2
                else:
                    i += 1
    return lines_input

def local_cal(string):
    for n in range(len(string)):
        if string[n] == '+' or string[n] == '*':
            first_oper_index = n
            break
    for n in range(len(string)-1,0,-1):
        if string[n] == '+' or string[n] == '*':
            last_oper_index = n
            break
    result = int(string[0:first_oper_index])
    i = first_oper_index
    while i < len(string):
        if string[i] == '+':
            for k in range(i+1,len(string)):
                if string[k] == '+' or string[k] == '*':
                    result += int(string[i+1:k])
                    i = k
                    break
        elif string[i] == '*':
            for k in range(i+1,len(string)):
                if string[k] == '+' or string[k] == '*':
                    result *= int(string[i+1:k])
                    i = k
                    break
        if i == n:
            if string[i] == '+':
                result += int(string[i+1:])
            else:
                result *= int(string[i+1:])
            break
    return result     

def local_cal_part_2(ex):
    n = 0
    while n < len(ex):
        if ex[n] == '+':
            ex[n+1] = int(ex[n-1]) + int(ex[n+1])
            del ex[n-1:n+1]
        else:
            n += 1
    n = 0
    while n < len(ex):
        if ex[n] == '*':
            ex[n+1] = int(ex[n-1]) * int(ex[n+1])
            del ex[n-1:n+1]
        else:
            n += 1
    return ex[0]

def line_cal(current_line):
    while '(' in current_line and ')' in current_line:
        left = 0
        right = 0
        for i in range(len(current_line)):
            if current_line[i] == ')':
                right = i
                for j in range(i,-1,-1):
                    if current_line[j] == '(':
                        left = j
                        break
                break
        local_val = local_cal(''.join(current_line[left + 1:right]))
        current_line[right] = str(local_val)
        del current_line[left:right]
    current_line = local_cal(''.join(current_line))
    return current_line

def line_cal_part_2(current_line):
    while '(' in current_line and ')' in current_line:
        left = 0
        right = 0
        for i in range(len(current_line)):
            if current_line[i] == ')':
                right = i
                for j in range(i,-1,-1):
                    if current_line[j] == '(':
                        left = j
                        break
                break
        local_val = local_cal_part_2(current_line[left + 1:right])
        current_line[right] = str(local_val)
        del current_line[left:right]
    current_line = local_cal_part_2(current_line)
    return current_line


def main():
    with open('day18input.txt','r') as string:
        file = string.read()
    lines = file.splitlines()
    lines =  line_clean(lines)
    lines_sum = 0
    for line in lines:
        lines_sum += line_cal(line)
    
    print(f'--PART 1-- The answer is: {lines_sum}\n')

    # PART 2 
    
    lines = file.splitlines()
    lines =  line_clean(lines)
    lines_sum = 0
    for line in lines:
        lines_sum += line_cal_part_2(line)
    
    print(f'--PART 2-- The answer is: {lines_sum}')

    input()
if __name__ == "__main__":
    main()
