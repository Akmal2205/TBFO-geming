import os
import re

def attribute_generalizer(string):
    pattern_src = re.compile(r'src\s*=\s*"[^"]+"')
    pattern_alt = re.compile(r'alt\s*=\s*"[^"]+"')
    pattern_href = re.compile(r'href\s*=\s*"[^"]+"')
    pattern_id = re.compile(r'id\s*=\s*"[^"]+"')
    pattern_class = re.compile(r'class\s*=\s*"[^"]+"')
    pattern_style = re.compile(r'style\s*=\s*"[^"]+"')
    pattern_action = re.compile(r'action\s*=\s*"[^"]+"')
    result_string = pattern_src.sub('src="*"', string)
    result_string = pattern_alt.sub('alt="*"', result_string)
    result_string = pattern_href.sub('href="*"', result_string)
    result_string = pattern_id.sub('id="*"', result_string)
    result_string = pattern_class.sub('class="*"', result_string)
    result_string = pattern_style.sub('style="*"', result_string)
    result_string = pattern_action.sub('action="*"', result_string)
    return result_string
    

def string_generalizer(lst):
    i=0
    while i!=len(lst)-1:
        if lst[i]==">":
            i+=1
            while lst[i]!="<":
                lst[i]="string"
                i+=1
        i+=1
        if lst[i]=="!--":
            i+=1
            while lst[i]!="--":
                lst[i]="string"
                i+=1
    j=0
    return lst           

def HtmlParser(filename):
    global lines
    global allnonwhitespace
    lines=[]
    allnonwhitespace=[]
    with open(os.path.abspath("../test_files/accepted_inputs/" + filename), 'r', encoding='utf-8') as file:
        # Read the entire content of the file into a variable
        for line in file:
            # all_nonspace+=re.split(r'[<,>]',line.strip())
            # lines+=re.findall(r'<[^>]+>|[^<>]+', ListtoString((line.strip()).split("/r")))
            g_line=attribute_generalizer(line)
            lines+= re.split(r'(<|>| )', (g_line.strip()))
    for el in lines:
        if el != '' and el!=' ':
           allnonwhitespace+=[el]
    # return replace_img_tags(string_generalizer(token(allnonwhitespace)))
    return (string_generalizer(allnonwhitespace))

# filename=input()
# HtmlParser(filename)