# Context Manager

## Knowledge
資源的管理，例如管理開啟的檔案、網路 socket 與各種鎖定（locks）。

- For 確保開啟的資源在使用完之後，有確實被關閉（或釋放）。（如果忘記關閉這些資源，就會造成程式執行上的效能問題，甚至出現錯誤）
- 除了關閉之外，有些特殊的資源在使用完畢之後，還必須進行一些後續的清理動作
- 自行建立 context manager，只要定義好類別的 __enter__ 與 __exit__ 兩個方法函數即可，with 在剛開始執行時，會執行 __enter__ 這個函數，傳回配給的資源（例如開啟的檔案），而在 with 範圍結束時，會自動呼叫 __exit__ 釋放資源（例如關閉檔案）

## Example

Simulate how to use a custom context manager to manage a database connection.

## Reference
https://blog.gtwang.org/programming/python-with-context-manager-tutorial/
https://urbandfish.com/what-is-context-manager/
