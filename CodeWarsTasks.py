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

# import string

# def is_pangram(s):
#     return (True if len("abcdefghijklmnopqrstuvwxyz".strip(s.lower())) == 0 
#             else False)

# print(is_pangram("The quick, brown fox jumps over the lazy dog!"))


""" Scramblies

    Complete the function scramble(str1, str2) that returns true if a portion of 
str1 characters can be rearranged to match str2, otherwise returns false.
    Notes:
    Only lower case letters will be used (a-z). No punctuation or digits will be 
    included.
    Performance needs to be considered
        Input strings s1 and s2 are null terminated.
    Examples
        scramble('rkqodlw', 'world') ==> True
        scramble('cedewaraaossoqqyt', 'codewars') ==> True
        scramble('katas', 'steak') ==> False

"""
# def scramble(s1, s2):
#     print(len(s1), len(s2))
#     if len(s2) > len(s1):
#         return False
#     for symbol in s1:
#         print(symbol, s2)
#         s2 = s2.replace(symbol, "", 1)
#         if len(s2) == 0: break
#     return True if len(s2) == 0 else False

# def scramble(s1, s2):
    # if len(s2) > len(s1):
    #     return False
    # for symbol in s1:
    #     s2 = s2.replace(symbol, "", 1)
    #     if len(s2) == 0: break
    # return True if len(s2) == 0 else False


# def to_dict_of_chars(s):  # fun creates dict containig chars and theirs amount
#     chars_dict = dict()
#     for symbol in s:
#         if symbol not in chars_dict.keys():
#             chars_dict[symbol] = 1
#         else:
#             chars_dict[symbol] += 1
#     return chars_dict

# def scramble(s1, s2):
#     s1_to_chars = to_dict_of_chars(s1)
#     s2_to_chars = to_dict_of_chars(s2)
#     for char in s2_to_chars.keys():  # for each char in s2 compare with s1 and 
#         if (char not in s1_to_chars.keys() or  #its amount
#             s2_to_chars[char] > s1_to_chars[char]):
#             return False
#     return True

# print(scramble('cedewaraaossoqqyt', 'codewars'))


""" First non-repeating character

    Write a function named first_non_repeating_letter that takes a string input, 
and returns the first character that is not repeated anywhere in the string.
    For example, if given the input 'stress', the function should return 't', 
since the letter t only occurs once in the strin<g, and occurs first in the 
string.
    As an added challenge, upper- and lowercase letters are considered the same 
character, but the function should return the correct case for the initial 
letter. For example, the input 'sTreSS' should return 'T'.
    If a string contains all repeating characters, it should return an empty 
string ("") or None -- see sample tests.

"""
# def first_non_repeating_letter(string):
#     symbols_counter = dict()
#     for symbol in string:
#         if symbol.lower() in symbols_counter.keys():
#             symbols_counter[symbol.lower()] += 1
#         elif symbol.upper() in symbols_counter.keys(): 
#             symbols_counter[symbol.upper()] += 1
#         else: symbols_counter[symbol] = 1
#     for symbol in symbols_counter.keys():
#         if symbols_counter[symbol] == 1:
#             return symbol
#     return ""

# print(first_non_repeating_letter("sTreSS"))


""" Recover a secret string from random triplets

    There is a secret string which is unknown to you. Given a collection of 
random triplets from the string, recover the original string.
    A triplet here is defined as a sequence of three letters such that each 
letter occurs somewhere before the next in the given string. "whi" is a triplet 
for the string "whatisup".
    As a simplification, you may assume that no letter occurs more than once in 
the secret string.
    You can assume nothing about the triplets given to you other than that they 
are valid triplets and that they contain sufficient information to deduce the 
original string. In particular, this means that the secret string will never 
contain letters that do not occur in one of the triplets given to you.

"""
# Примерный алгоритм: проходим по матрице и проверяем, встречается ли последний 
# элемент каждой строки ещё где-то в строках, если нет, то на данный момент он 
# является искомым, добавляем его ЛЕВЕЕ текущей строки, потом удаляем все его 
# упоминания в матрице
# def check_if_char_is_last(triplets, char):  # Looking through all lines to check 
#     for line in triplets:  # if there are any repeats of the element and its 
#         for symbol_index in range(len(line)):  # position
#             if char == line[symbol_index] and symbol_index != len(line) - 1:  
#                 return False
#     return True

# def get_last_char(triplets):  # Looking for an element without any elements to 
#     for line in triplets:     # the right and then call that element last
#         if len(line) > 0:
#             char = line[-1]
#             if check_if_char_is_last(triplets, char): return char

