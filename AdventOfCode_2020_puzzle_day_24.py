from pprint import pprint

def adjecant_tiles(tile_x, tile_y):
    adjecants = [f'{tile_x + 1},{tile_y}', f'{tile_x - 1},{tile_y}', f'{tile_x + 0.5},{tile_y + 0.5}', f'{tile_x + 0.5},{tile_y - 0.5}', f'{tile_x - 0.5},{tile_y + 0.5}', f'{tile_x -0.5},{tile_y - 0.5}',]
    return adjecants

def main():
    with open('C:\ztmDevelop\AdventOfCode_2020\day24input.txt','r') as string:
        file = string.read()
    instructions = file.splitlines()
    w = 'white'
    b = 'black'
    tiles= {}
    tiles['0.0,0.0'] = w
    for line in instructions:
        x_counter = 0.0
        y_counter = 0.0
        for char in range(len(line)):
            if line[char] == 'e' and line[char - 1] != 'n' and line[char - 1] != 's':
                x_counter += 1
            elif line[char] == 'w' and line[char - 1] != 'n' and line[char - 1] != 's':
                x_counter -= 1
            elif line[char] == 's':
                if line[char +1 ] == 'e':
                    x_counter += 0.5
                    y_counter -= 0.5
                elif line[char +1 ] == 'w':
                    x_counter -= 0.5
                    y_counter -= 0.5
            elif line[char] == 'n':
                if line[char +1 ] == 'e':
                    x_counter += 0.5
                    y_counter += 0.5
                elif line[char +1 ] == 'w':
                    x_counter -= 0.5
                    y_counter += 0.5
        name = f'{x_counter},{y_counter}'
        if name not in tiles:
            tiles[name] = b
        elif tiles[name] == b:
            tiles[name] = w
        else:
            tiles[name] = b
        adjecants = []
    counter = 0
    for tile in tiles:
        if tiles[tile] == b:
            counter += 1
    print(f'--PART 1-- The answer is: {counter}')

    # Part 2

    for i in range(100):
        to_be_added = {}
        for tile in tiles:
            x_counter = float(tile[0:tile.index(',')])
            y_counter = float(tile[tile.index(',') + 1:])
            adjecants = adjecant_tiles(x_counter, y_counter)
            for name in adjecants:
                if name not in tiles:
                    to_be_added[name] = w
        tiles = tiles | to_be_added
        to_be_flipped = {}
        for tile in tiles:
            x_counter = float(tile[0:tile.index(',')])
            y_counter = float(tile[tile.index(',') + 1:])
            adjecants = adjecant_tiles(x_counter, y_counter)
            b_counter = 0
            for name in adjecants:
                if name in tiles and tiles[name] == b:
                        b_counter += 1
            if tiles[tile] == b:
                if b_counter == 0 or b_counter > 2:
                    to_be_flipped[tile] = w
            elif tiles[tile] == w and b_counter == 2:
                to_be_flipped[tile] = b
        for tile in to_be_flipped:
            tiles[tile] = to_be_flipped[tile]
    counter = 0
    for tile in tiles:
        if tiles[tile] == b:
            counter += 1
    print(f'--PART 2-- The answer is: {counter}')
    input()

if __name__ == "__main__":
    main()
