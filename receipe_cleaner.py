import codecs
import json
import re
import sys

receipe = json.load(codecs.open(sys.argv[1], 'r', 'utf-8-sig'))
regexp = r'[0-9\s+\.\/\!_,$%^*(+\"\'\[\]\-]+|[+——！，。？?、~@#￥%……&*（）(){}~`-【】﹝﹞￣︶￣ ／｜：:～><＞＜・ノ]+'

for rc in receipe:
    if rc['name'] != '' and rc['name'] is not None:
        rc['name'] = re.sub(regexp, ' ', rc['name'])
        rc['name'] = re.sub(' +', ' ', rc['name'])
        rc['name'] = rc['name'].replace('私房食譜', '')
    if rc['intro'] != '' and rc['intro'] is not None:
        rc['intro'] = re.sub(regexp, ' ', rc['intro'])
        rc['intro'] = re.sub(' +', ' ', rc['intro'])
    if rc['steps'] is not None:
        for st in rc['steps']:
            st['content'] = re.sub(regexp, ' ', st['content'])
            st['content'] = re.sub(' +', ' ', st['content'])

with open(sys.argv[1].split('.')[0] + '_cleared.json', 'w', encoding='utf-8-sig') as json_file:
    json.dump(receipe, json_file)