# def check_if_matrix_is_empty(triplets):  # Check if there are still elements in 
#     for line in triplets:                # each line
#         if len(line) > 0:
#             return False
#     return True

# def delete_found_char(triplets, char):  # Delete element in matrix after saving
#     for line in triplets:
#         if char in line:
#             line.pop()
#     return triplets

# def recoverSecret(triplets):  # It's better to name function recover_secret()
#     decoded_line = ""
#     while not check_if_matrix_is_empty(triplets):  # Keep working with matrix 
#         last_char = get_last_char(triplets)  # if there are still elements
#         triplets = delete_found_char(triplets, last_char)
#         decoded_line = "{}{}".format(last_char,decoded_line)
#     return(decoded_line)

# triplets = [
#   ['t','u','p'],
#   ['w','h','i'],
#   ['t','s','u'],
#   ['a','t','s'],
#   ['h','a','p'],
#   ['t','i','s'],
#   ['w','h','s']
# ]
# print(recoverSecret(triplets))


""" Title Case

    A string is considered to be in title case if each word in the string is 
either:
(a) capitalised (that is, only the first letter of the word is in upper case) or 
(b) considered to be an exception and put entirely into lower case unless it is
 the first word, which is always capitalised.
    Write a function that will convert a string into title case, given an 
optional list of exceptions (minor words). The list of minor words will be given 
as a string with each word separated by a space. Your function should ignore the 
case of the minor words string -- it should behave in the same way even if the 
case of the minor word string is changed.
    ###Arguments (Other languages)
First argument (required): the original string to be converted.
Second argument (optional): space-delimited list of minor words that must always 
be lowercase except for the first word in the string. The 
JavaScript/CoffeeScript tests will pass undefined when this argument is unused.
        ###Example
    title_case('a clash of KINGS', 'a an the of') # should return: 
        'A Clash of Kings'
    title_case('THE WIND IN THE WILLOWS', 'The In') # should return: 
        'The Wind in the Willows'
    title_case('the quick brown fox') # should return: 'The Quick Brown Fox'

"""
# def title_case(title, minor_words=""):
#     title = list(map(str.lower, title.split()))  # Getting list of lowered and 
#     minor_words = list(map(str.lower, minor_words.split()))  # splitted words
#     # If word isn't on 0 position or not in minor - cap them and then create 
#     # array and return all data
#     return " ".join([title[idx].capitalize()  
#                      if idx == 0 or title[idx] not in minor_words 
#                      else title[idx].lower() for idx in range(len(title))])  

# print(title_case('the quick brown fox'))


""" Two sum

    Write a function that takes an array of numbers (integers for the tests) and 
a target number. It should find two different items in the array that, when 
added together, give the target value. The indices of these items should then be 
returned in a tuple like so: (index1, index2).
    For the purposes of this kata, some tests may have multiple answers; any 
valid solutions will be accepted.
    The input will always be valid (numbers will be an array of length 2 or 
greater, and all of the items will be numbers; target will always be the sum of 
two different items from that array).
    Based on: http://oj.leetcode.com/problems/two-sum/
    twoSum [1, 2, 3] 4 === (0, 2)

"""
# def two_sum(numbers, target):
#     for idx, first_number in enumerate(reversed(numbers)):
#         if target - first_number in numbers:
#             return(tuple((len(numbers) - idx - 1, numbers.index(target - first_number))))


# print(two_sum([1234,5678,9012], 14690)) 


""" What's a Perfect Power anyway?

    A perfect power is a classification of positive integers:
    "In mathematics, a perfect power is a positive integer that can be expressed 
as an integer power of another positive integer. More formally, n is a perfect 
power if there exist natural numbers m > 1, and k > 1 such that mk = n."
    Your task is to check wheter a given integer is a perfect power. If it is a 
perfect power, return a pair m and k with mk = n as a proof. Otherwise return 
Nothing, Nil, null, NULL, None or your language's equivalent.
    Note: For a perfect power, there might be several pairs. For example 
81 = 3^4 = 9^2, so (3,4) and (9,2) are valid solutions. However, the tests take 
care of this, so if a number is a perfect power, return any pair that proves it.

Examples
isPP(4) => [2,2]
isPP(9) => [3,2]
isPP(5) => None

"""
# import math
# def isPP(n):
#     tolerance = 0.000000001
#     for k in range(2, round(math.sqrt(n) + 1)):
#         root = n ** (1 / k)
#         if abs(round(root) - root) < tolerance:
#             return [round(root), k]
#     return None

