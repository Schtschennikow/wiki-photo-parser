Парсер фотографий чиновников из википедии.

### Установка
1. git clone https://github.com/nmaslov255/wiki-photo-parser.git
2. cd wiki-photo-parser
3. python3 -m venv .
4. source bin/activate
5. pip3 install -r requirements.txt
6. curl 'https://declarator.org/media/dumps/person.json' -o 'persons.json'

### Использование

1) Поиск по википедии страниц персон. Можно включить фильтр по конкретному офису в формате "Управа_района_Вишняки". Возвращает json с карточками персон с ссылкой на сраницу википедии, если она существует. Если на странице есть фото, то карточка будт содержать ссылку на изобращение и лицензию на его использование.

`python parser/main.py --persons 'persons.json' --out 'results.json'`

    optional arguments:
    --persons          путь к json с персонами из декларатора
                        (обязательный аргумент)
    --out              путь для сохранения результата
                        (обязательный аргумент)
    --start-from       файл из которого производилась загрузка, если
                        её необходимо продолжить
                        необходимо продолжить
    --office OFFICE    отфильтровать конкретный офис.
                        полный список офисов можно найти в файле offices.txt

2) Скачивание фотографий по ссылкам собранным из википедии. Поумолчанию фотографии сохраняются в папку ./photos в рабочей директории.

`python parser/photo.py --results 'results.json'`

    optional arguments:
    --results          путь к json-файлу с результатами парсинга
    --from_zero        начать сначала, удалив результаты предыдущих
                        скачиваний
    --go_on            продолжить загрузку из того же или из другого
                        источника (результата парсинга)
