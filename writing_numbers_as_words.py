numbers = {'0': '', '1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight',
           '9': 'nine', '10': 'ten', '11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen',
           '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
pow_10 = {'2': 'twenty', '3': 'thirty', '4': 'forty', '5': 'fifty', '6': 'sixty', '7': 'seventy', '8': 'eighty', '9': 'ninety'}
pow_above = ['hundred', 'thousand']


def letterify(p_number):
    number = p_number
    num_str = str(number)
    out = ''
    if number > 0 and number < 20:
        return numbers[num_str]
    if number >= 1000:
        out = numbers[num_str[0]]
        out += pow_above[1]
        num_str = num_str[1:]
        number = int(num_str)
    if number >= 100:
        out += numbers[num_str[0]]
        out += pow_above[0]
        num_str = num_str[1:]
        number = int(num_str)
        if number > 0:
            out += 'and'
    if number >= 20:
        out += pow_10[num_str[0]]
        # out += numbers[num_str[1]]
        num_str = num_str[1:]
        number = int(num_str)
    if number > 0:
        out += numbers[str(number)]

    print(out)
    return out

nbr_letters = 0
for i in range(1, 1001):
    nbr_letters += len(letterify(i))
print(nbr_letters)
