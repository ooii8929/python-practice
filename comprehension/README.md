# Comprehension

## Knowledge
一行程式碼即可完成多行的任務，提高開發效率和代碼可讀性。

	•	運用在任何可疊代的物件(Iterable Object)
	•	三種重要物件

### List Comprehension
```
[expression for item in iterable]
```
or
```
# 條件判斷擺在後面來篩選可疊代的物件(Iterable Object)元素
[expression for item in iterable (if condition)]
```
or
```
# 要依據條件來"改變"串列(List)中的值時，則要把條件判斷移至前方
[expression (if condition else) for item in iterable]
```
#### 比較：List Comprehension 與 map & filter
```
# map
map(function, iterable, ...)
```
or
```
# filter
filter(function, iterable)
```
-   Set & Dictionary Comprehension
-   Generator Expression

## Example

假設我們有一系列的事件 (events)，每個事件包含不同的服務 (services) 及其對應的規模 (size)。我們希望通過 comprehension 來提高查找和處理這些數據的效率

## Reference
https://www.learncodewithmike.com/2020/01/python-comprehension.html