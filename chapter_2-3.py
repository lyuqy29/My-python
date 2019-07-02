#coding=utf8
from random import randint
from collections import  Counter
import re
#test 1
data = [randint(0,20) for _ in xrange(30)]

c = dict.fromkeys(data,0)

for x in data:
    c[x] += 1
print c

#test 2
#统计出现的频率
c2 = Counter(data)
print c2.most_common(3)


txt = open('ssh_config').read()

c3 = Counter(re.split('\W+',txt))

print c3.most_common(3)