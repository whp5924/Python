# 游戏掷骰子实例
# 一次掷两个骰子,第一次如果掷出两个骰子之和为7和11,则判玩家赢;
# 首次如掷出2、3和12,则判玩家输;
# 首次如果掷出4、5、6、8、9、10和11 系统则判此次掷出的点数和为基准点
# 玩家在次基础上，再次掷，直接出现的点数和为基准点，、
# 在其中，如果掷出的点数和为7,直接判游戏结束
# 同时判玩家输
import random
def collpoint():
    point1=random.randrange(1,7)
    point2=random.randrange(1,7)
    pointsum=point1+point2
    print('掷出的点数和：%d+%d=%d' % (point1,point2,pointsum))
    return pointsum
# 主程序
sum1=collpoint()
if sum1==7 or sum1==11:
   gamestatus='WIN'
elif sum1==2 or sum1==3 or sum1==11:
   gamestatus='LOST'
else:
    gamestatus='continue'
    mypoint=sum1
    print('Point is: %d ' % mypoint)
while gamestatus=='continue':
    sum1=collpoint()
    if sum1==mypoint:
        gamestatus='WIN'
    elif sum1==7:
        gamestatus='LOST'
if gamestatus=='WIN':
    print('Play is WIN.')
else:
    print('Paly is LOST')
print(dir())



