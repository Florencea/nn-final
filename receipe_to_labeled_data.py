import codecs
import json
import sys

receipe = json.load(codecs.open(sys.argv[1], 'r', 'utf-8-sig'))

with open('data_name.train', 'w') as text_file:
    for rc in receipe:
        label_str = ''
        for ct in rc['category']:
            label_str += '__label__'
            label_str += ct
            label_str += ' '
        print(label_str + rc['name'], file=text_file)

with open('data_intro.train', 'w') as text_file:
    for rc in receipe:
        label_str = ''
        for ct in rc['category']:
            label_str += '__label__'
            label_str += ct
            label_str += ' '
        print(label_str + rc['intro'], file=text_file)

with open('data_steps.train', 'w') as text_file:
    for rc in receipe:
        label_str = ''
        for ct in rc['category']:
            label_str += '__label__'
            label_str += ct
            label_str += ' '
        step_str = ''
        for st in rc['steps']:
            step_str += st['content']
        print(label_str + step_str, file=text_file)

with open('data_name_intro.train', 'w') as text_file:
    for rc in receipe:
        label_str = ''
        for ct in rc['category']:
            label_str += '__label__'
            label_str += ct
            label_str += ' '
        print(label_str + rc['name'] + ' ' + rc['intro'], file=text_file)

with open('data_name_steps.train', 'w') as text_file:
    for rc in receipe:
        label_str = ''
        for ct in rc['category']:
            label_str += '__label__'
            label_str += ct
            label_str += ' '
        step_str = ''
        for st in rc['steps']:
            step_str += st['content']
        print(label_str + rc['name'] + ' ' + step_str, file=text_file)

with open('data_intro_steps.train', 'w') as text_file:
    for rc in receipe:
        label_str = ''
        for ct in rc['category']:
            label_str += '__label__'
            label_str += ct
            label_str += ' '
        step_str = ''
        for st in rc['steps']:
            step_str += st['content']
        print(label_str + rc['intro'] + ' ' + step_str, file=text_file)

with open('data_name_intro_steps.train', 'w') as text_file:
    for rc in receipe:
        label_str = ''
        for ct in rc['category']:
            label_str += '__label__'
            label_str += ct
            label_str += ' '
        step_str = ''
        for st in rc['steps']:
            step_str += st['content']
        print(label_str + rc['name'] + ' ' + rc['intro'] + ' ' + step_str, file=text_file)
