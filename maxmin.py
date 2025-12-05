def getmaxmin(array):
    array.sort()
    ans = []
    ans.append(array[0])
    ans.append(array[-1])

    return ans


print(getmaxmin([-200, 4, 7, 200, -400]))
