# @Author : 杨佳杰
# @Time   : 2022/6/21 22:59
# @File   : work9.py
import re

url_list = ['http://www.interoem.com/messageinfo.asp?id=35`',
            'http://3995503.com/class/class09/news_show.asp?id=14',
            'http://lib.wzmc.edu.cn/news/onews.asp?id=769',
            'http://www.zy-ls.com/alfx.asp?newsid=377&id=6',
            'http://www.fincm.com/newslist.asp?id=415',
            ]

for item in url_list:
    url=re.match(r"[^/]+//([^/]*)",item)
    print(url.group(1))