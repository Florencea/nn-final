# nn-final

## 開發筆記

-   使用python版本的[fasttext(v0.8.3)](https://pypi.org/project/fasttext/)

    -   `pip3 install Cython fasttext`

-   專案目錄結構

    -   原始碼皆放置於頂層目錄
    -   期末報告投影片`presentation.pptx`
    -   `models`放置已訓練之模型(執行程式前須先自行創建)
    -   `original_data`放置自資料庫輸出之原始資料表(未合併)
    -   `result`放置實驗結果
    -   `temp`作為一般工作目錄
    -   `training_data`放置訓練資料

## 流程

-   合併原始資料表、分離未分類食譜，空資料(沒有`name` or 沒有`intro` or 沒有`steps`)於製作訓練資料時再去除

    -   `python3 receipe_combiner.py`
    -   資料欄位欄位空缺食譜： 32219 筆
    -   已分類食譜： 43285 筆(`temp/receipe_categoried.json`)
    -   未分類食譜： 1606 筆(`temp/receipe_uncategoried.json`)

-   清理資料中所有標點符號與非法字元

    -   `python3 receipe_cleaner.py temp/receipe_categoried.json`
    -   `python3 receipe_cleaner.py temp/receipe_uncategoried.json`
    -   輸出`temp/receipe_categoried_cleared.json`
    -   輸出`temp/receipe_uncategoried_cleared.json`

-   製作標記訓練資料(若使用到的屬性為空資料則不採用)

    -   `python3 receipe_to_labeled_data.py temp/receipe_categoried_cleared.json`
    -   輸出

        -   `training_data/data_name.train`
        -   `training_data/data_intro.train`
        -   `training_data/data_steps.train`
        -   `training_data/data_name_intro.train`
        -   `training_data/data_name_steps.train`
        -   `training_data/data_intro_steps.train`
        -   `training_data/data_name_intro_steps.train`

-   訓練模型並驗證結果

    -   `receipe_classifier.py`作為模組，會自主執行抽樣、訓練、驗證

        ```python
        import receipe_classifier as trainer
        result = trainer.get_result_from('data_name.train')
        print(result.precision)
        print(result.recall)
        print(result.nexamples)
        print(result.ntrain)
        ```

    -   可使用參數說明：

        -   `input_file`(必須)，訓練資料路徑，會自動加上`training_data/`前綴
        -   `lr`，learning rate(0則模型不再變更)(0.1~1.0)，預設值`lr=0.1`
        -   `epoch`，epoch(會掃過每筆資料幾次)(5~50)，預設值`epoch=5`
        -   `word_ngrams`，word N grams(詞組)(1~5)，預設值`word_ngrams=1`
        -   `k`，驗證用的k值，預設值`k=1`
        -   `sample_rate`，訓練資料中有多少比例拿來做模型，預設值`sample_rate=0.9`

    -   回傳結果說明：

        -   `result.precision`，於`k=k`時的精確度
        -   `result.recall`，於`k=k`時的召回率
        -   `result.nexamples`，驗證的資料筆數
        -   `result.ntrain`，用於訓練的資料筆數

        ```python
        import receipe_classifier as trainer
        result = trainer.get_result_from('data_name.train', lr=0.1, epoch=5, word_ngrams=1, k=1, sample_rate=0.9)
        print(result.precision)
        print(result.recall)
        print(result.nexamples)
        print(result.ntrain)
        ```

-   自動執行訓練並於`result`目錄產生`.csv`結果

    -   `python3 receipe_test.py`
    -   預設將各組合執行`10`次(暫定，`100`次有點久)

        -   `lr_list = [0.1, 0.2, 0.3, 0.4, 0.5, 0.6]`，超過`0.6`會發生`Segmentation fault`，原因不明
        -   `epoch_list = [5, 10, 15, 20, 25, 30, 35, 40, 45, 50]`
        -   `word_ngrames = [1]`，超過1就會發生`Floating point exception`，推測是因為英文詞組使用空格分隔，中文語句過長導致的

    -   輸出各組合之精確度、召回率之平均值與標準差

## 訓練模式

### 單屬性

-   `name` [執行結果](result/result_name.csv)
-   `intro` [執行結果](result/result_intro.csv)
-   `steps` [執行結果](result/result_steps.csv)

### 兩屬性

-   `name` + `intro` [執行結果](result/result_name_intro.csv)
-   `name` + `steps` [執行結果](result/result_name_steps.csv)
-   `intro` + `steps` [執行結果](result/result_intro_steps.csv)

### 三屬性

-   `name` + `intro` + `steps` [執行結果](result/result_name_intro_steps.csv)

## 有關報告

-   動機
-   資料來源
-   方法
-   結果
-   討論