# print(isPP(27))  


# #Regex
# import re
# text = input("Enter smth: ")
# print(re.search("[0-9a-z][^>]\w+", text))
# print(re.search("[ab\]c-]", text))
# print(re.search(r"\babc", text))
# print(re.search(r"\Babc", text))
# print(re.search(r"\Babc\B", text))
# print(re.findall(r"\bСУ\d*", text))
# \d+:[^<]*  # Все символы внутри html тэгов по шаблону: 
#              <a href="#10">10: CamelCase -> under_score</a>;


""" Extract the domain name from a URL

    Write a function that when given a URL as a string, parses out just the 
domain name and returns it as a string. For example:
        domain_name("http://github.com/carbonfive/raygun") == "github" 
        domain_name("http://www.zombie-bites.com") == "zombie-bites"
        domain_name("https://www.cnet.com") == "cnet"

# """
# import re
# def domain_name(url):
#     return((re.search(r"(?<=//)[^w][a-zA-Z-]+|(?<=www.)[a-zA-Z-]+", url)).group(0))
# (?<=//)[^w][0-9a-zA-Z-]+|(?<=www.)[0-9a-zA-Z-]+ 
# (?<=//)[^w|][0-9a-zA-Z-]+|(?<=www.)[0-9a-zA-Z-]+
# http://github.com/carbonfive/raygun
# http://www.zombie-bites.com
# https://www.cnet.com
# http://google.com
# http://google.co.jp
# www.xakep.ru
# https://youtube.com
# icann.org
# (?<=\/\/)|(?<=www\.)[0-9a-zA-Z-]+ --- ???
# import re
# def domain_name(url):
#     return((re.search(r"(?!www\.|ww\.|w\.)[a-zA-Z0-9-]+(?=\.)", url)).group(0))


""" Count the number of JavaScript developers coming from Europe

    You will be given an array of objects representing data about developers who 
have signed up to attend the coding meetup that you are organising for the first 
time.
    Your task is to return the number of JavaScript developers coming from Europe.
    For example, given the following list:
lst1 = [
  { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
  { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
  { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
  { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
]
your function should return number 1.
    If, there are no JavaScript developers from Europe then your function should return 0.
    Notes:
    The format of the strings will always be Europe and JavaScript.
    All data will always be valid and uniform as in the example above.

"""
# def count_developers(lst):
#     #return len([worker for worker in lst if worker['continent'] == 'Europe' 
#     #            and worker['language'] == 'JavaScript']) 
#       #or
#     return sum(1 for dev in lst if dev['continent'] == 'Europe' and 
#                dev['language'] == 'JavaScript')

# list1 = [
#           { 'firstName': 'Noah', 'lastName': 'M.', 'country': 'Switzerland', 'continent': 'Europe', 'age': 19, 'language': 'JavaScript' },
#           { 'firstName': 'Maia', 'lastName': 'S.', 'country': 'Tahiti', 'continent': 'Oceania', 'age': 28, 'language': 'JavaScript' },
#           { 'firstName': 'Shufen', 'lastName': 'L.', 'country': 'Taiwan', 'continent': 'Asia', 'age': 35, 'language': 'HTML' },
#           { 'firstName': 'Sumayah', 'lastName': 'M.', 'country': 'Tajikistan', 'continent': 'Asia', 'age': 30, 'language': 'CSS' }
#         ]
        
# list2 = [
#           { 'firstName': 'Oliver', 'lastName': 'Q.', 'country': 'Australia', 'continent': 'Oceania', 'age': 19, 'language': 'HTML' },
#           { 'firstName': 'Lukas', 'lastName': 'R.', 'country': 'Austria', 'continent': 'Europe', 'age': 89, 'language': 'HTML' }
#         ]        
        
# print(count_developers(list1), 1)
# print(count_developers(list2), 0)


""" Split strings (usinf regex)

    Complete the solution so that it splits the string into pairs of two 
characters. If the string contains an odd number of characters then it should 
replace the missing second character of the final pair with an underscore ('_').
Examples:
solution('abc') # should return ['ab', 'c_']
solution('abcdef') # should return ['ab', 'cd', 'ef']

"""
# import re
# def solution(s):
#     if len(s) % 2 != 0: s += "_"
#     return re.findall(r"\w{2}", s)

# print(solution("asdfadsf"))
# print(solution("asdfads"))
# print(solution(""))
# print(solution("w"))


