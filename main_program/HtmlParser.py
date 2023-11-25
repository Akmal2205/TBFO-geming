import os
import re

def string_generalizer(string):
    lst=[]
    for el in string:
        if el == '':
            lst+=["string"]
        else:
            lst+=[el]
    return lst

def token(lst):
    text = ''.join(lst)  # Convert the list to a single string
    pattern = r'(<[^<>]*>)|[^<>]+'  # Regex pattern to match strings enclosed in < and >
    enclosed_strings = re.findall(pattern, text)
    return enclosed_strings

def HtmlParser(filename):
    global lines
    global allnonwhitespace
    lines=[]
    allnonwhitespace=[]
    with open(os.path.abspath("../test_files/" + filename), 'r', encoding='utf-8') as file:
        # Read the entire content of the file into a variable
        for line in file:
            # all_nonspace+=re.split(r'[<,>]',line.strip())
            lines+=(line.strip()).split(" ")
    for el in lines:
        if el != '':
           allnonwhitespace+=el
    return string_generalizer(token(allnonwhitespace))

# filename=input()
# HtmlParser(filename)