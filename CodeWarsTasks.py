"""Теория и практика языков программирования
git status
git init
git add .
git commit -m "..."
git push
"""
"""Here I gonna save some scripts while studying python language"""

"""

Complete the method/function so that it converts dash/underscore delimited words 
into camel casing. The first word within the output should be capitalized only 
if the original word was capitalized (known as Upper Camel Case, also often 
referred to as Pascal case).

"""
# def to_camel_case(text):
#     text = text.replace("-", "_")
#     text_without_requested_delimeters = text.split("_")
#     for i in range(1,len(text_without_requested_delimeters)):
#         text_without_requested_delimeters[i] = (
#             text_without_requested_delimeters[i].capitalize())
#     line_to_output = "".join(text_without_requested_delimeters)
#     return(line_to_output)    
    
# print(to_camel_case(input()))


"""Square(n) sum

Complete the square sum function so that it squares each number passed into it 
and then sums the results together.
For example, for [1, 2, 2] it should return 9 because 1^2 + 2^2 + 2^2 = 9.

"""
# def square_sum(numbers):
#     """
#     Using lambda and map function we count squares for each element in numbers 
#     list
#     Then list() takes list iterable from map and creates list
#     Using list sum counts total number of sum of elements
#     """
#     return(sum(list(map(lambda x: x**2, numbers))))

# square_sum([1, 2, 3])

"""List filtering

In this kata you will create a function that takes a list of non-negative 
integers and strings and returns a new list with the strings filtered out.

List comprehension is used

"""
# def filter_list(l):
#     return [x for x in l if type(x) is not str]
# print(filter_list([1, 2, 'a', 'b', 'c', 3, "d"]))

"""In a factory a printer prints labels for boxes. For one kind of boxes the 
printer has to use colors which, for the sake of simplicity, are named with 
letters from a to m.
    The colors used by the printer are recorded in a control string. For example 
a "good" control string would be aaabbbbhaijjjm meaning that the printer used 
three times color a, four times color b, one time color h then one time color 
a...
    Sometimes there are problems: lack of colors, technical malfunction and a 
"bad" control string is produced e.g. aaaxbbbbyyhwawiwjjjwwm with letters not 
from a to m.
    You have to write a function printer_error which given a string will return 
the error rate of the printer as a string representing a rational whose 
numerator is the number of errors and the denominator the length of the control 
string. Don't reduce this fraction to a simpler expression.
    The string has a length greater or equal to one and contains only letters 
from a to z."""
# def printer_errors(s):
#     errors_number = 0
#     for symbol in s:
#         if ord(symbol) > 109: errors_number += 1
#     # return(str(errors_number) + "/" + str(len(s)))
#     # or
#     return("{}/{}".format(errors_number, len(s)))

# print(printer_errors("aaaxbbbbyyhwawiwjjjwwm"))


"""Sum of positive

You get an array of numbers, return the sum of all of the positives ones.
Example [1,-4,7,12] => 1 + 7 + 12 = 20
Note: if there is nothing to sum, the sum is default to 0.

"""
# def positive_sum(arr):
#     return(sum([number for number in arr if number > 0]))

# print(positive_sum([-1, -2, -3, -4, -5]))


"""Array.diff

    Your goal in this kata is to implement a difference function, which 
subtracts one list from another and returns the result.
    It should remove all values from list a, which are present in list b keeping 
their order.
        array_diff([1,2],[1]) == [2]
    If a value is present in b, all of its occurrences must be removed from the 
other:
        array_diff([1,2,2,2,3],[2]) == [1,3]

"""
# def array_diff(a, b):
#     return [element for element in a if element not in b]

# print(array_diff([1, 2], [1]))


"""Split strings

    Complete the solution so that it splits the string into pairs of two 
characters. If the string contains an odd number of characters then it should 
replace the missing second character of the final pair with an underscore ('_').
        Examples:
    solution('abc') # should return ['ab', 'c_']
    solution('abcdef') # should return ['ab', 'cd', 'ef']

"""
# def solution(s):
#     if len(s) % 2 == 1: s += "_"
#     return ["{}{}".format(s[i], s[i + 1]) for i in range(0, len(s) - 1, 2)]

# print(solution("x"))


