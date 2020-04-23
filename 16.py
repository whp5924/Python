# 创建字符串 string
# 创建空字符串aString='' aString="" aString='''''' aString=""""""
# 创建字符串 aString='wwwwwwwwww'
# 创建空列表 aList=''
# 创建列表 aList=[1,2,3,4]
# 创建空元组 aTuple=()
# 创建元组 aTuple=(1,2,3)
# 创建元组 aTuple=1,2,3
# 创建单元组 aTuple=1, 创建元组是用,分隔
aList=[]
for number in range(1,12): #创建列表
    aList+=[number]
#    print('aList[%d]=' % number,aList)
print('The value of aList is:',aList)
print('Accessing values by iteration:') #通过迭代(遍历）访问值
for item in aList: # in的是列表 可以做循环值
    print(item,end=' ')
print('')
print('Accessubg value by index:') #通过索引访问值
print('Subscript Value')
for i in range(len(aList)):
    print('%8d %7d' % (i,aList[i]))
print('Modifying a list value......') #修改列表值
print('Vaule of aList befor Modifying:',aList)
aList[0]=-100
aList[-2]=12
print('Vaule of aList befor Modifying:',aList)