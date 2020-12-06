def main():
    with open('day5input.txt','r') as string:
        str = string.read()
    list = str.split('\n')
    max = 0
    row = 0
    column = 0
    seat_id = 0
    list_of_ids = []
    your_seat_id = 0
    for i in range(len(list)):
        list[i]=[list[i][:-3],list[i][7:]]
        left_margin = 0
        right_margin = 127
        for k in range(len(list[i][0]) - 1):
            if (list[i][0][k] == 'F'):
                right_margin = (left_margin + right_margin)//2
            else:
                left_margin = (left_margin + right_margin)//2 + 1
        if (list[i][0][-1] == 'F'):
            row = left_margin
        else:
            row = right_margin
        left_margin = 0
        right_margin = 7
        for k in range(len(list[i][1]) - 1):
            if (list[i][1][k] == 'L'):
                right_margin = (left_margin + right_margin)//2
            else:
                left_margin = (left_margin + right_margin)//2 + 1
        if (list[i][1][-1] == 'L'):
            column = left_margin
        else:
            column = right_margin
        seat_id = row * 8 + column
        list_of_ids.append(seat_id)
        if (seat_id > max):
            max = seat_id
    list_of_ids.sort()
    for i in range(len(list_of_ids)-1):
        if list_of_ids[i+1] - list_of_ids[i] != 1:
            your_seat_id = list_of_ids[i+1] - 1
    print('Highest seat ID: %d' % max)
    print('Your seat ID: %d' % your_seat_id)

    input()
if __name__ == "__main__":
    main()
