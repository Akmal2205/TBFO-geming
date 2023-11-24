from bs4 import BeautifulSoup
import re
import os

tags=[]
all_nonspace=[]

name = input("Masukan nama file: ") 

with open(os.path.abspath("../TBFO-GEMING/test_files/" + name), 'r', encoding='utf-8') as file:
    # Read the entire content of the file into a variable
    soup = BeautifulSoup(file, "html.parser")

    all_tags = soup.find_all()

for tag in all_tags:
    tags+=[tag.name]

with open(os.path.abspath("../TBFO-GEMING/test_files/" + name), 'r', encoding='utf-8') as file:
    # Read the entire content of the file into a variable
    for line in file:
        all_nonspace+=re.split(r'[<,>]',line.strip())

print(all_nonspace)