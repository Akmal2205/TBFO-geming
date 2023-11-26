import os
import re

def attribute_generalizer(string): # Untuk mengeneralisir bentuk atribut
    pattern_src = re.compile(r'src\s*=\s*"[^"]+"')
    pattern_alt = re.compile(r'alt\s*=\s*"[^"]+"')
    pattern_href = re.compile(r'href\s*=\s*"[^"]+"')
    pattern_id = re.compile(r'id\s*=\s*"[^"]+"')
    pattern_class = re.compile(r'class\s*=\s*"[^"]+"')
    pattern_style = re.compile(r'style\s*=\s*"[^"]+"')
    pattern_action = re.compile(r'action\s*=\s*"[^"]+"')
    pattern_type = re.compile(r'type\s*=\s*("[^"]*")')
    pattern_method = re.compile(r'method\s*=\s*("[^"]*")')
    pattern_comment = re.compile(r'<!--.*-->')
    result_string = pattern_src.sub('src="*"', string)
    result_string = pattern_comment.sub('<cmd>', string)
    result_string = pattern_alt.sub('alt="*"', result_string)
    result_string = pattern_href.sub('href="*"', result_string)
    result_string = pattern_id.sub('id="*"', result_string)
    result_string = pattern_class.sub('class="*"', result_string)
    result_string = pattern_style.sub('style="*"', result_string)
    result_string = pattern_action.sub('action="*"', result_string)
    result_string = pattern_method.sub(r'method=\1', result_string)
    result_string = pattern_type.sub(r'type=\1', result_string)
    return result_string
    

def string_generalizer(lst): # Untuk mengeneralisir bentuk string
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
    return lst           

def HtmlParser(filename): # Fungsi utama parser
    global lines
    global allnonwhitespace
    lines=[]
    allnonwhitespace=[]
    with open(os.path.abspath("../test_files/" + filename), 'r', encoding='utf-8') as file:
        for line in file:
            g_line=attribute_generalizer(line) # Mengeneralisir atribut per line yang dibaca
            lines+= re.split(r'(<|>| )', (g_line.strip()))
    for el in lines:
        if el != '' and el!=' ': # Menghilangkan kemungkinan whitespace pada list
           allnonwhitespace+=[el]
    return (string_generalizer(allnonwhitespace)) # Return sebuah list hasil parsing html

filename=input()
print(HtmlParser(filename))