# b-以二进制方式打开非文本文件,与其他模式共用,即rb,wb吗
src_file = open('v-11.jpg', 'rb')
target_file = open('copy.jpg', 'wb')

target_file.write(src_file.read())

src_file.close()
target_file.close()

