import statistics
from itertools import combinations

import recipe_classifier_verifier as trainer

test_times = 10
verify_mode = False
combination_length = 1

train_list = ['name', 'intro', 'ingres', 'steps']
# train_list = ['name_intro_ingres']
training_list = []
for iters in range(combination_length, len(train_list) + 1):
    for combination in combinations(train_list, iters):
        train_file = 'data'
        for cb in combination:
            train_file += '_' + cb
        train_file += '.train'
        training_list.append(train_file)

lr_list = [0.2, 0.4, 0.6]
epoch_list = [5, 20, 35, 50]
wng_list = [1]
# lr_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
# epoch_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# wng_list = [1]

if verify_mode:
    for training_source in training_list:
        with open('verified_result/' + training_source.split('.')[0].replace('data_', 'result_') + '.csv', 'w', encoding='utf-8-sig') as result_csv:
            print("原分類", "被分成", "\t原始資料", file=result_csv)
            for lr_i in lr_list:
                for ep_i in epoch_list:
                    for wng_i in wng_list:
                        print('doing ' + training_source + ' lr=' + str(lr_i) + ', epoch=' + str(ep_i) + ', word_ngrams=' + str(wng_i))
                        for test_i in range(test_times):
                            results = trainer.get_result_from(training_source, lr=lr_i, epoch=ep_i, word_ngrams=wng_i, verify=verify_mode)
                            for result in results:
                                print(result, file=result_csv)
else:
    with open('result/result.csv', 'w', encoding='utf-8-sig') as result_csv:
        for training_source in training_list:
            t = tuple('訓練資料來源 訓練資料筆數 驗證資料筆數 訓練次數 驗證時k值 lr epoch word_ngrams 精確度平均 精確度標準差 召回率平均 召回率標準差'.split(' '))
            print('%s %21s %7s %s %5s %3s %6s %4s %4s %4s %4s %4s' % t, file=result_csv)
            for lr_i in lr_list:
                for ep_i in epoch_list:
                    for wng_i in wng_list:
                        result_p = []
                        result_r = []
                        result_cnt = 0
                        result_nexample = 0
                        print('doing ' + training_source + ' lr=' + str(lr_i) + ', epoch=' + str(ep_i) + ', word_ngrams=' + str(wng_i))
                        for test_i in range(test_times):
                            result = trainer.get_result_from(training_source, lr=lr_i, epoch=ep_i, word_ngrams=wng_i, verify=verify_mode)
                            result_p.append(result.precision)
                            result_r.append(result.recall)
                            result_cnt = result.ntrain
                            result_nexample = result.nexamples
                        tmp = training_source[training_source.find('_') + 1: training_source.find('.')]
                        print('%-23s' % tmp + '%12d' % result_cnt + '%12s' % result_nexample + '%9s' % test_times + '%9s' % 1 + '%8s' % lr_i + '%5s' % ep_i + '%10s' % wng_i, end='', file=result_csv)
                        print('{:14.3%}'.format(statistics.mean(result_p)), '{:9.3%}'.format(statistics.stdev(result_p)), '{:10.3%}'.format(statistics.mean(result_r)), '{:9.3%}'.format(statistics.stdev(result_r)), file=result_csv)
            print('', file=result_csv)
