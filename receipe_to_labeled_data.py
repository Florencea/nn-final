import codecs
import json
import sys
from itertools import combinations

receipe = json.load(codecs.open(sys.argv[1], 'r', 'utf-8-sig'))
train_list = ['name', 'ingres', 'spices', 'steps']
#train_list = ['name', 'intro', 'ingres', 'spices', 'steps']

def is_None(recipe, combination):
    for cb in combination:
        if recipe[cb] == '' or recipe[cb] is None:
            return True
    return False

def get_label_str(category):
    label_str = ''
    for ct in category:
        label_str += '__label__'
        label_str += ct
    return label_str

for iters in range(1, len(train_list)+1):
    for combination in combinations(train_list, iters):
        train_file = 'training_data/data'
        for cb in combination:
            train_file += '_' + cb
        train_file += '.train'
        with open(train_file, 'w', encoding='utf-8-sig') as text_file:
            print(train_file)
            for rc in receipe:
                if is_None(rc, combination):
                    continue
                label_str = get_label_str(rc['category'])
                print(label_str, end='', file=text_file)
                train_str_list = []
                for cb in combination:
                    tmp_str = ''
                    if cb == 'steps':
                        for i in rc[cb]:
                            tmp_str += i['content'] + ' '
                    else:
                        for i in rc[cb]:
                            tmp_str += i + ' '
                    print(tmp_str, end='', file=text_file)
                print('', file=text_file)