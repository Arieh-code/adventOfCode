

def load_grid(filename):
    grid = []
    
    with open(filename, 'r') as file:
        
        for line in file:
            grid.append(list(line.strip()))
            
    return grid




def find_xmas1(filename):
    
    grid = load_grid(filename)
    
    rows, cols = len(grid), len(grid[0])
    target = "XMAS"
    directions = [
        (-1, -1),(-1,0),(-1, 1),(0, -1),(0, 1),(1, -1),(1, 0),(1, 1)
    ]
    
    count = 0
    
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    
    def search(x, y, dx, dy):
        for i in range(len(target)):
            nx, ny = x + i*dx , y + i * dy
            
            if not is_valid(nx, ny) or grid[nx][ny] != target[i]:
                return False
            
        return True
    
    
    
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'X':
                for x, y in directions:
                    if search(i, j, x, y):
                        count+=1
                        
                        
    return count

def find_xmas2(filename):
    grid = load_grid(filename)
    rows, cols = len(grid), len(grid[0])
    count = 0
    diagonals = [
        [(-1, -1), (1, 1)],
        [(-1, 1), (1, -1)]
    ]
    
    
    def is_valid(x, y):
        return 0 <= x < rows and 0 <= y < cols
    
    def check_xmas(x, y):
        """Check if both diagonals form a valid X-MAS pattern."""
        nonlocal count

        # Coordinates for both diagonals
        top_left, bottom_right = diagonals[0]
        top_right, bottom_left = diagonals[1]

        # Get diagonal positions
        nx1, ny1 = x + top_left[0], y + top_left[1]
        nx2, ny2 = x + bottom_right[0], y + bottom_right[1]
        nx3, ny3 = x + top_right[0], y + top_right[1]
        nx4, ny4 = x + bottom_left[0], y + bottom_left[1]

        # Check if all positions are valid
        if not (is_valid(nx1, ny1) and is_valid(nx2, ny2) and is_valid(nx3, ny3) and is_valid(nx4, ny4)):
            return

        # Get characters on diagonals
        char1 = grid[nx1][ny1]
        char2 = grid[nx2][ny2]
        char3 = grid[nx3][ny3]
        char4 = grid[nx4][ny4]

        # Check if both diagonals form a valid X-MAS pattern
        if ((char1 == 'M' and char2 == 'S') or (char1 == 'S' and char2 == 'M')) and \
           ((char3 == 'M' and char4 == 'S') or (char3 == 'S' and char4 == 'M')):
            count += 1
            
            
    for i in range(rows):
        for j in range(cols):
            if grid[i][j] == 'A':
                check_xmas(i, j) 
    
    return count 

filename = "day4.txt"

# result = find_xmas1(filename)
result2 = find_xmas2("test.txt")

print(result2)