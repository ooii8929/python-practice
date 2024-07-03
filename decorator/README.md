# Decorator

## Knowledge
Python 的 Syntax Candy

- 本質上是一個 Python 函式或類 ( class )，它可以讓其他函式或類，在不需要做任何代碼修改的前提下增加額外功能，裝飾器的返回值也是一個函式或類對象
- 使用「@」當做裝飾器使用的語法糖符號
- 在 Python 中，多層 decorators 是以「遞歸（recursive）」的方式來處理的。如果一個函數有兩個或以上的 decorators，邏輯上會先將「最靠近」的 decorator 應用於函數，產生一個新的函數，然後再由上一層的 decorator 處理這個新的函數。這樣的過程會一直遞歸進行，直到所有的 decorators 都被應用為止。

## Example
Simulate how to use decorators to reduce code duplication and enhance flexibility, using a built-in decorator and a custom log_decorator to improve the DB model as example.

