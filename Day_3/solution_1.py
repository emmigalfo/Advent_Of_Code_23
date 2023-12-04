def is_valid_symbol(char):
    not_symbol = ['1','2','3','4','5','6','7','8','9','0','.']
    return char not in not_symbol

def is_number(char):
    return char.isdigit()

def is_valid_position(x, y, grid_width, grid_height):
    return 0 <= x < grid_width and 0 <= y < grid_height

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

def numbers_touching_symbols(grid, full_nums_dict):
    rows = len(grid)
    cols = len(grid[0])
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0), (1, 1), (1, -1), (-1, 1), (-1, -1)]
    numbers_adjacent_to_symbols = []
    
    for (x, y), number in full_nums_dict.items():
        number_length = len(number)
        number_added = False  

        for i in range(number_length):
            current_x = x + i
            if current_x >= cols: 
                break

            for dx, dy in directions:
                tx, ty = current_x + dx, y + dy
                if is_valid_position(tx, ty, cols, rows) and is_valid_symbol(grid[ty][tx]):
                    numbers_adjacent_to_symbols.append(int(number))
                    number_added = True
                    break  
            
            if number_added:
                break  

    return list(numbers_adjacent_to_symbols)

if __name__ == '__main__':
    file = 'full.txt'
    with open(file, 'r') as f:
        lines = f.read().split('\n')
    full_nums_dict = complete_numbers_indices(lines)
    numbers = numbers_touching_symbols(lines, full_nums_dict)
    print(sum(numbers))