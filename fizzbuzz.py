#!/usr/bin/env python3

def fizz_buzz(start_number = 1, end_number = 50):
    """
        fizz_buzz is a function to solve the game fizz_buzz
        Parameters
        ----------
        start_number : int, optional
            the number to start in fizz_buzz (default is 1)
        end_number : int, optional
            the number to end in fizz_buzz (default is 50)
    """
    fizz_buzz_list = []
    for number in range(start_number, end_number + 1):
        fizz_buzz_value = ""
        if number % 3 == 0:
            fizz_buzz_value = "fizz"
        if number % 5 == 0:
            fizz_buzz_value += "buzz"
        if fizz_buzz_value == "":
            fizz_buzz_value = number
        fizz_buzz_list.append(fizz_buzz_value)
    return fizz_buzz_list


if __name__ == '__main__':
    print(fizz_buzz())