#!/usr/bin/python3
import sys, os
import json
import re

import requests
from requests import exceptions as reqext
from progress.bar import Bar
from logs import Querylog, CLIlog

import exceptions 
import parser
import api
import cli


if __name__ == '__main__':
    CLIlog.info('Загружаю чиновников из файла\n')
    persons = parser.get_persons_from_dump(cli.args.persons)
    
    if cli.args.office:
    	persons = [info for info in persons 
             if cli.args.office.replace('_', ' ') in info['offices']]

    CLIlog.info(f'Всего чиновников: {len(persons)}')

    Progress = Bar('Обрабатываю каждую персону:', max=len(persons))

    if cli.args.start_from:
        try:
            with open(cli.args.start_from) as fp:
                wiki_persons = json.loads(fp.read())
            
            for idx, person in enumerate(persons):
                if person['id'] == wiki_persons[-1]['id']:
                    persons = persons[idx+1:]; break
                Progress.next()
            else:
                Progress.finish()
                message = "Не сумел найти последний id в указанном файле."
                CLIlog.critical(message); sys.exit(0)
        except FileNotFoundError:
            CLIlog.error('Не найден файл: %s' % cli.args.start_from)
            sys.exit(0)    
    else:
        wiki_persons = []
    
    abr = []

    try:
        for idx, person in enumerate(persons):
            if not re.search(r'([А-ЯЁ]\.)+', person['name']):
                person['name'] = person['name'].replace('.', '').replace(',', '')
                try:
                    wiki_persons.append(parser.parse_person(person))
                except exceptions.WikiError as e:
                    # TODO: idx must be equal person_id
                    Querylog.error("person_number: %i, %s" % (idx, e.msg))
                except reqext.Timeout:
                    message = "person_number: %i, Query timeout is expired" % idx
                    Querylog.error(message)
            else:
                abr.append(person)
            Progress.next()
    except BaseException as e:
        Querylog.critical(e)
    finally:    
        Progress.finish()

        CLIlog.info(f'На википедии удалось найти {len(wiki_persons)} персон\n')
        CLIlog.info(('Время работы %i сек' % Progress.elapsed))

        with open(cli.args.out, 'w', encoding='utf-8') as fp:
            json.dump(wiki_persons, fp)

        CLIlog.info('Данные сохранены в папке: ')
        CLIlog.info(os.path.abspath(cli.args.out))
        # CLIlog.info(abr)