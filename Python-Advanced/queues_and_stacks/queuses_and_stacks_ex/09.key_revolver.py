from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])
intelligence_value = int(input())
bullets_copy = bullets.copy()

bullets_are_over = False

shot_count = gun_barrel_size

while locks and bullets_copy:

    current_lock = locks.popleft()
    current_bullet = bullets_copy.pop()

    if current_bullet <= current_lock:
        print('Bang!')
    else:
        print('Ping!')
        locks.appendleft(current_lock)
    shot_count -= 1
    if bullets_copy and shot_count == 0:
        print('Reloading!')
        shot_count = gun_barrel_size


if locks:
    print(f"Couldn't get through. Locks left: {len(locks)}")
else:
    money_earned = intelligence_value - (len(bullets) - len(bullets_copy)) * bullet_price
    print(f"{len(bullets_copy)} bullets left. Earned ${money_earned}")

