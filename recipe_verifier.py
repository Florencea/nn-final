import statistics
import recipe_classifier_verifier as trainer

test_times = 1

training_list = [
    'data_ingres.train',
    'data_name_ingres.train',
    'data_ingres_steps.train',
    'data_name_ingres_steps.train'
]

# lr_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
# epoch_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]
# wng_list = [1]

lr_list = [0.6]
epoch_list = [5]
wng_list = [1]

for training_source in training_list:
    with open('verified_result/' + training_source.split('.')[0].replace('data_', 'result_') + '.csv', 'w', encoding='utf-8-sig') as result_csv:
        print("原分類", "被分成", "原始資料", file=result_csv)
        for lr_i in lr_list:
            for ep_i in epoch_list:
                for wng_i in wng_list:
                    print('doing ' + training_source + ' lr=' + str(lr_i) + ', epoch=' + str(ep_i) + ', word_ngrams=' + str(wng_i))
                    for test_i in range(test_times):
                        results = trainer.get_result_from(training_source, lr=lr_i, epoch=ep_i, word_ngrams=wng_i)
                        for result in results:
                            print(result, file=result_csv)
