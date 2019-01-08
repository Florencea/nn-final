import statistics

import receipe_classifier as trainer

test_times = 10

training_list = [
    'data_name.train',
    'data_intro.train',
    'data_steps.train',
    'data_name_intro.train',
    'data_name_steps.train',
    'data_intro_steps.train',
    'data_name_intro_steps.train'
]

lr_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
epoch_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
wng_list = [1]

for training_source in training_list:
    with open('result/' + training_source.split('.')[0].replace('data_', 'result_') + '.csv', 'a', encoding='utf-8-sig') as result_csv:
        print('"訓練資料來源", "訓練資料筆數", "驗證資料筆數", "訓練次數", "驗證時k值", "lr", "epoch", "word_ngrams", "精確度平均", "精確度標準差", "召回率平均", "召回率標準差"', file=result_csv)
        for lr_i in lr_list:
            for ep_i in epoch_list:
                for wng_i in wng_list:
                    result_p = []
                    result_r = []
                    result_cnt = 0
                    result_nexample = 0
                    print('doing ' + training_source + ' lr=' + str(lr_i) + ', epoch=' + str(ep_i) + ', word_ngrams=' + str(wng_i))
                    for test_i in range(test_times):
                        result = trainer.get_result_from(training_source, lr=lr_i, epoch=ep_i, word_ngrams=wng_i)
                        result_p.append(result.precision)
                        result_r.append(result.recall)
                        result_cnt = result.ntrain
                        result_nexample = result.nexamples
                    print('"' + training_source + '", ' + str(result_cnt) + ', ' + str(result_nexample) + ', ' + str(test_times) + ', 1, ' + str(lr_i) + ', ' + str(ep_i) + ', ' + str(wng_i) + ', ' + str(statistics.mean(result_p)) + ', ' + str(statistics.stdev(result_p)) + ', ' + str(statistics.mean(result_r)) + ', ' + str(statistics.stdev(result_r)) + '', file=result_csv)
