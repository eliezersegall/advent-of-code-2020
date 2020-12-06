def main():
    with open('day6input.txt','r') as string:
        str = string.read()
    list = str.split('\n\n')
    part_1_sum = 0
    for i in range(len(list)):
        list[i] = list[i].replace('\n','')
        for k in range(97, 123):
            list[i] = list[i].replace(chr(k),'',list[i].count(chr(k))-1)
        part_1_sum += len(list[i])
    print("The sum of all groups' answers: %d" % part_1_sum)
    part_2_sum = 0
    list = str.split('\n\n')
    l_list = str.split('\n\n')
    for i in range(len(list)):
        list[i] = list[i].replace('\n','')
        l_list[i] = l_list[i].split('\n')
        for k in range(97, 123):
            if list[i].count(chr(k)) == len(l_list[i]):
                part_2_sum += 1
    
    print("The sum of all groups' SHARED answers: %d" % part_2_sum)

    input()
if __name__ == "__main__":
    main()
