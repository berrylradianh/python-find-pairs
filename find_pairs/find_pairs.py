def FindPairs(arr, target):
    found = False 
    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] + arr[j] == target:
                print(f"Pair found at {i} and {j} ({arr[i]} + {arr[j]})")
                found = True 

    if not found:
        print("No pairs found")
