def length_of_all_fields(fields_order_list):
    lengths_sum = 0
    for i in range(len(fields_order_list)):
        lengths_sum += len(fields_order_list[i])
    return lengths_sum
    
    

def main():
    with open('D:\ztmDevelop\AdventOfCode_2020\day16input.txt','r') as string:
        file = string.read()
    puzzle = file.split('\n\n')
    fields = puzzle[0].splitlines()
    leftfield_left_margins, leftfield_right_margins, rightfield_left_margins, rightfield_right_margins = [], [], [], []
    for i in range(len(fields)):
        leftfield_left_margins.append(fields[i][fields[i].index(': ') + 2: fields[i].index('-')])
        leftfield_right_margins.append(fields[i][fields[i].index('-') + 1: fields[i].index(' or')])
        rightfield_left_margins.append(fields[i][fields[i].index(' or') + 3: fields[i].rindex('-')])
        rightfield_right_margins.append(fields[i][fields[i].rindex('-') + 1:])
    combined_leftfield_left_margin = int(min(leftfield_left_margins))
    combined_leftfield_right_margin = int(max(leftfield_right_margins))
    combined_rightfield_left_margin = int(min(rightfield_left_margins))
    combined_rightfield_right_margin = int(max(rightfield_right_margins))
    nearby_tickets = puzzle[2].splitlines()
    nearby_tickets.remove(nearby_tickets[0])
    sum_of_invalid_numbers = 0
    invalid_ticket_numbers = [] # for part 2 
    for i in range(len(nearby_tickets)):
        nearby_tickets[i] = nearby_tickets[i].split(',')
        for j in range(len(nearby_tickets[i])):
            nearby_tickets[i][j] = int(nearby_tickets[i][j])
            if not ((combined_leftfield_left_margin <= nearby_tickets[i][j] <= combined_leftfield_right_margin) or (combined_rightfield_left_margin <= nearby_tickets[i][j] <= combined_rightfield_right_margin)):
                sum_of_invalid_numbers += nearby_tickets[i][j]
                if i not in invalid_ticket_numbers:   # for part 2
                    invalid_ticket_numbers.append(i)  # for part 2
                
    print(f'Answer for part 1: {sum_of_invalid_numbers}\n')

    # PART 2
    nearby_valid_tickets = []
    for i in range(len(nearby_tickets)):
        if i not in invalid_ticket_numbers:
            nearby_valid_tickets.append(nearby_tickets[i])
    tickets_fields = []
    fields_order = []
    for i in range(len(fields)):
        tickets_fields.append([])
        fields_order.append([])
    for i in range(len(nearby_valid_tickets)):
        for j in range(len(nearby_valid_tickets[i])):
            tickets_fields[j].append(nearby_valid_tickets[i][j])
    for i in range(len(tickets_fields)):
        for j in range(len(fields)):
            fit = True
            for k in range(len(tickets_fields[i])):
                if not ((int(leftfield_left_margins[j]) <= tickets_fields[i][k] <= int(leftfield_right_margins[j])) or (int(rightfield_left_margins[j]) <= tickets_fields[i][k] <= int(rightfield_right_margins[j]))):
                    fit = False
            if fit:
                fields_order[i].append(fields[j][:fields[j].index(':')])
    while length_of_all_fields(fields_order) != 20:
        for i in range(len(fields_order)):
            if len(fields_order[i]) != 1:
                for j in range(len(fields_order[i])):
                    in_more = 0
                    for k in range(len(fields_order)):
                        if k != i:
                            if fields_order[i][j] in fields_order[k]:
                                in_more += 1
                    if in_more == 0:
                        fields_order[i] = [fields_order[i][j]]
                        break
    for i in range(len(fields_order)):
        fields_order[i] = fields_order[i][0]
    your_ticket = puzzle[1].splitlines()[1]
    your_ticket = your_ticket.split(',')
    product = 1
    for i in range(len(your_ticket)):
        your_ticket[i] = int(your_ticket[i])
        if fields_order[i].startswith('departure'):
            product *= your_ticket[i]
    print(f'Answer for part 2: {product}')
    
                
    input()
if __name__ == "__main__":
    main()
