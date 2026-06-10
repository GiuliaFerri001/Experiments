def write_measurements(path, values):
    with open(path, "w") as f:
        for value in values:
            f.write(f"{value}\n")

def read_measurements(path):
    with open(path, "r") as f:
        content = f.read()
    return [float(x) for x in content.split() if x]
    
def summarise(values):
    return sum(values) / len(values) if values else 0

if __name__ == "__main__":
    data = [12.5, 9.3, 14.1, 11.8, 10.2]
    write_measurements("measurements.txt", data)
    loaded = read_measurements("measurements.txt")
    print(f"n={len(loaded)} mean={summarise(loaded):.2f}")