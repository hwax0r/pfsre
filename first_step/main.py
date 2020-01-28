import os
from bs4 import BeautifulSoup

this_dir = os.path.abspath(os.getcwd()) + '/first_step/'
file_names = ['first', 'second', 'third']

def wrong_answer_txt(file_name):
    ''''''
    file_input = this_dir + 'txts/' + str(file_name) + '.txt'
    matrix = open(file_input, 'r').read()
    numbers = matrix.split()
    result = 0
    for elem in numbers:
        result += int(elem)
    return result

def wrong_not_gut_answer_html(file_name):
    ''''''
    file_input = this_dir + 'htmls/' + str(file_name) + '.html'
    html_file = open(file_input).read()
    html_context = str(html_file).split()
    result = 0
    for elem in html_context:
        if elem.isdigit(): result += int(elem)
    return result

# def as_needed_bs4(file_name):
#     file_input = this_dir + 'htmls/' + str(file_name) + '.html'
#     html_file = BeautifulSoup(file_input.encode('utf-8'), 'html.parser')
#     print(html_file)

def output(file_names):
    print(file_names + ':')
    print(wrong_answer_txt(files))
    # print(wrong_not_gut_answer_html(files))
    print('\n')

# as_needed_bs4('first')

for files in file_names:
    output(files)
    