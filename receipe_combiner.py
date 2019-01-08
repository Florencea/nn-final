import codecs
import json

cate_type = json.load(codecs.open('./original_data/cate_type.json', 'r', 'utf-8-sig'))
rec_type = json.load(codecs.open('./original_data/rec_type.json', 'r', 'utf-8-sig'))
steps = json.load(codecs.open('./original_data/steps.json', 'r', 'utf-8-sig'))
receipe = json.load(codecs.open('./original_data/receipe.json', 'r', 'utf-8-sig'))

cate_dict = {}
for ct in cate_type:
    cate_dict[ct['id']] = ct['name']

rec_dict = {}
for rd in rec_type:
    if rd['id_rec'] not in rec_dict:
        rec_dict[rd['id_rec']] = []
        rec_dict[rd['id_rec']].append(cate_dict[rd['id_type']])
    else:
        rec_dict[rd['id_rec']].append(cate_dict[rd['id_type']])

steps_dict = {}
for st in steps:
    stt = {
        'step': st['step'],
        'content': st['content']
    }
    if st['id_receipe'] not in steps_dict:
        steps_dict[st['id_receipe']] = []
        steps_dict[st['id_receipe']].append(stt)
    else:
        steps_dict[st['id_receipe']].append(stt)

receipe_output_categoried = []
receipe_output_uncategoried = []
receipe_empty = []

for rp in receipe:
    tmp = steps_dict[rp['id']] if rp['id'] in steps_dict else None
    if rp['name'] == '' or rp['name'] is None or rp['introduce'] == '' or rp['introduce'] is None or rp['id'] not in steps_dict:
        receipe_empty.append(rp)
    if rp['id'] not in rec_dict:
        rpp = {
            'id': rp['id'],
            'name': rp['name'],
            'intro': rp['introduce'],
            'steps': tmp,
            'category': []
        }
        receipe_output_uncategoried.append(rpp)
    else:
        rpp = {
            'id': rp['id'],
            'name': rp['name'],
            'intro': rp['introduce'],
            'steps': tmp,
            'category': rec_dict[rp['id']]
        }
        receipe_output_categoried.append(rpp)

print('未分類食譜： ' + str(len(receipe_output_uncategoried)) + ' 筆')
print('已分類食譜： ' + str(len(receipe_output_categoried)) + ' 筆')
print('資料欄位欄位空缺食譜： ' + str(len(receipe_empty)) + ' 筆')

with open('receipe_categoried.json', 'w', encoding = 'utf-8-sig') as json_file:
    json.dump(receipe_output_categoried, json_file)

with open('receipe_uncategoried.json', 'w', encoding = 'utf-8-sig') as json_file:
    json.dump(receipe_output_uncategoried, json_file)
