'''
堆積排序由三個部分組成
heapify(堆積化) : 從索引 i 開始，比較父節點與左右子節點的大小。若父節點非最大值，則與最大者交換位置，並遞迴向下修正。關鍵在於 heap_size 參數，它定義了操作的邊界，防止程式更動到陣列後端已排序好的部分。
build_heap(建立堆積) : 僅在排序開始前執行 1 次。邏輯是從最後一個非葉子節點（索引 $heap\_size // 2 - 1$）倒序處理至根節點（索引 0），確保整棵樹在初始狀態下均符合父節點大於子節點的規則。
heap_sort(堆積排序) : 
    呼叫 build_max_heap 建立初始堆積。
    利用迴圈將根節點（當前最大值 data[0]）與目前堆積末尾元素交換。
    縮減 heap_size（界定已排序區），並針對根節點重新執行 max_heapify 以找回剩餘元素中的最大值。重複此過程直到所有元素皆離開堆積。
'''

#從第i個節點檢查並堆積
def max_heapify(data, i, heap_size):
    l = 2 * i + 1     #左子節點
    r = 2 * i + 2     #右子節點
    #heap_size = len(data)
    largest = i     #先假設最大的為 i

    #進行比較與邊界判斷
    if l < heap_size and data[l] > data[largest]:
        largest = l
    if r < heap_size and data[r] > data[largest]:
        largest = r
    
    #判斷是否需要交換
    if largest != i:
        data[i], data[largest] = data[largest], data[i]
        #從i - 1遞迴
        max_heapify(data, largest, heap_size)    
    
    return data

#建立堆積
def build_max_heap(data, heap_size):
    #heap_size = len(data)
    for i in range(heap_size//2 -1, -1, -1):
        max_heapify(data, i, heap_size)
    return data

#堆積排序
def max_heap_sort(data):
    heap_size = len(data)
    build_max_heap(data, heap_size)
    for i in range(len(data) - 1, 0, -1):
        data[0], data[i] = data[i], data[0]
        heap_size -= 1
        max_heapify(data, 0, heap_size)
    return data

data = [3, -1, 0, -5, 2]
print(max_heap_sort(data))