# @Author : 杨佳杰
# @Time   : 2022/6/7 14:44
# @File   : 4-封装案例.py
class HouseItem():
    def __init__(self,name,area):
        self.name=name
        self.area=area


    def __str__(self):
        return f'家具{self.name}占地面积为{self.area}'

class House():
    def __init__(self, house_type, area):
        self.house_type = house_type
        self.area = area
        self.free_area = area
        self.item_list = []

    def __str__(self):
        return f'户型为{self.house_type},总面积为{self.area},剩余面积{self.free_area},包含家具{self.item_list}'

    def add_item(self, item: HouseItem):
        if self.free_area < item.area:
            print(f'房间剩余面积不够,无法添加{item.name}')
            return
        self.free_area-=item.area
        self.item_list.append(item.name)
        print(f'家具{item.name}添加成功')


house=House('别墅',6)
print(house)
bed=HouseItem('席梦思',4)
print(bed)
chest=HouseItem('衣柜',2)
print(chest)
table=HouseItem('餐桌',1.5)
print(table)
print('-'*50)
house.add_item(bed)
print(house)
house.add_item(chest)
print(house)
house.add_item(table)
print(house)

