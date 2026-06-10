def write_measurements(path, values):
    with open(path, "w") as f:
        for value in values:
            f.write(f"{value}\n")

def std_dev(values):
    if not values:
        return 0
    mean = sum(values) / len(values)
    squared_diffs = [(x - mean) ** 2 for x in values]
    return (sum(squared_diffs) / len(values)) ** 0.5

def summarise(values):
    return sum(values) / len(values) if values else 0



if __name__ == "__main__":
    data = [12.5, 9.3, 14.1, 11.8, 10.2]
    write_measurements("measurements.txt", data)
    print(f"n={len(data)} mean={summarise(data):.2f} std_dev={std_dev(data):.2f}")