import codecs
import json
import re
import sys

receipe = json.load(codecs.open(sys.argv[1], 'r', 'utf-8-sig'))
regexp = '[\s+\.\/\!_,$%^*(+\"\']+|[+——！，。？?、~@#￥%……&*（）(){}~`-【】：:～><＞＜]+'

for rc in receipe:
    rc['name'] = re.sub(regexp, ' ', rc['name'])
    rc['name'] = re.sub(' +', ' ', rc['name'])
    rc['intro'] = re.sub(regexp, ' ', rc['intro'])
    rc['intro'] = re.sub(' +', ' ', rc['intro'])
    for st in rc['steps']:
        st['content'] = re.sub(regexp, ' ', st['content'])
        st['content'] = re.sub(' +', ' ', st['content'])

with open(sys.argv[1].split('.')[0] + '_cleared.json', 'w') as json_file:
    json.dump(receipe, json_file)
