# a-追加模式打开文件,若文件不存在则创建新文件,文件指针位于文件开头.若文件存在,则文件指针位于文件末尾,在原内容下追加内容
file = open('b.txt', 'a', encoding='utf-8')
file.write('python')
file.close()