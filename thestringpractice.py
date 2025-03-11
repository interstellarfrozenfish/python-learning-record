s1 = 72
s2 = 85
r = ((s2 - s1) / s1) * 100
# 格式化
print('小明的成绩提升了： %.1f%%' % r) 
# format()
print('小明的成绩提升了： {0:.1f}%'.format(r)) 
# f-string
print(f'小明的成绩提升了： {r:.1f}%') 