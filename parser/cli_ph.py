#!/usr/bin/python3
import argparse

argparser = argparse.ArgumentParser(
    description='Parser photos from wikipedia')

argparser.add_argument('--results', type=str, default='',
    help='путь к .json-файлу с результатами парсинга')

argparser.add_argument('--from_zero', action='store_true',
    help='начать сначала, удалив результаты предыдущих скачиваний')

argparser.add_argument('--go_on', action='store_true',
    help='продолжить загрузку из того же или из другого источника (результата парсинга)')

args = argparser.parse_args()