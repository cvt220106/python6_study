# @Author : 杨佳杰
# @Time   : 2022/6/23 10:00
# @File   : 3-使用property属性实例化paper对象.py
class Page:
    def __init__(self,current_page):
        self.current_page=current_page
        self.per_items=10

    @property
    def start(self):
        return (self.current_page-1)*self.per_items

    @property
    def end(self):
        return self.current_page*self.per_items


p=Page(1)
print(p.start)
print(p.end)
