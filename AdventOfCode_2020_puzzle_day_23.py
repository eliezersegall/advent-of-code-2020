def cycle(cups_input):
    minimum = min(cups_input)
    maximum = max(cups_input)
    picked = cups_input[1:4]
    del cups_input[1:4]
    destination_value = cups_input[0] - 1
    if destination_value == 0:
        destination_value = maximum
    while destination_value in picked:
        if destination_value > minimum:
            destination_value -= 1
        else:
            destination_value = maximum
    destination = cups_input.index(destination_value) + 1
    cups_input[destination : destination] = picked
    cups_input.append(cups_input[0])
    del cups_input[0]
    return cups_input
                
def round(ring, current):
    maximum = 1000000
    minimum = 1
    next = ring[current]
    outside = [None, None, None]
    for x in range(3):
        outside[x] = next
        next = ring[next]
    ring[current] = next
    dest = current - 1
    if dest == 0:
        dest = maximum
    while dest in outside:
        if dest > minimum:
            dest = dest - 1
        else:
            dest = maximum
    stitch = ring[dest]
    ring[dest] = outside[0]
    ring[outside[2]] = stitch
    return ring, next
    
def main():
    with open('day23input.txt','r') as string:
        file = string.read()
    cups = [int(i) for i in list(file)]
    for i in range(100):
        cups = cycle(cups)
    cups = [str(cups[i]) for i in range(len(cups))]
    print(f"--Part 1-- The answer is: {int(''.join(cups[cups.index('1')+1:] + cups[:cups.index('1')]))}")
 
    # PART 2
    
    cups = [int(x) for x in list(file)]
    for x in range(max(cups), 1000000):
        cups.append(x+1)

    current = cups[0]
    ring = {}
    for i in range(len(cups)):
        if i == len(cups) - 1:
            ring[cups[i]] = cups[0]
        else:
            ring[cups[i]] = cups[i+1]

    for x in range(10000000):
        ring, current = round(ring, current)

    print(f"--Part 2-- The answer is: {ring[1]*ring[ring[1]]}")
    input()
    
if __name__ == "__main__":
    main()