# def get_total_time(heroes, n):
#     fight_time = [0 for fight in range(n)]
#     for hero_time in heroes:
#         fight_time[fight_time.index(min(fight_time))] += hero_time
#     return max(fight_time)

# print(get_total_time([6, 2, 9], 1))
# print(get_total_time([11, 2, 3, 4], 2))
# print(get_total_time([3, 5, 10], 2))


""" IP Validation

    Write an algorithm that will identify valid IPv4 addresses in dot-decimal 
format. IPs should be considered valid if they consist of four octets, with 
values between 0 and 255, inclusive.

Valid inputs examples:
    Examples of valid inputs:
        1.2.3.4
        123.45.67.89
    Invalid input examples:
        1.2.3
        1.2.3.4.5
        123.456.78.90
        123.045.067.089
    Notes:
        Leading zeros (e.g. 01.02.03.04) are considered invalid
        Inputs are guaranteed to be a single string

"""
# import re
# def is_valid_IP(string):
#     if re.search(r"(?:([0-9]{0,3}\.)){3}[0-9]{1,3}", string) is not None:
#         ip_address_splitted = re.search(r"(?:([0-9]{0,3}\.)){3}[0-9]{1,3}", 
#                                         string).string.split(".")
#         for field in ip_address_splitted:
#             if (len(field) > 1 and field[0] == "0") or int(field) > 255:
#                 return False
#         return True
#     return False


# print(is_valid_IP('12.255.56.1'),     True)
# print(is_valid_IP(''),                False)
# print(is_valid_IP('abc.def.ghi.jkl'), False)
# print(is_valid_IP('123.456.789.0'),   False)
# print(is_valid_IP('12.34.56'),        False)
# print(is_valid_IP('12.34.56 .1'),     False)
# print(is_valid_IP('12.34.56.-1'),     False)
# print(is_valid_IP('123.045.067.089'), False)
# print(is_valid_IP('127.1.1.0'),        True)
# print(is_valid_IP('0.0.0.0'),          True)
# print(is_valid_IP('0.34.82.53'),       True)
# print(is_valid_IP('192.168.1.300'),   False)


""" Remove anchor from URL

    Complete the function/method so that it returns the url with anything after 
the anchor (#) removed.
    Examples:
        "www.codewars.com#about" --> "www.codewars.com"
        "www.codewars.com?page=1" -->"www.codewars.com?page=1"

"""
# import re
# def remove_url_anchor(url):
#     url_no_anchor = re.search(r".*(?=#)", url)  # Trying to find regex match 
#     return url if url_no_anchor == None else url_no_anchor.group()  # Return url 
#                                                  # w/o anchor if there is match

# print(remove_url_anchor("www.codewars.com#about"), "www.codewars.com")
# print(remove_url_anchor("www.codewars.com/katas/?page=1#about"), "www.codewars.com/katas/?page=1")
# print(remove_url_anchor("www.codewars.com/katas/"), "www.codewars.com/katas/")


""" ISBN-10 Validation

    ISBN-10 identifiers are ten digits long. The first nine characters are 
digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10
    An ISBN-10 number is valid if the sum of the digits multiplied by their 
position modulo 11 equals zero.
    
    For example:
        ISBN     : 1 1 1 2 2 2 3 3 3  9
        position : 1 2 3 4 5 6 7 8 9 10
    This is a valid ISBN, because:
        (1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0
    Examples:
        1112223339   -->  true
        111222333    -->  false
        1112223339X  -->  false
        1234554321   -->  true
        1234512345   -->  false
        048665088X   -->  true
        X123456788   -->  false

"""
# import re
# def valid_ISBN10(isbn):
#     isbn_valid_check = 0
#     if len(isbn) != 10 or re.search(r"[0-9]{9}[0-9X]", isbn) == None: 
#         return False
#     if isbn.endswith("X"): 
#         isbn = isbn.rstrip("X")
#         isbn_valid_check += 100
#     isbn = list(map(int, list(isbn)))
#     for idx, number in enumerate(isbn):
#         isbn_valid_check += number * (idx + 1)
#     return True if isbn_valid_check % 11 == 0 else False
# # SECOND Try
# def valid_ISBN10(isbn):
#     isbn_valid_check = 0  #Summator for final number
#     if len(isbn) != 10 or re.search(r"[0-9]{9}[0-9X]", isbn) == None: 
#         return False  # Check template to all numbers and throw away bad ISBNs
#     for idx, number in enumerate(isbn):
#         if number == "X": isbn_valid_check += 100  # If last number is X(=10)
#         else: isbn_valid_check += int(number) * (idx + 1)  
#     return True if isbn_valid_check % 11 == 0 else False

