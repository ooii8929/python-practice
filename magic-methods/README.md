# Magic Methods

## Knowledge
不需要去重新定義或架構一個方法，直接使用即可

- 有一個 list = [a,b,c]，想知道它的長度，可以直接使用len(list)=3，這是因為type(list)是list，list這個物件的class裡面已經有定義 __len__
- 使用 dir(int) 查看 magic methods

## Example
Simulate how to customize magic methods to meet specific needs, using event duration comparison as an example.

