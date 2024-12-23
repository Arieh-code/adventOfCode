import requests
import os
from dotenv import load_dotenv
from itertools import product


def parse_data(input_data):
    targets = []
    numbers = []
    
    for i in input_data.splitlines():
        target, number = i.split(":")
        target = int(target.strip())
        number = list(map(int, number.split()))
        
        targets.append(target)
        numbers.append(number)

    return targets, numbers


def evaluate_left_to_right(numbers, ops):
    result = numbers[0]
    for i, op in enumerate(ops):
        if op == '+':
            result += numbers[i+1]
        elif op == '*':
            result *= numbers[i+1]
        elif op == '||':
            result = int(str(result) + str(numbers[i+1]))
    return result


def is_equation_possible(numbers, target):
    operator_combination = product(['+', '*', '||'], repeat=len(numbers)-1)
    for ops in operator_combination:
        if evaluate_left_to_right(numbers, ops) == target:
            return True
    return False

def is_equation_possible2(numbers, target):
    operator_combination = product(['+', '*', '||'], repeat=len(numbers)-1)
    for ops in operator_combination:
        if evaluate_left_to_right(numbers, ops) == target:
            return True
    return False

def calculate_total_calibrations(numbers_list, targets_list):
    total = 0
    for i in range(len(numbers_list)):
        numbers, target = numbers_list[i], targets_list[i]
        
        if is_equation_possible(numbers, target):
            total += target
        # elif is_equation_possible2(numbers, target):
        #     total += target
    
    
    return total




if __name__ == "__main__":
    load_dotenv()
    SESSION_COOKIE = os.getenv("AOC_SESSION")
    
    DAY = 7
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
            print(f"Failed to fetch data")
            
    except Exception as e:
        print(f"An error occurred {e}")
        
        
    targets, numbers = parse_data(input_data)
    
    result = calculate_total_calibrations(numbers, targets)
    
    print(result)