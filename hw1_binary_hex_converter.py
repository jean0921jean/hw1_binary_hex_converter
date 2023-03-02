#!/usr/bin/env python
# coding: utf-8

# In[21]:


#十進位轉換成二進位
#宣告變數

a = 2**7
b = 2**6
c = 2**5
d = 2**4
e = 2**3
f = 2**2
g = 2**1
h = 2**0

#初始化變數
d1 = d2 = d3 = d4 = d5 = d6 = d7 = d8 = 0

number = int(input("請輸入0~255間的任一數字"))
if number >= a:
    d1 = 1
else:
    d1 = 0
    
if number - a >= b:
    d2 = 1
else:
    d2 = 0
    
if number - a - b >= c:
    d3 = 1
else:
    d3 = 0

if number - a - b - c >= d:
    d4 = 1
else:
    d4 = 0
    
if number - a - b - c - d >= e:
    d5 = 1
else:
    d5 = 0

if number - a - b - c - d - e >= f:
    d6 = 1
else:
    d6 = 0
    
if number - a - b - c - d - e - f >= g:
    d7 = 1
else:
    d7 = 0

if number - a - b - c - d - e - f - g >= h:
    d8 = 1
else:
    d8 = 0

#答案1
answer1 = [str(d1), str(d2), str(d3), str(d4), str(d5), str(d6), str(d7), str(d8)]
print(' '.join(answer1))

#十進位轉換成十六進位

#先定義十六進位的數字
hexa_digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'A', 'B', 'C', 'D', 'E', 'F']
hexa1 = d1 * 2**3 + d2 * 2**2 + d3 * 2**1 + d4 * 2**0
hexa2 = d5 * 2**3 + d6 * 2**2 + d7 * 2**1 + d8 * 2**0

hexa_str = [str(hexa_digits[hexa1]), str(hexa_digits[hexa2])]
print(' '.join(hexa_str))


# In[ ]:





# In[ ]:




