import receipe_classifier as trainer

result = trainer.get_result_from('data_name.train', sample_rate=0.5)
print(result.precision)
print(result.recall)
print(result.nexamples)
