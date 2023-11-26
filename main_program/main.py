import argparse
from HtmlParser import HtmlParser
from txtParser import txtParser

if __name__ == "__main__": # Agar input sesuai dengan format di spek
    parser = argparse.ArgumentParser(description='Process two files.')
    parser.add_argument('file1', type=str, help='First file name')
    parser.add_argument('file2', type=str, help='Second file name')

    args = parser.parse_args()

    file1 = args.file1
    file2 = args.file2

productions=(txtParser(file1)) # Merupakan list yang berisi productions [#State, Html section, description](Pembagi state), [Current state, Symbol read, Top of stack, Next state, Current top of stack]
html_parse=(HtmlParser(file2)) # Merupakan list yang berisi hasil parsing dari html code displit berdasarkan karakter "<", ">", dan spasi


current_state="q0"
current_topstack=["Z"]

def isPrdFound(state, symbol, top_stack): # Mengembalikan indeks production apabila ditemukan dan -1 apabila tidak ditemukan
    i=0
    index = -1
    for prod in productions:
        if prod[0]==state and prod[1]==symbol and prod[2]==top_stack:
            index=i
            break
        else:
            i+=1
    return index

def nextState(index): # Mengembalikan next state
    state = productions[index][3]
    return state

def nextTopStack(index): # Mengembalikan next top stack
    topstack = productions[index][len(productions[1])-1]
    return topstack
    
# PDA Checking Section
Valid = True
for el in html_parse:
    if isPrdFound(current_state, el, current_topstack[len(current_topstack)-1])!=-1:
        temp_state=nextState(isPrdFound(current_state, el, current_topstack[len(current_topstack)-1]))
        temp_topstack=[nextTopStack(isPrdFound(current_state, el, current_topstack[len(current_topstack)-1]))]
        current_state=temp_state
        current_topstack+=temp_topstack
        print(current_state, current_topstack[len(current_topstack)-1], el)
    else:
        print(current_state, current_topstack[len(current_topstack)-1], el)
        Valid = False
        break

if Valid :
    print("Accepted")
else:
    print("Syntax Error")