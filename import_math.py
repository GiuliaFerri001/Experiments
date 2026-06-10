import math
angles_deg = [0, 30, 45, 60, 90]
angles_rad = [math.radians(angle) for angle in angles_deg]
sin = [math.sin(angle) for angle in angles_rad]
cos = [math.cos(angle) for angle in angles_rad]
for i in range(len(angles_deg)):
    print(f"{angles_deg[i]:<15} | {angles_rad[i]:<15} | {sin[i]:<15} | {cos[i]:<15}")

# compute math.tan(rad) for each angle and add it to the tuple. What value does
# math.tan(math.radians(90)) 
rad = math.tan(math.radians(90))
print(rad)