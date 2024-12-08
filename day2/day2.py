


def level2(arr):
    def isSafe(sequence):
        if len(sequence) < 2:
            return True  # A single level is trivially safe

        increasing = None  # To determine the trend (increasing or decreasing)

        for i in range(len(sequence) - 1):
            diff = sequence[i + 1] - sequence[i]  # Difference between adjacent levels

            if diff == 0:
                return False  # Adjacent levels must differ

            if diff < -3 or diff > 3:
                return False  # Difference must be between -3 and 3

            if increasing is None:
                increasing = diff > 0  # Set direction on first valid comparison
            elif increasing and diff < 0:
                return False  # Break in increasing sequence
            elif not increasing and diff > 0:
                return False  # Break in decreasing sequence

        return True  # All conditions are satisfied
    
    if isSafe(arr):
        return True
    
    for i in range(len(arr)):
        modified_arr = arr[:i] + arr[i+1:]
        if isSafe(modified_arr):
            return True

    return False
        
        
with open('input2.txt', 'r') as file:
    safe_count = 0
    for line in file:
        if line.strip():  # Skip empty lines
            array = list(map(int, line.split()))
            if level2(array):
                safe_count += 1
            
            
print(safe_count)
            
    
    


            