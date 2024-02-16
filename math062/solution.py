def find_permutations(number, idx, permutation_list):
    if idx == len(number) - 1:
        num = int("".join(number))

        if num == 41063625 or num == 56623104 or num==66430125:
            print('yes')
        if len(str(num)) == len(number):
            permutation_list.append(num)
        return permutation_list
    
    for i in range(idx, len(number)):
        num_list = list(number)
        num_list[idx], num_list[i] = num_list[i], num_list[idx]
        permutation_list = find_permutations(num_list, idx+1, permutation_list)

    return permutation_list


def solver(n):
    number = 1
    while True:
        cube = number ** 3
        print(number)

        permutations = find_permutations(str(cube), 0, [])

        count = 0
        for permutation in permutations:
            val = permutation ** (1/3)
            if val == int(val):
                count += 1

        if count == n:
            break

        number += 1

    return cube


def answer():
    return solver(3)


if __name__ == '__main__':
    # print(f'answer() = {answer()}')
    find_permutations('41063625', 0, [])