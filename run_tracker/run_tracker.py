import csv

runs = []

while True:
    distance = float(input("Distance (km): "))
    if distance <= 0:
        print("Distance must be greater than 0.")
        continue
    time = float(input("Time (minutes): "))
    pace = time / distance
    runs.append([distance, time, round(pace, 2)])
    print(f"Pace: {round(pace, 2)} min/km")

    more = input ("Add another? (y/n):")
    if more.lower() != "y":
        break

        

with open ("runs.csv", "w", newline = "")as file:
    writer = csv.writer(file)
    writer.writerow(["Distance", "Time", "Pace"])
    writer.writerows (runs)

total_distance = sum(r[0] for r in runs)
avg_pace = sum(r[2] for r in runs) / len(runs)

print("\n--- Summary ---")
print(f"Total distance: {total_distance:.2f} km")
print(f"Average pace: {round(avg_pace, 2)} min/km")

print("Saved to runs.csv")