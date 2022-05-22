import math
import time

DRAG = 1
GRAVITY = 1

target_min_x = 56
target_max_x = 76
target_min_y = -162
target_max_y = -134

# target_min_x = 20
# target_max_x = 30
# target_min_y = -10
# target_max_y = -5

STYLISH_VELOCITY = None
HEIGHT = 0


def will_target_be_hit(x_velocity_start, y_velocity_start):
    """ Checks if the target trench area (defined globally above) will be hit """
    x_velocity, y_velocity = x_velocity_start, y_velocity_start
    position_x, position_y = (0, 0)
    max_height_attained = position_y
    while True:
        next_x = position_x + x_velocity
        next_y = position_y + y_velocity
        if next_x > target_max_x:
            y_velocity_start -= 1
            break
        if next_y < target_min_y:
            y_velocity_start += 1
            break
        if next_y > max_height_attained:
            max_height_attained = next_y
        if target_min_x <= next_x <= target_max_x:
            if target_min_y <= next_y <= target_max_y:
                print(f"HIT: {x_velocity_start}, {y_velocity_start}")
                global HEIGHT, STYLISH_VELOCITY
                if max_height_attained > HEIGHT:
                    HEIGHT = max_height_attained
                    STYLISH_VELOCITY = (x_velocity_start, y_velocity_start)
                return True, ""

        if x_velocity > 0:
            x_velocity -= DRAG
        elif x_velocity < 0:
            x_velocity += DRAG
        y_velocity = y_velocity - GRAVITY

        position_x = next_x
        position_y = next_y
    return False, y_velocity_start


def test_main():
    # print(will_target_be_hit(6, 6))
    # print(will_target_be_hit(7, 7))
    # print(will_target_be_hit(7, 2))
    # print(will_target_be_hit(6, 3))
    # print(will_target_be_hit(6, 9))
    # print(will_target_be_hit(17, -4))
    print(f"Height {HEIGHT} achieved by {STYLISH_VELOCITY}")


def main():
    for start_x_velocity in range(1, target_max_x+1):
        start_y_velocity = 1
        y_direction = None
        while True:
            hit, new_y_velocity = will_target_be_hit(start_x_velocity, start_y_velocity)
            if hit:
                if y_direction == "i":
                    start_y_velocity += 1
                elif y_direction == "d":
                    start_y_velocity -= 1
                else:
                    start_y_velocity += 1
            if not hit:
                time.sleep(0.02)
                if y_direction is None:
                    y_direction = "i" if new_y_velocity > start_y_velocity else "d"
                    start_y_velocity = new_y_velocity
                    print("here")
                elif y_direction == "d" and new_y_velocity > start_y_velocity:
                    start_y_velocity = new_y_velocity
                    print(f"d new_start_y: {start_y_velocity}")
                    # print("d")
                elif y_direction == "i" and new_y_velocity < start_y_velocity:
                    start_y_velocity = new_y_velocity
                    print(f"i new_start_y: {start_y_velocity}")
                    # print("i")
                else: 
                    break

    print(f"Height {HEIGHT} achieved by {STYLISH_VELOCITY}")

def main2():
    for start_x_velocity in range(1, target_max_x+1):
        for start_y_velocity in range(0, abs(target_min_y)):
            will_target_be_hit(start_x_velocity, start_y_velocity)
    print(f"Height {HEIGHT} achieved by {STYLISH_VELOCITY}")


if __name__ == "__main__":
    main2()
    # test_main()