# print(valid_ISBN10('1112223339'), True)
# print(valid_ISBN10('048665088X'), True)
# print(valid_ISBN10('1293000000'), True)
# print(valid_ISBN10('1234554321'), True)
# print(valid_ISBN10('1234512345'), False)
# print(valid_ISBN10('1293'), False)
# print(valid_ISBN10('X123456788'), False)
# print(valid_ISBN10('ABCDEFGHIJ'), False)
# print(valid_ISBN10('XXXXXXXXXX'), False)


""" Return substring instance count -2

    Complete the solution so that it returns the number of times the search_text 
is found within the full_text.

    search_substr( full_text, search_text, allow_overlap = True )

so that overlapping solutions are (not) counted. If the searchText is empty, it 
should return 0. Usage examples:

search_substr('aa_bb_cc_dd_bb_e', 'bb') # should return 2 since bb shows up 
    twice
search_substr('aaabbbcccc', 'bbb') # should return 1
search_substr( 'aaa', 'aa' ) # should return 2
search_substr( 'aaa', '' ) # should return 0
search_substr( 'aaa', 'aa', False ) # should return 1

"""
# import re
# def check_with_overlap(full_text, search_text):
#     # looking for a match, if there is one - add counter and take 
#     # substr[char next to search_text start:end] 
#     substr_with_overlap_counter = 0
#     substr = re.search(r"{0}".format(search_text), full_text)
#     while substr != None:
#         substr_with_overlap_counter += 1
#         substr_start = (substr.span())[0]
#         full_text = full_text[substr_start + 1:]
#         substr = re.search(r"{0}".format(search_text), full_text)
#     return substr_with_overlap_counter

# def search_substr(full_text, search_text, allow_overlap=True):
#     if len(full_text) == 0 or len(search_text) == 0: return 0
#     if allow_overlap:
#         # there is no methods in libs for finding non-overlap, so I created mine
#         return(check_with_overlap(full_text, search_text))
#     else:
#         # findall is looking for non-overlaping substrings 
#         return(len(re.findall(r"{0}".format(search_text), full_text)))

# print(search_substr('aa_bb_cc_dd_bb_e', 'bb'), 2)
# print(search_substr('aaabbbcccc', 'bbb'), 1)
# print(search_substr('aaacccbbbcccc', 'cc'), 5)
# print(search_substr('aaa', 'aa'), 2)
# #Should handle non-overlapping cases
# print(search_substr('aaa', 'aa',False), 1)
# print(search_substr('aaabbbaaa', 'bb',False), 1)
# #Should handle empty strings on both sides
# print(search_substr('a', ''), 0)
# print(search_substr('', 'a'), 0)
# print(search_substr('', ''), 0)
# print(search_substr('', '',False), 0)

""" ROT13

Code/Decode given text

"""
# import re
# def rot13_char_transformation(char):
#     char_code = ord(char)
#     if re.search(r"[a-zA-Z]", char) == None: return char
#     if char.islower(): 
#         return chr(char_code + 13) if char_code < 110 else chr(char_code - 13)
#     else: return chr(char_code + 13) if char_code < 78 else chr(char_code - 13)

# def rot13(message):
#     return "".join(list(map(rot13_char_transformation, list(message))))

# print(rot13("EBG13 rknzcyr."), "ROT13 example.")
# print(rot13("How can you tell an extrovert from an\nintrovert at NSA? Va gur ryringbef,\ngur rkgebireg ybbxf ng gur BGURE thl'f fubrf."), "Ubj pna lbh gryy na rkgebireg sebz na\nvagebireg ng AFN? In the elevators,\nthe extrovert looks at the OTHER guy's shoes.")
# print(rot13("123"), "123")
# print(rot13("Guvf vf npghnyyl gur svefg xngn V rire znqr. Gunaxf sbe svavfuvat vg! :)"), "This is actually the first kata I ever made. Thanks for finishing it! :)")
# print(rot13("@[`{"), "@[`{")

""" Javascript filter-1

    While developing a website, you detect that some of the members have 
troubles logging in. Searching through the code you find that all logins ending 
with a "_" make problems. So you want to write a function that takes an array of 
pairs of login-names and e-mails, and outputs an array of all login-name, 
e-mails-pairs from the login-names that end with "_".
    If you have the input-array:
        [ [ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
    it should output
        [ [ "bar_", "bar@bar.com" ] ]

"""
# import re
# def search_names(logins):
#     return [[login[0], login[1]] for login in logins if 
#             re.search(r"\.*?_", login[0]) != None or 
#             re.search(r"\.*?_", login[1]) != None]

