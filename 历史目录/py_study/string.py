str1='hello,wolrdhello'
'''字符串等同于只含有字符的列表,同样可以用[]来读取其中某一个字符'''
print(str1[2])#l
print(str1)

'''字符串的查询操作.可查询一个字符或者一段子串,返回的是子串的第一个字符所在下标'''
#利用index()函数查询第一次出现,与rindex()函数查询最后一次出现
print(str1.index('ll'))#2
print(str1.rindex('ll'))#13
'''若所查询的子串不存在,则会抛出异常'''
#利用find()函数查询第一次出现,rfind函数查询最后一次出现
print(str1.find('ll'))#2
print(str1.rfind('ll'))#13
print(str1.find('lw'))#-1
print(str1.rfind('lw'))#-1
'''若查询的子串不存在,则会返回-1'''

'''字符串的大小写转换,原来的字符串不变,会产生一个新的字符串'''
#upper()函数,将所有的小写字母转换为大写字母
str2='Hello,python'
a=str2.upper()#'HELLO,PYTHON'
print(a,str2)
#lower()函数,将所有的大写字母转换为小写字母
b=a.lower()#'hello,python'
print(b,a)
#swapcase()函数将字符串中的小写转大写,大写转小写
c=str2.swapcase()#'hELLO,PYTHON'
print(c,str2)
#captialize()函数将字符串中的第一个字符转为大写,其他转为小写
d=c.capitalize()#'Hello,python'
print(d,c)
#title()函数将字符串中的每个单词的首字母变为大写,其他变为小写
str3='hello,I am jacky,do you want to be my girl friend?'
e=str3.title()
print(e)

'''字符串的对齐操作'''
#center()函数实现居中对齐
#第一个参数控制格式化长度,第二个参数控制填充字符,默认为空格
#若第一个格式化参数小于原字符串长度,则输出原字符串
str4='hello,wolrd!'
print(str4.center(20,'_'))
print(str4.center(10))
#同理还有ljust()左对齐函数,rjust()右对齐函数,函数参数同上
print(str4.ljust(20,'_'))
print(str4.ljust(10))
print(str4.rjust(20,'_'))
print(str4.rjust(10))
#zfill()函数实现右对齐,不同于rjust()函数的是,其填充单位默认为0,不可修改
t='100010111100'
print(t.zfill(16))
print(t.zfill(10))

'''字符串的分割,将一个字符串分割为多部分,并以list存储'''
#split(sep='char',maxsplit=num)
#char指定分隔符,maxsplit指定分割次数,若不指定则默认char为空格,maxsplit无上限
str5='hello python hello'
lst1=str5.split()
print(lst1)
lst2=str5.split(sep=' ',maxsplit=1)
print(lst2)
str6='hello_python_hello'
print(str6.split())
print(str6.split(sep='_'))
print(str6.split(sep='_',maxsplit=1))
#rsplit()从后往前分割字符串
print(str5.rsplit())
print(str5.rsplit(sep=' ',maxsplit=1))

'''字符串的判断'''
#isidentifier()函数判断字符串是否为合法标识符，即仅有字符数字_组成
print('1.','abc_'.isidentifier())#True
print('2.','abc%'.isidentifier())#False
print('3.','张三_13'.isidentifier())#True
'''中文也视作字符'''
#isspace()判断字符串是否仅有回车，换行，制表符组成
print('4.','\t\n'.isspace())#True
#isalpha()判断字符串是否全为字母
print('5.','abcsdasgd'.isalpha())#True
print('6.','abcs_123'.isalpha())#False
#isdecimal()判断字符串是否全为十进制数
print('7.','12321874683'.isdecimal())#True
print('8.','123四'.isdecimal())#False
print('9.','ⅠⅡⅢⅣ'.isdecimal())#false
#isnumeric()判断字符串是否全为数字
print('10.','12321874683'.isnumeric())#True
print('11.','123四'.isnumeric())#True
print('12.','ⅠⅡⅢⅣ'.isnumeric())#True
#isalnum()判断字符串是否全为字母和数字
print('13.','abc123'.isalnum())#True
print('14.','abc123四'.isalnum())#True
print('15.','abcⅡⅢⅣ'.isalnum())#True

'''字符串的替换,repalce()函数'''
demo1='hello world world world'
print(demo1)
print(demo1.replace('world','python'))
print(demo1.replace('world','python',2))

'''字符串的合并,join()函数将列表以及元祖内的字符串合并为一个新的字符串'''
lst=['hello','world','python']
print(''.join(lst))
print('_'.join(lst))

tuple=('hello','world','python')
print(''.join(tuple))
print('_'.join(tuple))
#join()的对象也可以是字符串,即将字符串的每一个字符看做一个元素
print('_'.join('Python'))

'''字符串的比较
从第一个字符开始对比比较
比较对象ordinal value的大小
可用ord(char)查看
同理也可用chr(ordinal value)转换回字符
'''
s1='apple'
s2='app'
s3='banana'
print(s1>s2)#True
print(s1>s3)#False
print(ord('a'),ord('b'),ord('杨'))#97,98,26472
print(chr(97),chr(98),chr(26472))

'''字符串的切片str[start:stop:step],语法规则同list'''
s4='hello,world woshi python'
s5=s4[:5]
print(s5)
s6=s4[6:]
print(s6)
print(s5+','+s6)

'''字符串的格式化输出'''
name='杨佳杰'
age=22
sign='i am jacky'
grade=398.1381097873
#利用%s,%d,%f来格式化数据
print('我叫%s,年龄%d,成绩是%.1f,签名是:%s'%(name,age,grade,sign))
#利用{}和format()函数来格式化
print('我叫{0},年龄{1},成绩是{2:.1f},签名是:{3}'.format(name,age,grade,sign))
#利用fstring格式化
print(f'我叫{name},年龄{age},成绩是{grade:.1f},签名是:{sign}')
