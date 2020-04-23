# 向函数传递列表
class PrivateClass:
    """Class that contains public and private data"""
    def __init__(self):
        """Private the class"""
        self.publicdata="public"
        self.__privatedata="private"

