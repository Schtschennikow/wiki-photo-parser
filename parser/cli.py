#!/usr/bin/python3
import argparse

argparser = argparse.ArgumentParser(
    description='Parser photos from wikipedia')

argparser.add_argument('--persons', type=str, default='',
    help='путь к json с персонами из декларатора')

argparser.add_argument('--out', type=str, default='',
    help='путь для сохранения результата')

argparser.add_argument('--start-from', action='store_true', 
    help="файл из которого производилась загрузка, если её необходимо продолжить")

argparser.add_argument('--office', type=str, default='',
    help='отфильтровать конкретный офис. полный список офисов можно найти в файле offices.txt')

args = argparser.parse_args()