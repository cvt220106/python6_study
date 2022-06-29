# w模式-即写函数模式,若文件不存在,则创建文件.每次写都从文件的开头重写,即这一次的write会将上一次的write所覆盖
file = open('b.txt', 'w', encoding='utf-8')
file.write('hello  world')
file.close()
