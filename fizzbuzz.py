#!/usr/bin/env python3

"""
FizzBuzz

Die Funktion gibt den Zahlraum von 1 bis 100 wieder.
Bei jeder Zahl die durch drei teilbar ist, soll die Zahl durch "fizz" ersetzt werden.
Bei jeder Zahl die durch fünf teilbar ist, soll die Zahl durch "buzz" ersetzt werden.
Bei jeder Zahl die durch fünfzehn teilbar ist, soll die Zahl durch "fizzbuzz" ersetzt werden.
"""

def fizz_buzz(start_number, end_number):
    """
    fizz_buzz is a function to solve the game fizz_buzz
    Parameters
    ----------
    start_number : int, optional
        the number to start in fizz_buzz (default is 1)
    end_number : int, optional
        the number to end in fizz_buzz (default is 50)
    """
    print("Start von FizzBuzz")
    # Hier kannst du einen Code schreiben.

    print("Ende von FizzBuzz")


if __name__ == '__main__':
    print(fizz_buzz())


### Hilfestellung
## So funktioniert die for-Schleife

# for i in range(1, 100):
#     print(i)


## So funktioniert die if-Abfrage

# if a == 2:
#     print("a ist 2")
# elif a == 7:
#     print("a ist 7")
# else:
#     print("a ist etwas anderes")