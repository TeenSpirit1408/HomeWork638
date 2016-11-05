#!/usr/bin/env python3

import argparse
import sys
import os

# создаём парсер и описываем все параметры командной строки, которые может
# принимать наша программа
parser = argparse.ArgumentParser(
    description='Отображает древовидную структуру катологов и файлов'
)

parser.add_argument(
    # название поля в объекте, где будут сохранены параметры
    'directory',
    # название параметров, которое будет отображено в справке
    metavar='DIRECTORY',
    # сообщаем что ожидается строка
    type=str,
    # параметр будет один
    nargs='?',
    # краткое описание параметра
    help='назавние интересуещей вас директории'
)

# описываем опцию
parser.add_argument(
    # короткое название опции
    '-fo',
    # длинное название опции
    '--folders-only',
    # парсер сохранит значение True, если встретит эту опцию
    action='store_true',
    # краткое описание опции
    help='не отображает файлы в дереве'
)

# описываем опцию
parser.add_argument(
    # короткое название опции
    '-in',
    # длинное название опции
    '--include',
    # парсер сохранит значение если встретит эту опцию
    action='store',
    # краткое описание опции
    help='отображает только те файлы, в названии которых встречается текст SOME_TEXT'
)

# описываем опцию
parser.add_argument(
    # короткое название опции
    '-ex',
    # длинное название опции
    '--exclude',
    # парсер сохранит значение если встретит эту опцию
    action='store',
    # краткое описание опции
    help='не отображает те файлы, в названии которых встречается текст SOME_TEXT'
)

# описываем опцию
parser.add_argument(
    # короткое название опции
    '-a',
    # длинное название опции
    '--all',
    # парсер сохранит значение True, если встретит эту опцию
    action='store_true',
    # краткое описание опции
    help='отображает скрытые файлы/директории (начинающиеся с .)'
)

# описываем опцию
parser.add_argument(
    # короткое название опции
    '-fn',
    # длинное название опции
    '--full-name',
    # парсер сохранит значение True, если встретит эту опцию
    action='store_true',
    # краткое описание опции
    help='выводит полный текущий путь'
)

args = parser.parse_args()

if not os.path.exists(args.directory) or not os.path.isdir(args.directory):
    print('Указанный путь не существует или не является папкой')
else:
    content = os.listdir(args.directory)
    for i in range(len(content)):
        print(content[i])
        if os.path.isdir(content[i]):
            content[i] = os.listdir(content[i])
            print(content[i])