# 2nd version
# import re
# def login_check(login):
#     return True if (re.search(r"\.*?_", login[0]) != None or 
#                     re.search(r"\.*?_", login[1]) != None) else False

# def search_names(logins):
#     return [login for login in filter(login_check, logins)]

# a = [[ "foo", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
# b = [ [ "bar_", "bar@bar.com" ] ]
# print(search_names(a), b)

# a = [[ "foobar_", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
# b = [[ "foobar_", "foo@foo.com" ], [ "bar_", "bar@bar.com" ] ]
# print(search_names(a), b)

# a = [[ "foo", "foo@foo.com" ], [ "bar", "bar@bar.com" ] ]
# b = []
# print(search_names(a), b)

""" Coordinates Validator

    You need to create a function that will validate if given parameters are 
valid geographical coordinates.
    Valid coordinates look like the following: "23.32353342, -32.543534534". The 
return value should be either true or false.
    Latitude (which is first float) can be between 0 and 90, positive or 
negative. Longitude (which is second float) can be between 0 and 180, positive 
or negative.
    Coordinates can only contain digits, or one of the following symbols 
(including space after comma) __ -, . __
    There should be no space between the minus "-" sign and the digit after it.
Here are some valid coordinates:
-23, 25
24.53525235, 23.45235
04, -23.234235
43.91343345, 143
4, -3

"""
# import re
# def is_valid_coordinates(coordinates):
#     coordinates = coordinates.split(", ")
#     for coordinate in coordinates:
#         if (len(re.search(r"-*\d{1,3}\.*\d*", coordinate).group()) 
#             != len(coordinate)):
#             return False
#     try:
#         coordinates[0] = float(coordinates[0])
#         coordinates[1] = float(coordinates[1])
#         return True if (-90 <= coordinates[0] <= 90 
#                         and -180 <= coordinates[1] <= 180) else False
#     except ValueError:
#         return False

# print(is_valid_coordinates("-23, 25"))
# print(is_valid_coordinates("4, -3"))
# print(is_valid_coordinates("24.53525235, 23.45235"))
# print(is_valid_coordinates("04, -23.234235"))
# print(is_valid_coordinates("43.91343345, 143"))
# print(is_valid_coordinates("23.245, 1e1"))

""" Most frequently used words in a text

    Write a function that, given a string of text (possibly with punctuation and 
line-breaks), returns an array of the top-3 most occurring words, in descending 
order of the number of occurrences.
    Assumptions:
- A word is a string of letters (A to Z) optionally containing one or more 
apostrophes (') in ASCII.
- Apostrophes can appear at the start, middle or end of a word ('abc, abc', 
'abc', ab'c are all valid)
- Any other characters (e.g. #, \, / , . ...) are not part of a word and should 
be treated as whitespace.
- Matches should be case-insensitive, and the words in the result should be 
lowercased.
- Ties may be broken arbitrarily.
- If a text contains fewer than three unique words, then either the top-2 or 
top-1 words should be returned, or an empty array if a text contains no words.
    Examples:
top_3_words("In a village of La Mancha, the name of which I have no desire to 
call to mind, there lived not long since one of those gentlemen that keep a 
lance in the lance-rack, an old buckler, a lean hack, and a greyhound for
coursing. An olla of rather more beef than mutton, a salad on most
nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
on Sundays, made away with three-quarters of his income.")
# => ["a", "of", "on"]

top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e")
# => ["e", "ddd", "aa"]

top_3_words("  //wont won't won't")
# => ["won't", "wont"]

"""
# import re
# def top_3_words(text):
#     words = dict()
#     # word = (maybe)' + (one or more)word + (maybe)' + (maybe)word
#     word = r"\'*[a-zA-Z-]+\'*[a-zA-Z-]*"
#     splitted_text = list(map(lambda x: x.lower(), re.findall(word, text)))
#     for word in splitted_text:
#         if word in words.keys(): words[word] += 1
#         else: words[word] = 1
#     # Sort dict by number of repeats in ascending order of frequency
#     words = sorted(words.items(), key=lambda x: x[1], reverse=True)
#     if len(words) >= 3:
#         return [word[0] for word in words[:3]]
#     else:
#         return [word[0] for word in words]
        
