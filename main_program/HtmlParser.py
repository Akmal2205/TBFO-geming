from bs4 import BeautifulSoup
import re

tags=[]
all_nonspace=[]

with open('c:\\Users\\ASUS\\Documents\\TBFO\\TBFO-geming\\test_files\\index.html', 'r', encoding='utf-8') as file:
    # Read the entire content of the file into a variable
    soup = BeautifulSoup(file, "html.parser")

    all_tags = soup.find_all()

for tag in all_tags:
    tags+=[tag.name]

with open('c:\\Users\\ASUS\\Documents\\TBFO\\TBFO-geming\\test_files\\index.html', 'r', encoding='utf-8') as file:
    # Read the entire content of the file into a variable
    for line in file:
        all_nonspace+=re.split(r'[<,>]',line.strip())

print(all_nonspace)