import codecs
import json

cate_type = json.load(codecs.open('./original_data/cate_type.json', 'r', 'utf-8-sig'))
rec_type = json.load(codecs.open('./original_data/rec_type.json', 'r', 'utf-8-sig'))
steps = json.load(codecs.open('./original_data/steps.json', 'r', 'utf-8-sig'))
rec_ingre = json.load(codecs.open('./original_data/rec_ingre.json', 'r', 'utf-8-sig'))
ingredient = json.load(codecs.open('./original_data/ingredient.json', 'r', 'utf-8-sig'))
spices = json.load(codecs.open('./original_data/rec_ingre_spi.json', 'r', 'utf-8-sig'))
receipe = json.load(codecs.open('./original_data/receipe.json', 'r', 'utf-8-sig'))

cate_dict = {}
for ct in cate_type:
    cate_dict[ct['id']] = ct['name']

def merge_type(type_id):
    type_id = int(type_id)
    if type_id==0 or type_id==1 or type_id==12:
        type_id = 0
    elif type_id==3:
        type_id = 3
    elif type_id==16:
        type_id = 16
    else:
        type_id = 2
    return str(type_id)

rec_dict = {}
for rd in rec_type:
    if rd['id_rec'] not in rec_dict:
        rec_dict[rd['id_rec']] = []
        rec_dict[rd['id_rec']].append(cate_dict[merge_type(rd['id_type'])])
    else:
        rec_dict[rd['id_rec']].append(cate_dict[merge_type(rd['id_type'])])

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

ingre_dict = {}
for ingre in ingredient:
    ingre_dict[ingre['id']] = ingre['name']

rec_ingre_dict = {}
for ri in rec_ingre:
    if ri['id_rec'] not in rec_ingre_dict:
        rec_ingre_dict[ri['id_rec']] = []
        rec_ingre_dict[ri['id_rec']].append(ingre_dict[ri['id_ingre']])
    else:
        rec_ingre_dict[ri['id_rec']].append(ingre_dict[ri['id_ingre']])

spices_dict = {}
for sp in spices:
    if sp['rec_id'] not in spices_dict:
        spices_dict[sp['rec_id']] = []
        spices_dict[sp['rec_id']].append(sp['ingre'])
    else:
        spices_dict[sp['rec_id']].append(sp['ingre'])

receipe_output_categoried = []
receipe_output_uncategoried = []
receipe_empty = []

for rp in receipe:
    tmp_steps = steps_dict[rp['id']] if rp['id'] in steps_dict else None
    tmp_ingres = rec_ingre_dict[rp['id']] if rp['id'] in rec_ingre_dict else None
    tmp_spices = spices_dict[rp['id']] if rp['id'] in spices_dict else None
    if rp['name'] == '' or rp['name'] is None or rp['introduce'] == '' or rp['introduce'] is None or rp['id'] not in steps_dict:
        receipe_empty.append(rp)
    if rp['id'] not in rec_dict or rec_dict[rp['id']][0] == 'null':
        rpp = {
            'id': rp['id'],
            'name': rp['name'],
            'intro': rp['introduce'],
            'steps': tmp_steps,
            'ingres': tmp_ingres,
            'spices': tmp_spices,
            'category': []
        }
        receipe_output_uncategoried.append(rpp)
    else:
        rpp = {
            'id': rp['id'],
            'name': rp['name'],
            'intro': rp['introduce'],
            'steps': tmp_steps,
            'ingres': tmp_ingres,
            'spices': tmp_spices,
            'category': rec_dict[rp['id']]
        }
        receipe_output_categoried.append(rpp)

print('未分類食譜： ' + str(len(receipe_output_uncategoried)) + ' 筆')
print('已分類食譜： ' + str(len(receipe_output_categoried)) + ' 筆')
print('資料欄位欄位空缺食譜： ' + str(len(receipe_empty)) + ' 筆')

with open('temp/receipe_categoried.json', 'w', encoding='utf-8-sig') as json_file:
    json.dump(receipe_output_categoried, json_file)

with open('temp/receipe_uncategoried.json', 'w', encoding='utf-8-sig') as json_file:
    json.dump(receipe_output_uncategoried, json_file)
