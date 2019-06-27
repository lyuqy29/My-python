#coding=utf8
# test 1
# 随机数字 -10 - 10 数量: 10
from random import randint

data = [randint(-10,10) for _ in xrange(10) ]

#print filter(lambda x: x>= 0 , data)
#打印出大于0的数字
print  [x for x in data if x >= 0]

# test 2

#字典解析
d = {x: randint(60, 100) for x in xrange(1,21)}

print {k:v for k,v in d.iteritems() if v >90}

