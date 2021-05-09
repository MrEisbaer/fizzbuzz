def fizz_buzz(start_number = 1, end_number = 50):
    fizz_buzz_list = []
    for number in range(start_number, end_number + 1):
        fizz_buzz_value = ""
        if number % 3 == 0:
            fizz_buzz_value = "fizz"
        if number % 5 == 0:
            fizz_buzz_value += "buzz"
        if fizz_buzz_value != "":
            fizz_buzz_list.append(fizz_buzz_value)
        else:
            fizz_buzz_list.append(number)
    return fizz_buzz_list


if __name__ == '__main__':
    print(fizz_buzz())