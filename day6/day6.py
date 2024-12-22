import requests
import os 
from dotenv import load_dotenv



def parse_data(input_data):
    data = [list(line) for line in input_data.splitlines()]
    return data

def find_position(board):
    position = None
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == '^':
                position = (i, j)
                break
    
    return position
    
    
def find_distinct_positions(board):
    
    rows, cols = len(board), len(board[0])
    positions = set()
    
    directions = {0:(-1,0), 1: (0,1), 2:(1,0), 3:(0,-1)}
    
    
    current_direction = 0
    
    current_position = find_position(board)

    if not current_position:
        raise ValueError("The current position is None")
    
    
    while True:
        
        positions.add(current_position)
        
        x, y = current_position
        dx, dy = directions[current_direction]
        
        nx, ny = x+dx, y+dy
        
        
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols: # this means we are out of bounds 
            break
        
        elif board[nx][ny] == '#':
            current_direction = (current_direction + 1)% 4
        
        else:
            current_position = (nx, ny)
    
    return len(positions)


def simulate_guard(board):
    
    rows, cols = len(board), len(board[0])
    
    visited = set()
    directions = {0:(-1,0), 1: (0,1), 2:(1,0), 3:(0,-1)}
    current_direction = 0
    current_position = find_position(board)
    
    
    while True:
        if(current_position, directions[current_direction]) in visited:
            return True
        visited.add((current_position, directions[current_direction]))
        
        x, y = current_position
        dx, dy = directions[current_direction]
        
        nx, ny = x+dx, y+dy
        
        if nx < 0 or nx >= rows or ny < 0 or ny >= cols:
            return False
        
        elif board[nx][ny] != "#":
            current_position = (nx, ny)
        
        else:
            current_direction = (current_direction+1) % 4
            

def calculate_obstructions(board):
    rows, cols = len(board), len(board[0])
    count = 0
    
    for i in range(rows):
        for j in range(cols):
            if board[i][j] == ".":
                board[i][j] = "#"
                if simulate_guard(board):
                    count += 1
                board[i][j] = "."
                
    return count
    





if __name__ == "__main__":

    load_dotenv()
    SESSION_COOKIE = os.getenv("AOC_SESSION")

    # Replace with the day of the challenge you want to fetch input for
    DAY = 6
    YEAR = 2024

    # URL to fetch the input
    url = f"https://adventofcode.com/{YEAR}/day/{DAY}/input"

    # Headers with your session cookie
    headers = {
        "Cookie": f"session={SESSION_COOKIE}"
    }

    input_data = None


    try:
        response = requests.get(url, headers=headers)
        if response.status_code == 200:
            input_data = response.text
        else:
            print(f"failed to fetch input {response.status_code} {response.text}")
            
    except Exception as e:
        print(f"An Error occured {e}")
        
        
    board = parse_data(input_data)
    # print(len(board) * len(board[0]))
    
    # res = find_distinct_positions(board)
    res = calculate_obstructions(board)
    print(res)