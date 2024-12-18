import requests
from dotenv import load_dotenv
import os
from collections import defaultdict, deque

  
    
def is_valid_update(update, graph):
    positions = {page: i for i, page in enumerate(update)}
    
    for x in graph:
        for y in graph[x]:
            if x in positions and y in positions and positions[x] > positions[y]:
                return False
    return True
    

def parse_input(input_text):
    parts = input_text.split("\n\n")
    rules = parts[0].splitlines()
    update = [list(map(int, line.split(','))) for line in parts[1].splitlines()]
    
    return rules, update


def build_graph(rules):
    graph = defaultdict(set)
    
    for rule in rules:
        x, y = map(int, rule.split("|"))
        graph[x].add(y)
    
    return graph


def find_correct_updates(input_text):
    rules, updates = parse_input(input_text)
    graph = build_graph(rules)
    
    correct_updates = []
    
    for update in updates:
        if is_valid_update(update, graph):
            correct_updates.append(update)
            
    middle_sum = sum(update[len(update)//2] for update in correct_updates)
    
    return middle_sum


def reorder_update(update, graph):
    subgraph = defaultdict(set)
    indegree = defaultdict(int)
    
    for x in update:
        if x in graph:
            for y in graph[x]:
                if y in update:
                    subgraph[x].add(y)
                    indegree[y] += 1
                    
        if x not in indegree:
            indegree[x] = 0
            
    
    queue = deque([node for node in update if indegree[node] == 0])
    sorted_update = []
    
    while(queue):
        current_node = queue.popleft()
        sorted_update.append(current_node)
        
        for neighbor in subgraph[current_node]:
            
            indegree[neighbor] -= 1
            
            if indegree[neighbor] == 0:
                queue.append(neighbor)
    
    
    return sorted_update
            
            


def fix_false_updates(input_text):
    rules, updates = parse_input(input_text)
    graph = build_graph(rules)
    
    fixed_updates = []
    
    for update in updates:
        if not is_valid_update(update, graph):
            fixed_update = reorder_update(update, graph)
            fixed_updates.append(fixed_update)
            
    middle_sum = sum(update[len(update)//2] for update in fixed_updates)
    
    return middle_sum 


if __name__ == "__main__":
    
    load_dotenv()
    SESSION_COOKIE = os.getenv("AOC_SESSION")

    # Replace with the day of the challenge you want to fetch input for
    DAY = 5
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
        
        
    # res = find_correct_updates(input_data)
    res = fix_false_updates(input_data)
    print(res)
        