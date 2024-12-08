import re 

def calculate_valid_mul(filename):
    
    total = 0
    pattern = re.compile(r"mul\((\d{1,3}),(\d{1,3})\)")
    
    
    with open(filename, 'r') as file:
        
        for line in file:
            matches = pattern.findall(line)
            for match in matches:
                x, y = map(int, match)
                total += (x * y)
                
                
                
    return total


def calculate_valid_mul2(filename):
    
    pattern = re.compile(r"(do\(\)|don't\(\)|mul\(\d{1,3},\d{1,3}\))")
    
    with open(filename, 'r') as file:
        text = file.read()
        matches = pattern.findall(text)
        
    total = 0
    enabled = True
    
    
    for match in matches:
        # print(match)
        if match == "do()":
            enabled = True
        elif match == "don't()":
            enabled = False
        elif match.startswith("mul"):  # Matches `mul(x, y)`
            if enabled:
                # Extract the numbers inside `mul(x, y)`
                x, y = map(int, re.findall(r"\d{1,3}", match))
                total += x * y
    
    return total


filename = 'input3.txt'
result1 = calculate_valid_mul2(filename)
result2 = calculate_valid_mul(filename)
print(result1, result2)