# print(top_3_words("a a a  b  c c  d d d d  e e e e e"), ["e", "d", "a"])
# print(top_3_words("e e e e DDD ddd DdD: ddd ddd aa aA Aa, bb cc cC e e e"), ["e", "ddd", "aa"])
# print(top_3_words("  //wont won't won't "), ["won't", "wont"])
# print(top_3_words("  , e   .. "), ["e"])
# print(top_3_words("  ...  "), [])
# print(top_3_words("  '  "), [])
# print(top_3_words("  '''  "), [])
# print(top_3_words("""In a village of La Mancha, the name of which I have no desire to call to
# mind, there lived not long since one of those gentlemen that keep a lance
# in the lance-rack, an old buckler, a lean hack, and a greyhound for
# coursing. An olla of rather more beef than mutton, a salad on most
# nights, scraps on Saturdays, lentils on Fridays, and a pigeon or so extra
# on Sundays, made away with three-quarters of his income."""), ["a", "of", "on"])

""" ISBN-10 Validation

    ISBN-10 identifiers are ten digits long. The first nine characters are 
digits 0-9. The last digit can be 0-9 or X, to indicate a value of 10.
    An ISBN-10 number is valid if the sum of the digits multiplied by their 
position modulo 11 equals zero.

For example:
ISBN     : 1 1 1 2 2 2 3 3 3  9
position : 1 2 3 4 5 6 7 8 9 10
This is a valid ISBN, because:
(1*1 + 1*2 + 1*3 + 2*4 + 2*5 + 2*6 + 3*7 + 3*8 + 3*9 + 9*10) % 11 = 0

"""

# import re

# def valid_ISBN10(isbn):
#     if re.search(r"[0-9]{9}([0-9]{1}|X{1})", isbn) != None and len(isbn) < 10:
#         if sum([ int(digit) * (position + 1) if digit != "X" else 100 for 
#            position, digit in enumerate(isbn)]) % 11 == 0:
#             return True
#     return False
    

# valid_ISBN10("1112223339")
# valid_ISBN10("111222333")
# valid_ISBN10("1112223339X")
# valid_ISBN10("048665088X")
# print(valid_ISBN10("45673749913"))
            
""" Decode Morse

    In this kata you have to write a simple Morse code decoder. While the Morse 
code is now mostly superseded by voice and digital data communication channels, 
it still has its use in some applications around the world.
    The Morse code encodes every character as a sequence of "dots" and "dashes". 
For example, the letter A is coded as ·−, letter Q is coded as −−·−, and digit 1 
is coded as ·−−−−. The Morse code is case-insensitive, traditionally capital 
letters are used. When the message is written in Morse code, a single space is 
used to separate the character codes and 3 spaces are used to separate words. 
For example, the message HEY JUDE in Morse code is ···· · −·−−   ·−−− ··− −·· ·.
    NOTE: Extra spaces before or after the code have no meaning and should be 
          ignored.
    In addition to letters, digits and some punctuation, there are some special 
service codes, the most notorious of those is the international distress signal 
SOS (that was first issued by Titanic), that is coded as ···−−−···. These 
special codes are treated as single special characters, and usually are 
transmitted as separate words.
    Your task is to implement a function that would take the morse code as input 
and return a decoded human-readable string.
    For example:
    decode_morse('.... . -.--   .--- ..- -.. .')
    #should return "HEY JUDE"
    NOTE: For coding purposes you have to use ASCII characters . and -, not 
          Unicode characters.
    
Good luck!

"""
# ENGLISH_TO_MORSE = {'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.', 'F': '..-.', 'G': '--.', 'H': '....',
#                     'I': '..', 'J': '.---', 'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---', 'P': '.--.',
#                     'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-', 'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-',
#                     'Y': '-.--', 'Z': '--..', '0': '-----', '1': '.----', '2': '..---', '3': '...--', '4': '....-',
#                     '5': '.....', '6': '-....', '7': '--...', '8': '---..', '9': '----.',  'SOS': '...---...', '!': '-.-.--',
#                     '.': '.-.-.-', ',': '--..--'}

# def decode_morse(morse_code):
#     decoded_text = ""
#     morse_code = morse_code.split("   ")
#     morse_code = list(map(lambda word: word.split(), morse_code))
#     for word in morse_code:
#         for char in word:
#             if char in ENGLISH_TO_MORSE.values():
#                 char_position = list(ENGLISH_TO_MORSE.values()).index(char)
#                 decoded_text += list(ENGLISH_TO_MORSE.keys())[char_position]
#         decoded_text += " "
#     return decoded_text.strip()
                

# decode_morse('.... . -.--   .--- ..- -.. .')


