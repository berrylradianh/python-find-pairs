# main.py
from find_pairs.find_pairs import FindPairs

if __name__ == "__main__":
    input_array = input("Enter the array of integers (comma separated):")
    arr = list(map(int, input_array.split(',')))
    
    target = int(input("Enter the target sum:"))
    
    FindPairs(arr, target)
