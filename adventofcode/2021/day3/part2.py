
def track_first_bit(values, i, reverse=False):
    track = [0, 0]

    for v in values:
        if int(v[i]) == 0:
            track[0] += 1
        elif int(v[i]) == 1:
            track[1] += 1

    if reverse:
        precedece_bit = 0 if track[0] < track[1] else 1
        if track[0] == track[1]:
            precedece_bit = 0
    else:
        precedece_bit = 0 if track[0] > track[1] else 1
        if track[0] == track[1]:
            precedece_bit = 1
    return list(filter(lambda x: str(x)[i] == str(precedece_bit), values))
    # filtered_list = []
    # for  v in values:
    #     if str(v)[i] == str(precedece_bit):
    #         filtered_list.append(v)
    # return filtered_list


def main():
    with open('day3.input', 'r') as fh:
        all_list_one = fh.read().split('\n')
    with open('day3.input', 'r') as fh2:
        all_list_two = fh2.read().split('\n')

    while True:
        for i in range(len(all_list_one[0])):
            if len(all_list_one) <= 1:
                break
            all_list_one = track_first_bit(all_list_one, i)
        if len(all_list_one) == 1:
            break

    while True:
        for j in range(len(all_list_two[0])):
            if len(all_list_two) <= 1:
                break
            all_list_two = track_first_bit(all_list_two, j, True)
        if len(all_list_two) == 1:
            break

    print(all_list_one)
    print(all_list_two)


if __name__ == "__main__":
    main()

    