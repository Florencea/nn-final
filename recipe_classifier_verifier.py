import math
import random
import fasttext

def get_result_from(input_file, lr=0.1, epoch=5, word_ngrams=1, k=1, sample_rate=0.9, verify=True):
    training_data_all = []
    with open('training_data/' + input_file, 'r', encoding='utf-8-sig') as training_file:
        for line in training_file:
            training_data_all.append(line)
    training_data_counts = len(training_data_all)
    training_data_sample_counts = math.floor(training_data_counts * sample_rate)
    sample_seq = random.sample(range(training_data_counts), k=training_data_sample_counts)
    verified_seq = list(set(range(training_data_counts)) - set(sample_seq))
    data_sampled = []
    data_verified = []
    for ds in sample_seq:
        data_sampled.append(training_data_all[ds])
    for dv in verified_seq:
        data_verified.append(training_data_all[dv])
    with open('temp/' + input_file.split('.')[0] + '.sample', 'w', encoding='utf-8-sig') as sampled_file:
        for line in data_sampled:
            print(line.rstrip(), file=sampled_file)
    training_source = 'temp/' + input_file.split('.')[0] + '.sample'
    model_name = 'models/' + input_file.split('.')[0].replace('data', 'model')
    classifier = fasttext.supervised(training_source, model_name, lr=lr, epoch=epoch, word_ngrams=word_ngrams)

    if verify:
        verified_list = []
        lable_list = []
        for d in data_verified:
            lable_list.append(d[d.find('l__')+3: d.find(' ')])
            verified_list.append(d[d.find(' '): len(d)])

        results = classifier.predict_proba(verified_list, k=1)
        result_list = []
        for result in results:
            for r in result: 
                result_list.append(r[0])

        wrong = 0
        handled_result_list = []
        for idx in range(0, len(result_list)):
            if lable_list[idx] != result_list[idx]:
                wrong += 1 
                tmp_str = '' + lable_list[idx] + ' => ' + result_list[idx] + ' => ' + verified_list[idx]
                handled_result_list.append(tmp_str)

        print('驗證資料數 :', len(results))
        print('錯誤分類數 :', wrong)
        print('正確率 :', 100-(wrong/len(results)*100), '%')
        return handled_result_list

    else:
        with open('temp/' + input_file.split('.')[0] + '.verified', 'w', encoding='utf-8-sig') as verified_file:
            for line in data_verified:
                print(line.rstrip(), file=verified_file)
        verified_source = 'temp/' + input_file.split('.')[0] + '.verified'
        training_source = 'temp/' + input_file.split('.')[0] + '.sample'
        verified_source = 'temp/' + input_file.split('.')[0] + '.verified'
        result = classifier.test(verified_source, k=k)
        result.ntrain = training_data_counts
        return result