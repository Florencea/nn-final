# nn-final

## 流程

-   合併原始資料表、去除空資料(沒有`name` or 沒有`intro` or 沒有`steps`)、分離未分類食譜
    -   `python3 receipe_combiner.py`
    -   資料欄位欄位空缺食譜： 5914 筆
    -   已分類食譜： 37629 筆(`receipe_categoried.json`)
    -   未分類食譜： 1348 筆(`receipe_uncategoried.json`)
-   清理資料
-   製作標記訓練資料

## 訓練模式

### 單屬性

-   `name`
-   `intro`
-   `steps`

### 兩屬性

-   `name` + `intro`
-   `name` + `steps`
-   `intro` + `steps`

### 三屬性

-   `name` + `intro` + `steps`

## 有關開發筆記

-   使用python版本的fasttext(v0.8.3)

    -   `pip3 install Cython fasttext`

## 有關報告

-   動機
-   資料來源
-   方法
-   結果
-   討論
