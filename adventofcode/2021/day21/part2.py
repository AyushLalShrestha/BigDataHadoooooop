
counter = 1
odd_even_step = 0
die_roll_count = 0
player_one_pos = 10 #4
player_two_pos = 1 #

player_one_total = 0
player_two_total = 0

while True:
    if counter <= 98:
        val = counter + counter + 1 + counter + 2
    elif counter == 99:
        val = 99 + 100 + 1
    elif counter == 100:
        val = 100 + 1 + 2
    die_roll_count += 3

    if odd_even_step % 2 == 0:
        player_one_pos += val
        player_one_pos = player_one_pos % 10 if player_one_pos % 10 else 10
        player_one_total += player_one_pos
        if player_one_total >= 1000:
            print(player_two_total, die_roll_count, player_two_total * die_roll_count)
            break
        print(f"Counter:{counter}, die_roll:{ die_roll_count}, p1 pos:{player_one_pos}, p1 total:{player_one_total}")
    else:
        player_two_pos += val
        player_two_pos = player_two_pos % 10 if player_two_pos % 10 else 10
        player_two_total += player_two_pos
        if player_two_total >= 1000:
            print(player_one_total, die_roll_count, player_one_total * die_roll_count)
            break

    if counter <= 97:
        counter += 3
    elif counter == 98:
        counter = 1
    elif counter == 99:
        counter = 2
    elif counter == 100:
        counter = 3
    odd_even_step += 1
