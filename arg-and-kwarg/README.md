# Args and Kwargs

## Knowledge
當需要傳遞不固定數量的參數時，可以使用 *args 和 **kwargs。

	•	*args：傳入的多個參數將以 tuple 儲存，是可變的 positional arguments。
	•	**kwargs：傳入的多個參數將以 dict 儲存，是可變的 keyword arguments 列表。
	•	在使用時，*args 必須位於 **kwargs 之前，因為 positional arguments 有位置順序的對應，必須位於 keyword arguments 之前。

## Example

我們假設程式開發中需要針對事件 (event) 進行操作，因此設計了一個 Event 類別。這個事件會有不同的元資料 (meta data)，包含類型 (types) 及其他不確定的值。我希望在利用 Event 類別建立物件時，可以顯示它的資料。
