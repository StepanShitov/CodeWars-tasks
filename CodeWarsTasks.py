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