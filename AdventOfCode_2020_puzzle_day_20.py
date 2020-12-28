from collections import defaultdict
from pprint import pprint
import math

def rotateR(num, tile):
    index = num
    if index > 0:
        new_tile = []
        for i in range(len(tile[0])):
            new_tile.append('')
            for line in tile[-1::-1]:
                new_tile[-1] += line[i]
        index -= 1
    if index > 0:
        new_tile = rotateR(index, new_tile)
    if index == num:
        return tile
    else:
        return new_tile

def flip(num, tile):
    if num == 1:
        new_tile = []
        for line in tile[-1::-1]:
            new_tile.append(line)
        return new_tile
    else:
        return tile

def check_valid_rl(tile1, tile2):
    right_border = ''
    left_border = ''
    for line in tile1:
        right_border += line[-1]
    for line in tile2:
        left_border += line[0]
    if right_border == left_border:
        return True
    else:
        return False

def check_valid_ud(tile1, tile2):
    down_border = tile1[-1]
    up_border = tile2[0]
    if down_border == up_border:
        return True
    else:
        return False

def is_neighbor_down(tile1, tile2):
    for f1 in range(2):
        for r1 in range(4):
            if check_valid_ud(tile1, flip(f1, rotateR(r1, tile2))):
                return (True, r1, f1)
                break
    else:
        return False

def is_neighbor_right(tile1, tile2, first_tiles):
    if first_tiles:
        for f1 in range(2):
            for f2 in range(2):
                for r1 in range(4):
                    for r2 in range(4):
                        if check_valid_rl(flip(f1, rotateR(r1, tile1)), flip(f2, rotateR(r2, tile2))):
                            return(True, r1, f1, r2, f2)
                            break
    else:
        for f1 in range(2):
            for r1 in range(4):
                if check_valid_rl(tile1, flip(f1, rotateR(r1, tile2))):
                            return(True, r1, f1)
                            break
        else:
            return False

def remove_borders(tile):
    new_tile = tile[1:-1]
    for line in range(len(new_tile)):
        new_tile[line] = new_tile[line][1:-1]
    return new_tile

def sea_monster_check(appearances, area):
    fit = True
    for i in range(3):
        for appearance in appearances[i]:
            if area[i][appearance] != '#':
                fit = False
    return fit
    
