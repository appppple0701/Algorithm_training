#sort(Data) = merge(sort(Left), sort(Right))

#負責拆分
def merge_sort(data):
    #判斷是否還需要再拆
    if len(data) <= 1:
        return data
    else:
        #算出拆分的中間點
        mid = len(data) // 2
        #依照中間點把原數列拆分成兩分
        left = merge_sort(data[:mid])
        right = merge_sort(data[mid:])
        return merge(left, right)
        
#負責合併已經排列好的子陣列
def merge(left, right):
    #收到left和right後，要把它們合併成一個排序好的新陣列
    result = []
    #利用指標判斷是否排序完成， i for left, j for right
    i = 0
    j = 0

    #只要其中一個指標走到底，就停止
    while (i <len(left) and j < len(right)):
        #判斷大小
        if left[i] <= right[j]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    
    #反正會剩下: 排好的其中一邊(指標走到底了 沒有東西可以加上去) and 指標還沒走到底的一邊(反正已經排好了 直接貼上取也會對)
    result += left[i:] + right[j:]
    # print(result)
    return result

data = [1,5,3,4,2,6]
print(merge_sort(data))