""" Smalles possible sum

    Given an array X of positive integers, its elements are to be transformed by 
running the following operation on them as many times as required:
    if X[i] > X[j] then X[i] = X[i] - X[j]
    When no more transformations are possible, return its sum ("smallest 
possible sum").
    For instance, the successive transformation of the elements of input 
X = [6, 9, 21] is detailed below:
X_1 = [6, 9, 12] # -> X_1[2] = X[2] - X[1] = 21 - 9
X_2 = [6, 9, 6]  # -> X_2[2] = X_1[2] - X_1[0] = 12 - 6
X_3 = [6, 3, 6]  # -> X_3[1] = X_2[1] - X_2[0] = 9 - 6
X_4 = [6, 3, 3]  # -> X_4[2] = X_3[2] - X_3[1] = 6 - 3
X_5 = [3, 3, 3]  # -> X_5[1] = X_4[0] - X_4[1] = 6 - 3
The returning output is the sum of the final transformation (here 9).

Example
solution([6, 9, 21]) #-> 9
Solution steps:
[6, 9, 12] #-> X[2] = 21 - 9
[6, 9, 6] #-> X[2] = 12 - 6
[6, 3, 6] #-> X[1] = 9 - 6
[6, 3, 3] #-> X[2] = 6 - 3
[3, 3, 3] #-> X[1] = 6 - 3
Additional notes:
    There are performance tests consisted of very big numbers and arrays of size 
at least 30000. Please write an efficient algorithm to prevent timeout.

"""
import math

def find_pairs2(a):
    while True:
        pairs_flag = False
        for i in range(len(a)):
            next_element = a[(i + 1) % len(a)]
            previous_element = a[(i - 1 + len(a)) % len(a)]
            if a[i] > next_element or a[i] > previous_element:
                pairs_flag = True
                while a[i] > next_element:
                    a[i] -= next_element
                while a[i] > previous_element:
                    a[i] -= previous_element
        if pairs_flag == False: break;
    return(a)

                    
def find_pairs1(a):
    while True:
        pairs_flag = False
        for idx in range(1,len(a) - 1):
            if a[idx] > a[idx + 1]:
                a[idx] = a[idx] - a[idx + 1]
                if pairs_flag == False: pairs_flag = True
        if pairs_flag == False:
            break;
    return(a)

def find_pairs_GCD_edition(a):
    all_gcds = []
    prev_gcd = a[0]
    for i in range(len(a)):
        for gcd in range(prev_gcd, 0, -1):
            if prev_gcd % gcd == 0 and a[(i + 1) % len(a)] % gcd == 0 and a[(i - 1 + len(a)) % len(a)] % gcd == 0:
                all_gcds.append(gcd)
                prev_gcd = gcd
                break
    return(all_gcds)

def find_pairs(a):
    all_gcds = []
    prev_gcd = a[0]
    for i in range(10):
        for gcd in range(prev_gcd, 0, -1):
            if prev_gcd % gcd == 0 and a[(i + 1) % len(a)] % gcd == 0 and a[(i - 1 + len(a)) % len(a)] % gcd == 0:
                all_gcds.append(gcd)
                prev_gcd = gcd
                break
    
    counted_elements = {}
    for i in range(10):
        if all_gcds[i] in counted_elements.keys(): counted_elements[all_gcds[i]] += 1
        else: counted_elements[all_gcds[i]] = 1
    
    return( sorted(counted_elements.items(), key=lambda kv: kv[1])[0][0]) 
    # print(counted_elements)
    # return(all_gcds)

def solution(a):
    print(find_pairs(a))

solution([3, 2, 1])
solution([3, 4, 5, 1])
solution([6, 9, 21])
solution([1, 21, 55])
solution([9])
solution([137641, 203401, 9409, 44944, 3025, 116964, 34969, 169744, 71824, 31684, 17956])
#66
solution([195364, 128164, 8100, 145161, 235225, 71824, 20449, 102400, 21316, 12100, 107584, 5929, 20736, 233289, 126736, 12100, 12544, 96721, 57121, 46225, 190096, 73441, 4096, 70756, 69169, 168100, 196249, 7569, 78400, 116281, 20164, 7569, 193600, 42436, 5041, 61009, 2809, 175561, 108900, 14161, 160000, 165649, 108900, 87025, 159201, 52900, 153664, 248004, 176400, 49729, 80656, 168921, 25600, 81225, 204304, 33856, 176400, 33489, 48841, 61009, 22801, 10201, 116281, 6724, 64009, 170569])