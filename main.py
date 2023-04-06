import random


def dice_throw(code: str) -> int or str:

    code = list(code)
    possible_dice_types = [3, 4, 6, 8, 10, 12, 20, 100]

    try:
        index_with_D_letter = code.index('D')
    except ValueError:
        return 'Wrong code.'

    if '+' in code:
        index_with_sign = code.index('+')
        add_number = int(''.join(code[index_with_sign+1:]))
    elif '-' in code:
        index_with_sign = code.index('-')
        substract_number = int(''.join(code[index_with_sign+1:]))
    else:
        index_with_sign = None

    dice_type = int(''.join(code[index_with_D_letter + 1:index_with_sign]))

    if dice_type not in possible_dice_types:
        return 'No such dice type.'

    number_of_throws = int(''.join(code[:index_with_D_letter]))

    results_of_throws = [random.randint(1, dice_type) for index in range(number_of_throws)]

    print(f'Here are results of your throws: {results_of_throws}')

    if '+' in code:
        return sum(results_of_throws) + add_number
    elif '-' in code:
        return sum(results_of_throws) - substract_number
    else:
        return sum(results_of_throws)


y = dice_throw('2')
print(y)

y = dice_throw('2D8+16')
print(y)

y = dice_throw('6D4-10')
print(y)

y = dice_throw('6D5+5')
print(y)

y = dice_throw('6D4')
print(y)
