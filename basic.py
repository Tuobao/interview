# 问题一：字符串排序

s = "hello world"

# 请编写代码，将 s 以 [a-z] 顺序输出

'''法1

l = list(s)
l.sort()
s2 = ''.join(l)
print(s2)

'''
l = list(s)


# 快排
def kp(arr):
    def foo(begin, end):
        if begin > end:
            return
        low, high = begin, end
        mid = arr[begin]

        while low < high:
            while low < high and arr[high] > mid:
                high -= 1
            while low < high and arr[low] <= mid:
                low += 1
            arr[low], arr[high] = arr[high], arr[low]
        arr[low], arr[begin] = arr[begin], arr[low]
        foo(begin, low-1)
        foo(high+1, end)
    foo(0, len(arr)-1)


kp(l)
print(''.join(l))

# 问题二：数值比较

n = [9,15,23,89,33,26,2,76]

# 请编写代码，找出数组中的最大数与最小数


max_n = max(n)
min_n = min(n)
print('最大数为：%d ,最小数为：%d' %(max_n, min_n))

# 或者先通过排序，然后拿出第一个和最后一个元素



# 问题三：替换

a = "i,am,a,student,in,chengdu"

# 请编写代码，将 “student” 和 “chengdu” 变为可基于参数输入配置的输出
# 通过参数输入打印出完整的句子

def fc(role='student', add='chengdu'):
    print('i,am,a,%s,in,%s' %(role, add))

fc()