def main():
    with open('day20input.txt','r') as string:
        file = string.read()
    tiles = {}
    list_of_ids = []
    tile_borders = []
    for tile in file.split('\n\n'):
        tile_id = tile.splitlines()[0][tile.splitlines()[0].index(' ') + 1: -1]
        tiles[int(tile_id)] = tile.splitlines()[1:]
    for tile in tiles:
        list_of_ids.append(tile)
        tile_borders.append([])
        tile_borders[-1].append(tiles[tile][0])
        tile_borders[-1].append(tiles[tile][-1])
        tile_borders[-1].append(tiles[tile][0][-1::-1])
        tile_borders[-1].append(tiles[tile][-1][-1::-1])
        right_border = ''
        left_border = ''
        for line in tiles[tile]:
            right_border += line[-1]
            left_border += line[0]
        tile_borders[-1].append(right_border)
        tile_borders[-1].append(left_border)
        tile_borders[-1].append(right_border[-1::-1])
        tile_borders[-1].append(left_border[-1::-1])
    product = 1
    edges = [] #----
    neighbors = defaultdict(list)
    for tile_id_index in range(len(list_of_ids)):
        counter = 0
        for local_border in tile_borders[tile_id_index]:
            for block in range(len(tile_borders)):
                if block != tile_id_index:
                    if local_border in tile_borders[block]:
                        if list_of_ids[block] not in neighbors[list_of_ids[tile_id_index]]:
                            neighbors[list_of_ids[tile_id_index]].append(list_of_ids[block]) 
                        counter += 1
        if counter == 4:
            product *= list_of_ids[tile_id_index]
            edges.append(list_of_ids[tile_id_index]) #----
    print(f'--PART 1-- The answer is: {product}')
    
    # Part 2

    puzzle = [[edges[0]]]
    list_of_used = [edges[0]]
    length = int(math.sqrt(len(tiles)))
    for neighbor in neighbors[puzzle[-1][-1]]:
        if neighbor not in list_of_used:
            if is_neighbor_right(tiles[puzzle[-1][-1]], tiles[neighbor], True)[0]:
                r1, f1, r2, f2 = is_neighbor_right(tiles[puzzle[-1][-1]], tiles[neighbor], True)[1:]
                puzzle[-1].append(neighbor)
                list_of_used.append(neighbor)
                tiles[edges[0]] = flip(f1, rotateR(r1, tiles[edges[0]]))
                tiles[neighbor] = flip(f2, rotateR(r2, tiles[neighbor]))
                break
    while len(puzzle) != length or len(puzzle[-1]) != length:
        edge_checker = 0
        for edge in edges:
            if edge in list_of_used:
                edge_checker += 1
        if edge_checker == 4:
            break
        while len(puzzle[-1]) != length:
            for neighbor in neighbors[puzzle[-1][-1]]:
                if neighbor not in list_of_used:
                    if is_neighbor_right(tiles[puzzle[-1][-1]], tiles[neighbor], False):
                        r1, f1 = is_neighbor_right(tiles[puzzle[-1][-1]], tiles[neighbor], False)[1:]
                        puzzle[-1].append(neighbor)
                        list_of_used.append(neighbor)
                        tiles[neighbor] = flip(f1, rotateR(r1, tiles[neighbor]))
                        break
        else:
            puzzle.append([])
            for neighbor in neighbors[puzzle[-2][0]]:
                if neighbor not in list_of_used:
                    if is_neighbor_down(tiles[puzzle[-2][0]], tiles[neighbor]):
                        r1, f1 = is_neighbor_down(tiles[puzzle[-2][0]], tiles[neighbor])[1:]
                        puzzle[-1].append(neighbor)
                        list_of_used.append(neighbor)
                        tiles[neighbor] = flip(f1, rotateR(r1, tiles[neighbor]))
                        break
    del puzzle[-1]
    image = ['']
    for tile in tiles:
        tiles[tile] = remove_borders(tiles[tile])
    for line in range(len(puzzle)):
        for tile in range(len(puzzle[line])):
            puzzle[line][tile] = tiles[puzzle[line][tile]]
    for block_line in range(len(puzzle)):
        for line in range(len(puzzle[0][0])):
            for block in range(len(puzzle[0])):
                image[-1] += puzzle[block_line][block][line]
                if len(image[-1]) == len(puzzle[0][0][0]) * len(puzzle[0]):
                    image.append('')
    del image[-1]
    SEA_MONSTER = '''                  # 
#    ##    ##    ###
 #  #  #  #  #  #   '''.splitlines()
    appearances = [[],[],[]]
    for i in range(len(SEA_MONSTER)):
        for j in range(len(SEA_MONSTER[i])):
                if SEA_MONSTER[i][j] == '#':
                        appearances[i].append(j)
    roughness = 0
    for line in image:
        for char in line:
            if char == '#':
                roughness += 1
    monsters = 0
    flip_check = 0
    rotate_check = 0
    while monsters == 0:
        for line in range(len(image)-3):
            for char in range(len(image[0])-len(SEA_MONSTER[0])):
                area = [image[line][char:char + 21],image[line+1][char:char + 21],image[line+2][char:char + 21]]
                if sea_monster_check(appearances, area):
                    monsters += 1
        if monsters == 0:
            if flip_check == 0:
                image = flip(1, image)
                flip_check += 1
            elif rotate_check != 3:
                image = rotateR(1, image)
                rotate_check += 1
    print(f'--PART 2-- The answer is: {roughness - (monsters * 15)}')

    input()
if __name__ == "__main__":
    main()