"""Take a ten minute walk

    You live in the city of Cartesia where all roads are laid out in a perfect 
grid. You arrived ten minutes too early to an appointment, so you decided to 
take the opportunity to go for a short walk. The city provides its citizens with 
a Walk Generating App on their phones -- everytime you press the button it sends 
you an array of one-letter strings representing directions to walk 
(eg. ['n', 's', 'w', 'e']). You always walk only a single block for each letter 
(direction) and you know it takes you one minute to traverse one city block, so 
create a function that will return true if the walk the app gives you will take 
you exactly ten minutes (you don't want to be early or late!) and will, of 
course, return you to your starting point. Return false otherwise.
    Note: you will always receive a valid array containing a random assortment 
of direction letters ('n', 's', 'e', or 'w' only). It will never give you an 
empty array (that's not a walk, that's standing still!).

"""
# def is_valid_walk(walk):
#     moves = {'n': 0, 's': 0, 'e': 0, 'w': 0}
#     for direction in moves.keys():  # Count moves in each direction
#         moves[direction] = len([move for move in walk if move == direction])
#     if (moves['n'] == moves['s'] and moves['e'] == moves['w'] and 
#         len(walk) == 10):  # Sum of moves in opposite directions should be eq, 
#                            # amount of moves should be 10
#         return True
#     return False

# print(is_valid_walk(['w','e','w','e','w','e','w','e','w','e','w','e']))


""" Delete occurences of an element if it occurs more than n times

    Given a list lst and a number N, create a new list that contains each number 
of lst at most N times without reordering. For example if N = 2, and the input 
is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since this would 
lead to 1 and 2 being in the result 3 times, and then take 3, which leads 
to [1,2,3,1,2,3].
    Example
        delete_nth ([1,1,1,1],2) # return [1,1]  
        delete_nth ([20,37,20,21],1) # return [20,37,21]

"""
# def delete_nth(order, max_e):
#     for element in order: 
#         number_of_repeats = order.count(element)
#         if(number_of_repeats > max_e):  # If there are more elements than needed
#             order.reverse()  # Deleting elements from the end
#             for i in range(number_of_repeats - max_e):
#                 order.remove(element)
#             order.reverse()  # Reverse back
#     return(order)


# print(delete_nth([1,1,3,3,7,2,2,2,2], 3))


""" Pete, the baker

    Write a function cakes(), which takes the recipe (object) and the available 
ingredients (also an object) and returns the maximum number of cakes Pete can 
bake (integer). For simplicity there are no units for the amounts (e.g. 1 lb of 
flour or 200 g of sugar are simply 1 or 200). Ingredients that are not present 
in the objects, can be considered as 0.
    Examples:
        # must return 2
        cakes({flour: 500, sugar: 200, eggs: 1}, 
              {flour: 1200, sugar: 1200, eggs: 5, milk: 200})
        # must return 0
        cakes({apples: 3, flour: 300, sugar: 150, milk: 100, oil: 100}, 
              {sugar: 500, flour: 2000, milk: 2000})

"""
# def cakes(recipe, available):
#     ingredients = list(available.keys()) 
#     needed_ingredients = list(recipe.keys())
#     cakes_amount = list()  # Save amount of possible cakes for each ingr
#     for ingredient in needed_ingredients:
#         if ingredient not in ingredients: return 0  # If there is no that ingr
#         portions = (available[ingredient] // recipe[ingredient])
#         cakes_amount.append(portions)
#     return min(cakes_amount)

# recipe = {'flour': 500, 'sugar': 200, 'eggs': 1}
# # available = {"flour": 1200, "sugar": 1200, "eggs": 5, "milk": 200}
# available = {'flour': 1200, 'sugar': 1200, 'eggs': 5, 'milk': 200}
# print(cakes(recipe, available))


""" Create phone number

    Write a function that accepts an array of 10 integers (between 0 and 9), 
that returns a string of those numbers in the form of a phone number.
    Example
        create_phone_number([1, 2, 3, 4, 5, 6, 7, 8, 9, 0]) # => 
        returns "(123) 456-7890"
    The returned format must be correct in order to complete this challenge.
    Don't forget the space after the closing parentheses!

"""
# def create_phone_number(n):
#     return "({}{}{}) {}{}{}-{}{}{}{}".format(*n)

# print(create_phone_number([1, 1, 1, 1, 1, 1, 1, 1, 1, 1]))


""" Detect pangram

    A pangram is a sentence that contains every single letter of the alphabet at 
least once. For example, the sentence "The quick brown fox jumps over the lazy 
dog" is a pangram, because it uses the letters A-Z at least once (case is 
irrelevant).
    Given a string, detect whether or not it is a pangram. Return True if it is, 
False if not. Ignore numbers and punctuation.

"""

import string

def is_pangram(s):
    return (True if len("abcdefghijklmnopqrstuvwxyz".strip(s.lower())) == 0 
            else False)

print(is_pangram("The quick, brown fox jumps over the lazy dog!"))