days = int(input())
daily_plunder = int(input())
expected_plunder = float(input())
current_plunder = 0

for day in range(1, days + 1):
    current_plunder += daily_plunder

    if day % 3 == 0:
        current_plunder += daily_plunder * 0.5
    if day % 5 == 0:
        current_plunder -= current_plunder * 0.3

if current_plunder >= expected_plunder:
    print(f"Ahoy! {current_plunder:.2f} plunder gained.")
else:
    percentage = current_plunder / expected_plunder * 100
    print(f"Collected only {percentage:.2f}% of the plunder.")
