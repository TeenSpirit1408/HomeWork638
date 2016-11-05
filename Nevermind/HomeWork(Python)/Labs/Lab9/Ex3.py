#!/usr/bin/env python3
import sys
import os

files_input = []
for arg in sys.argv[1:]:
    files_input.append(arg)

if len(files_input) == 0:
    print('Укажите хотя бы один файл')
else:
    files_for_print = []
    for elem in files_input:
        a = '/home/user/PycharmProjects/HomeWork/Lab9/'
        a = a + elem
        if os.path.exists(a):
            text_file = open(a, 'r')
            a = text_file.read()
            files_for_print.append(a)
        else:
            print('Файла ' + elem + ' не существует')
    for i in range(len(files_for_print)):
        print(files_for_print[i])
