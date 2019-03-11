import os
import shutil
import json
from progress.bar import Bar
import requests
import cli_ph
from logs import CLIlog


with open(cli_ph.args.results, 'r', encoding='utf-8') as f:
    data = json.load(f)

no_url = []

if cli_ph.args.from_zero and os.path.isdir('photos'):
    shutil.rmtree("photos")

if not "photos" in os.listdir('.'):
    os.mkdir("photos")

if cli_ph.args.go_on and len(os.listdir('photos')) > 0:
    done_pics = [int(name[:-4]) for name in os.listdir('photos')]
    for idx, person in enumerate(data):
        if not int(person['id']) in done_pics:
            data = data[idx+1:]; break
        Progress.next()
    if os.path.isfile('problem.json'):
        with open('problem.json', 'r') as pf:
            no_url.extend(json.load(pf))

progress = Bar('Загрузка фотокарточек:', 
               max=len(data))

for info in data:
    if 'photo' in info:
        url = info['photo']['url']
        pic = requests.get(url).content

        f = open(f"photos/{info['id']}.png", "wb")
        f.write(pic)       
        f.close()
    else:
        no_url.append(info)
        with open('problem.json', 
                  'w', 
                  encoding='utf-8') as pf:
            json.dump(no_url, pf)
    progress.next()
    
CLIlog.info('Фото собраны и сохранены в папке ./photos\n')
CLIlog.info(f'Для {len(no_url)} персон ссылок на фото нет.\n'+
  'Список этих персон сохранён в файле /problem.json\n')