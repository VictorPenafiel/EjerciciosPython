def fibonacci_dynamic(num):
    arr = [0, 1]
    
    if num == 1:
        return [0]
    elif num == 2:
        return arr
    else:
        for _ in range(2, num):
            arr.append(arr[-1] + arr[-2])
        return arr

print(fibonacci_dynamic(30))