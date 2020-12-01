def main():
    with open('D:\ztmDevelop\day1puzzle.txt','r') as string:
        str = string.read()
    list = ['0']
    n = 0
    for i in str:
        if i != '\n':
            list[n] += i
        else:
            list += '0'
            n += 1

    found = False
    for i in range(len(list)):
        for k in range(len(list)):
            if not(found) and (i != k) and (int(list[i]) + int(list[k]) == 2020):
                print('%d + %d = 2020' % (int(list[i]), int(list[k])))
                print('%d * %d = %d' % (int(list[i]), int(list[k]), int(list[i])*int(list[k])))
                found = True
                
    found = False
    for i in range(len(list)):
        for k in range(len(list)):
            for g in range(len(list)):
                    if not(found) and (i != k) and (i != g) and (g != k) and (int(list[i]) + int(list[k]) + int(list[g]) == 2020):
                        print('%d + %d + %d = 2020' % (int(list[i]), int(list[k]), int(list[g])))
                        print('%d * %d * %d = %d' % (int(list[i]), int(list[k]), int(list[g]), int(list[i])*int(list[k])*int(list[g])))
                        found = True
    input()
if __name__ == "__main__":
    main()
