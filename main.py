from functools import cmp_to_key

def compare(str1, str2):
    return int(str2 + str1) - int(str1 + str2)
def highestPosNum(arr):
    sortArray = sorted(map(str, arr), key=cmp_to_key(compare))
    result = "".join(sortArray)
    return result

array = list(map(int, input().split()))
result = highestPosNum(array)
print(result)
