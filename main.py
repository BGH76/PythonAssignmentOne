# a=add s=subtract p=product d=division
def simple_calculator():
    num1 = input("Enter a number")
    operator = input("Enter operator (+, -, *, /")
    num2 = input("Enter a second number")
    if operator == '+':
        print(int(num1) + int(num2))
    elif operator == '-':
        print(int(num1) - int(num2))
    elif operator == '*':
        print(int(num1) * int(num2))
    elif operator == '/':
        print(int(num1) / int(num2))
    else:
        return "Error"


def largest_among_three_numbers():
    num1 = input("Enter your first number")
    num2 = input('Enter your second number')
    num3 = input('Enter you third number')
    if int(num1) > int(num2) and int(num1) > int(num3):
        print(num1)
    elif int(num2) > int(num1) and int(num2) > int(num3):
        print(num2)
    else:
        print(num3)


def leap_year():
    year = input("Enter a year")
    if int(year) % 100 and int(year) % 400:
        print(year + ' is a leap year.')
    else:
        print(year + ' is NOT a leap year')


def fib_sequence():
    def generate_fibonacci_sequence(num):
        if num < 0:
            return
        elif num == 0:
            return 0
        elif num == 1 or num == 2:
            return 1
        else:
            return generate_fibonacci_sequence(num - 1) + generate_fibonacci_sequence(num - 2)
    num = input("Enter a number")
    temp = generate_fibonacci_sequence(int(num))
    print("Your Fibonacci number is " + str(temp))


def check_prime_number():
    num = input('Enter a number')
    if int(num) <= 1:
        print('Enter a number greater than 1')
    elif int(num) == 2:
        print('Yes, 2 is a prime number')
    elif int(num) % 2 == 0:
        print('Sorry, ' + str(num) + ' is not a prime number')
    temp = int(num) * int(num)
    for i in range(2, temp+1):
        if int(num) % i == 0:
            print('Sorry, ' + str(num) + ' is not a prime number')
        else:
            print('Yes, ' + str(num) + ' is a prime number')
            break


def absolute_value():
    num = input("Enter a number")
    print(abs(int(num)))


def counting_strings():
    number = 0
    array_list = []
    count = 0
    number_in_list = input("Enter the number of strings you wish to enter")
    while(count < int(number_in_list)):
        next_string = input('Enter a word')
        array_list.append(next_string)
        count = count + 1
    for x in array_list:
        print(x)

    for i in array_list:
        if len(i) > 1:
            if i[0] == i[-1]:
                number = number + 1
        else:
            continue
    print('The number of strings greater than 2 with matching letters at the start and end are ' + str(number))


def check_for_empty_list(list):
    if len(list) == 0:
        return True
    return False


def remove_duplicates_from_list():
    count = 0
    list_set = set()
    size_of_list = input('Enter a number for the size of your list')
    while count < int(size_of_list):
        next_item = input('Enter an item: duplicates will be removed from the list')
        list_set.add(next_item)
        count = count + 1
    if check_for_empty_list(list_set) == False:
        for i in list_set:
            print(i)


def copy_a_list():
    list = []
    count = 0
    list_size = input('Enter your list size')
    if list_size == '':
        print('Sorry you did not enter a number')
        return
    while count < int(list_size):
        next_item = input('Enter an item')
        list.append(next_item)
        count = count + 1
    copy_list = list
    print('This is your list')
    for i in list:
        print(i)
    print('This is a copy of your list')
    for j in copy_list:
        print(j)


def max_of_three_numbers():
    num1 = input('Enter your first number')
    num2 = input('Enter your second number')
    num3 = input('Enter your third number')
    temp = set()
    temp.add(num1)
    temp.add(num2)
    temp.add(num3)
    print('Your max number is: ' + max(temp))


def sum_all_numbers_in_a_list():
    count = 0
    number = 0
    list = []
    list_size = input('Enter you list size')
    while count < int(list_size):
        next_int = input('Enter you next number')
        list.append(int(next_int))
        count = count + 1
    for i in list:
        number = number + i
    print('Your total number is: ' + str(number))

def multiply_all_numbers_in_a_list():
    count = 0
    number = 1
    list = []
    list_size = input('Enter you list size')
    while count < int(list_size):
        next_int = input('Enter you next number')
        list.append(int(next_int))
        count = count + 1
    for i in list:
        number = number * i
    print('Your total product is: ' + str(number))

def reverse_a_string():
    item = input('Enter a string')
    print('Your string in reverse is: ' + item[::-1])


def print_menu():
    print('')
    print('Please select from the menu or enter q to exit')
    print('1 - Simple Calculator')
    print('2 - Largest Among Three Numbers')
    print('3 - Leap Year')
    print('4 - Fib Sequence')
    print('5 - Check For A Prime Number')
    print('6 - Absolute Value')
    print('7 - Counting Strings In A List')
    print('8 - Remove Duplicates From A List')
    print('9 - Copy A List')
    print('10 - Max Of Three Numbers')
    print('11 - Sum All Numbers In A List')
    print('12 - Multiply All Numbers In A List')
    print('13 - Reverse A String')
    print('')


if __name__ == '__main__':
    test = ''
    while test != 'q':
        print_menu()
        selection = input('Enter your choice')
        if selection == 'q':
            test = 'q'
        else:
            if int(selection) == 1:
                simple_calculator()
            elif int(selection) == 2:
                largest_among_three_numbers()
            elif int(selection) == 3:
                leap_year()
            elif int(selection) == 4:
                fib_sequence()
            elif int(selection) == 5:
                check_prime_number()
            elif int(selection) == 6:
                absolute_value()
            elif int(selection) == 7:
                counting_strings()
            elif int(selection) == 8:
                remove_duplicates_from_list()
            elif int(selection) == 9:
                copy_a_list()
            elif int(selection) == 10:
                max_of_three_numbers()
            elif int(selection) == 11:
                sum_all_numbers_in_a_list()
            elif int(selection) == 12:
                multiply_all_numbers_in_a_list()
            elif int(selection) == 13:
                reverse_a_string()