def sub_game(index, list1, list2):
    local_previous1 = []
    local_previous2 = []
    while len(list1) > 0 and len(list2) > 0:
        if list1 not in local_previous1 and list2 not in local_previous2:
            local_previous1.append(list1[:])
            local_previous2.append(list2[:])
            if list1[0] <= len(list1) - 1 and list2[0] <= len(list2) - 1:
                if sub_game(index+1, list1[1:list1[0] + 1], list2[1:list2[0] + 1]) == 1:
                    list1 += (list1[0], list2[0])
                    del list1[0]
                    del list2[0]
                else:
                    list2 += (list2[0], list1[0])
                    del list1[0]
                    del list2[0]
            else:
                if list1[0] > list2[0]:
                    list1 += (list1[0], list2[0])
                    del list1[0]
                    del list2[0]
                elif list1[0] < list2[0]:
                    list2 += (list2[0], list1[0])
                    del list1[0]
                    del list2[0]
        else:
            list2 = []
            break
    if len(list1) == 0:
        return 2
    else:
        return 1

def game(part,player1,player2):
    if part == 1:
        while len(player1) > 0 and len(player2) > 0:
            if player1[0] > player2[0]:
                player1 += (player1[0], player2[0])
                del player1[0]
                del player2[0]
            elif player1[0] < player2[0]:
                player2 += (player2[0], player1[0])
                del player1[0]
                del player2[0]
        score = 0
        if len(player1) == 0:
            player2.reverse()
            for i in range(len(player2)):
                score += player2[i] * (i+1)
        elif len(player2) == 0:
            player1.reverse()
            for i in range(len(player1)):
                score += player1[i] * (i+1)
        return score
    else:
        previous1 = []
        previous2 = []
        while len(player1) > 0 and len(player2) > 0:
            if player1 not in previous1 and player2 not in previous2:
                previous1.append(player1[:])
                previous2.append(player2[:])
                if player1[0] <= len(player1) - 1 and player2[0] <= len(player2) - 1:
                    if sub_game(1, player1[1:player1[0] + 1], player2[1:player2[0] + 1]) == 1:
                        player1 += (player1[0], player2[0])
                        del player1[0]
                        del player2[0]
                    else:
                        player2 += (player2[0], player1[0])
                        del player1[0]
                        del player2[0]
                else:
                    if player1[0] > player2[0]:
                        player1 += (player1[0], player2[0])
                        del player1[0]
                        del player2[0]
                    elif player1[0] < player2[0]:
                        player2 += (player2[0], player1[0])
                        del player1[0]
                        del player2[0]
            else:
                player2 = []
                break
        score = 0
        if len(player1) == 0:
            player2.reverse()
            for i in range(len(player2)):
                score += player2[i] * (i+1)
        elif len(player2) == 0:
            player1.reverse()
            for i in range(len(player1)):
                score += player1[i] * (i+1)
        return score          
                
def main():
    with open('D:\ztmDevelop\AdventOfCode_2020\day22input.txt','r') as string:
        file = string.read()
    deck1 = file.split('\n\n')[0].splitlines()[1:]
    deck2 = file.split('\n\n')[1].splitlines()[1:]
    for i in range(len(deck1)):
        deck1[i] = int(deck1[i])
    for i in range(len(deck2)):
        deck2[i] = int(deck2[i])
    print(f'--PART 1-- The answer is: {game(1, deck1, deck2)}')

    # PART 2 
    
    deck1 = file.split('\n\n')[0].splitlines()[1:]
    deck2 = file.split('\n\n')[1].splitlines()[1:]
    for i in range(len(deck1)):
        deck1[i] = int(deck1[i])
    for i in range(len(deck2)):
        deck2[i] = int(deck2[i])
    print(f'--PART 2-- The answer is: {game(2, deck1, deck2)}')


    input()
if __name__ == "__main__":
    main()