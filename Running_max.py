def running_max(data):
    if not data:
        return []

    result = []
    current_max = data[0]

    for num in data:
        if num > current_max:
            current_max = num
        result.append(current_max)

    return result

data = [3, 1, 4, 1, 5, 9, 2, 6]
print(running_max(data))
