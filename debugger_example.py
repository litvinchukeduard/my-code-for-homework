
'''
В нас список [1, 2, 3, 4, 5, 6, 7, 8, 9]
потрібно написати функцію, яка буде проходити по цьому списку та виводити
лише непарні числа
'''

def is_odd(number: int) -> bool:
    '''
    Function that receives a number and returns if it is odd
    '''
    # if number % 2 != 0:
    #     return True
    # else:
    #     return False
    return number % 2 != 0

#print_odd_numbers
def print_odd_numbers(number_list: list[int]):
    '''
    A function that receives a list of numbers and prints only odd numbers 
    '''
    # Пройтися по усім числам
    for number in number_list:
        # Перевірити чи конкретне число є парне чи ні
        if number % 2 != 0:
            # Якщо не парне, то вивести у термінал
            print(number)
    
    

# bbbbsdfggfd()

# To comment:
# Command /
# Ctrl /

# To clear terminal:
# Ctrl L 

# numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9]
# print_odd_numbers(numbers)

print_odd_numbers({1, 2, 3, 4, 5})

# print(is_odd("Hello"))

# 2 4 6 8 10
# 3 5 7 9 11

# 10 / 5
# 2 * 5

# 3 / 2
# 2 * 1 + 1

# 4 / 2
# 2 * 2 + 0

# print(4 % 2)
