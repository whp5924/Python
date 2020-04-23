import matplotlib.pyplot as plt
import numpy as np

values = [0.09,-0.05,0.20,-0.02,0.08,0.09,0.03,0.027]
x = np.linspace(0,2*np.pi,9)[:-1]
c = np.random.random(size=(8,3))
fig = plt.figure()
plt.axes(polar=True)
#获取当前的axes
print(plt.gca())
#绘图
plt.bar(x,values,width=0.5,color=c,align='center')
plt.scatter(x,values,marker='o',c='black')
#添加文本
plt.figtext(0.03,0.7,s='陆地面积增长指数',fontproperties='KaiTi',fontsize=22,rotation='vertical',verticalalignment='center',horizontalalignment='center')

plt.ylim(-0.05, 0.25)

labels = np.array(['省1','省2','省3','省4','省5','省6','省7','研究区'])
dataLength = 8
angles = np.linspace(0, 2*np.pi, dataLength, endpoint=False)
plt.thetagrids(angles * 180/np.pi, labels,fontproperties='KaiTi',fontsize=18)

#添加注释
# plt.annotate(s='省',xy=(0,0.09),xytext=(0,0.28),fontproperties='KaiTi',fontsize=18)
# plt.annotate(s='省',xy=(0,-0.05),xytext=(np.pi/4,0.28),fontproperties='KaiTi',fontsize=18)
# plt.annotate(s='省',xy=(0,0.20),xytext=(np.pi/2,0.28),fontproperties='KaiTi',fontsize=18)
# plt.annotate(s='省',xy=(0,-0.02),xytext=(3*np.pi/4,0.33),fontproperties='KaiTi',fontsize=18)
# plt.annotate(s='省',xy=(0,0.08),xytext=(np.pi,0.38),fontproperties='KaiTi',fontsize=18)
# plt.annotate(s='省',xy=(0,0.09),xytext=(np.pi*5/4,0.35),fontproperties='KaiTi',fontsize=18)
# plt.annotate(s='前江省',xy=(0,0.03),xytext=(np.pi*3/2,0.30),fontproperties='KaiTi',fontsize=18)
# plt.annotate(s='研究区',xy=(0,0.027),xytext=(np.pi*7/4,0.28),fontproperties='KaiTi',fontsize=18)
#设置网格线样式
plt.grid(c='gray',linestyle='--',)


# y1 = [-0.05,0.0,0.05,0.10,0.15,0.20,0.25]
# lai=fig.add_axes([0.12,0.01,0.8,0.98])
# lai.patch.set_alpha(0.25)
# lai.set_ylim(-0.05, 0.25)
#显示

plt.show()