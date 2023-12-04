def is_valid_position(x, y, grid_width, grid_height):
    return 0 <= x < grid_width and 0 <= y < grid_height

def is_asterisk(char):
    return char == '*'

def is_number(char):
    return char.isdigit()

def numbers_touching_asterisk(grid, full_nums_dict):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    numbers_adjacent_to_asterisk = {}
    
    for (x, y), number in full_nums_dict.items():
        number_length = len(number)
        number_added = False  

        for i in range(number_length):
            current_x = x + i
            if current_x >= cols: 
                break

            for dx, dy in directions:
                tx, ty = current_x + dx, y + dy
                if is_valid_position(tx, ty, cols, rows) and is_asterisk(grid[ty][tx]):
                    if (tx, ty) not in numbers_adjacent_to_asterisk:
                        numbers_adjacent_to_asterisk[(tx, ty)] = []
                    numbers_adjacent_to_asterisk[(tx,ty)].append(int(number))
                    number_added = True
                    break  
            
            if number_added:
                break  

    return numbers_adjacent_to_asterisk               

def gear_ratio(dictionary):
    gear_ratios=[]
    for gear in dictionary.values():
        if len(gear)==2:
            gear_ratios.append(gear[0]*gear[1])
    return gear_ratios   
            
def complete_numbers_indices(grid):
    nums_dict = {}
    rows = len(grid)
    cols = len(grid[0])
    # right, left
    digits_to_skip = []
    for x in range(cols):
        for y in range(rows):
            if is_number(grid[y][x]) and (x,y) not in digits_to_skip:
                full_number = grid[y][x]
                next_x = x + 1
                while next_x < cols and is_number(grid[y][next_x]):
                    full_number += grid[y][next_x]
                    digits_to_skip.append((next_x,y))
                    next_x += 1
                    
                nums_dict[(x,y)] = full_number

    return nums_dict   

def solution_2(file):
    with open(file, 'r') as f:
        lines = f.read().split('\n')
    full_nums_dict = complete_numbers_indices(lines)
    numbers = numbers_touching_asterisk(lines, full_nums_dict)
    gear_ratios = gear_ratio(numbers)
    return sum(gear_ratios)

if __name__ == '__main__':
    file='full.txt'
    print(solution_2(file))
