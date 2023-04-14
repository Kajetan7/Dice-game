import random


def dice_throw(code: str) -> int or str:
    """
    Simulates throwing a dice with a given code.

    Args:
    code (str): The code for the dice throw, e.g. "2D6+3", where "2" is the number of dice to throw,
    "D6" is the type of dice, and "+3" is the number to add to the sum of dice throws.

    Returns:
    int or str: The sum of the dice throws with the number to add/subtract, or a string with an error message.
    """

    # Convert the input code into a list of characters
    code = list(code)

    # List of possible dice types
    possible_dice_types = [3, 4, 6, 8, 10, 12, 20, 100]

    try:
        # Find the index of 'D' character in the list
        index_with_D_letter = code.index('D')
    except ValueError:
        # If there is no 'D' character in the list, return an error
        return 'Wrong code.'

    # Check if there is a sign '+' or '-' in the list and find its index
    if '+' in code:
        index_with_sign = code.index('+')
        # Extract the number to add from the code and convert it to an integer
        add_number = int(''.join(code[index_with_sign+1:]))
    elif '-' in code:
        index_with_sign = code.index('-')
        # Extract the number to subtract from the code and convert it to an integer
        substract_number = int(''.join(code[index_with_sign+1:]))
    else:
        index_with_sign = None

    # Extract the dice type from the code and convert it to an integer
    dice_type = int(''.join(code[index_with_D_letter + 1:index_with_sign]))

    # Check if the dice type is valid (in the possible_dice_types list)
    if dice_type not in possible_dice_types:
        return 'No such dice type.'

    # Extract the number of throws from the code and convert it to an integer
    number_of_throws = int(''.join(code[:index_with_D_letter]))

    # Generate random integers for each dice throw and store the results in a list
    results_of_throws = [random.randint(1, dice_type) for index in range(number_of_throws)]

    print(f'Here are results of your throws: {results_of_throws}')

    # Check if there is a sign '+' or '-' in teh code and return the sum of dice throws with added number
    if '+' in code:
        return sum(results_of_throws) + add_number
    elif '-' in code:
        return sum(results_of_throws) - substract_number
    else:
        return sum(results_of_throws)


# Examples of using the dice_throw function
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
