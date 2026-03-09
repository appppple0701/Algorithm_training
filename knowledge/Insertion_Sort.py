'''
插入排序法 : 從元素i(key)開始，和左邊的元素做比較，只要比key大的元素就往右搬一格，直到找到比 key 小的元素或到達陣列開頭，並最後插入key。

worst case O(n^2) : [n, n-1, ..., 3, 2, 1]; average case O(n^2); best case O(n) : [1, 2, 3, ..., n-1, n]
'''
#插入排序法
def insertion_sort(data):
    #遍歷陣列
    for i in range(1, len(data)):
        #每次抓第i個元素(key)，並和key之前的元素比較，不停向左放，直到出現比key小的元素或結束
        key = data[i]
        #key的前一個元素索引
        j = i - 1

        #比較直到出現比key小的元素或結束
        while ( j >= 0 and data[j] > key):
            #只要比key大的元素就通通往前搬一格
            data[j+1] = data[j]
            j -= 1

        #迴圈結束時j - 1，因此j + 1才是正確插入位置
        data[j+1] = key
            
    return data

data = [10,9,8,7,6,5,4,3,2,1]
print(insertion_sort(data))