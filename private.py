# 定义私有属性 私有方法
# Fig. 7.11: private.py
# Class with private data members
class privateclass:
    "Class that contains public and private data" # 文档化字符串
    def __init__(self):
        "Private class,Contains publice and private data member" # 文档化字符串
        self.publicdata="public"
        self.__privatedata="private"

