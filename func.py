# 使用 while 循环打印 1 3 5 7 9

i = 1
while i <= 9:
    print(i)
    i += 2

# 编写一个函数，查找数字 6 是否在列表 l 里，如果在，输出“found”，如果不在，输出“not found”

l = [1,5,7,8,9]


def fc(l):
    if 6 in l:
        print('found')
    else:
        print('not found')

        
fc(l)
    

# 将字符串 s 拆分成两个字符串 s1、s2，其中 s1 只包含字母，转换为小写，以 [a-z] 排序，s2 只包含数值，升序排序

s = "aAsnr3id2d4b6gs7DZsf9e1AF"

l = list(s)

l.sort()
i = 0
while l[i] <= '9':
    i += 1

l1 = [x.lower() for x in l[i:]]
l1.sort()
l2 = l[:i]

s1 = ''.join(l1)
s2 = ''.join(l2)

print('s1: %s, s2: %s' %(s1, s2))
