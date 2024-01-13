from collections import deque

bullet_price = int(input())
gun_barrel_size = int(input())
bullets = deque([int(b) for b in input().split()])
locks = deque([int(l) for l in input().split()])
intelligence_value = int(input())

bullets_copy = bullets.copy()
while locks:
    if bullets_copy:
        for _ in range(gun_barrel_size):

            current_lock = locks.popleft()
            current_bullet = bullets_copy.pop()

            if current_bullet <= current_lock:
                current_lock = locks.popleft()
                print('Bang!')
            else:
                locks.appendleft(current_lock)
                print('Ping!')
            if len(bullets_copy) == 0:
                break
        if len(bullets_copy) > 0:
            print('Reloading!')

    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
        break
else:
    used_bullets = len(bullets) - len(bullets_copy)
    print(f"{len(bullets_copy)} bullets left. Earned ${intelligence_value - (used_bullets * bullet_price)}")