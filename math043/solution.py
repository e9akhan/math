def combinations(num_str, index, combination_list):
    if index == len(num_str) - 1:
        combination_list.append(int("".join(num_str)))
        
    for i in range(index, len(num_str)):
        num_list = list(num_str)
        num_list[index], num_list[i] = num_list[i], num_list[index]

        combination_list = combinations(num_list, index+1, combination_list)

    return combination_list


def solver():
    pandigital = [str(i) for i in range(10)]

    combination_list = combinations(pandigital, 0, [])
    print(combination_list[::-1])

# print(solver())