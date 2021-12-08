"""Теория и практика языков программирования"""
"""Here I gonna save some scripts while studying python language"""

"""

Complete the method/function so that it converts dash/underscore delimited words 
into camel casing. The first word within the output should be capitalized only 
if the original word was capitalized (known as Upper Camel Case, also often 
referred to as Pascal case).

"""
def to_camel_case(text):
    text = text.replace("-", "_")
    text_without_requested_delimeters = text.split("_")
    for i in range(1,len(text_without_requested_delimeters)):
        text_without_requested_delimeters[i] = (
            text_without_requested_delimeters[i].capitalize())
    line_to_output = "".join(text_without_requested_delimeters)
    return(line_to_output)    
    
print(to_camel_case(input()))