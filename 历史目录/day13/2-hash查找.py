# @Author : 杨佳杰
# @Time   : 2022/6/13 14:06
# @File   : 2-hash查找.py
MAXKEY=1000

def elf_hash(hash_str:str):
    h = 0
    g = 0
    for i in hash_str:
        h = (h << 4) + ord(i)
    g = h & 0xf0000000
    if g:
        h ^= g >> 24
    h &= ~g
    return h % MAXKEY


def use_hash():
    str_list = ["xiongda", "lele", "hanmeimei", "wangdao", "fenghua"]
    hash_table = [None] * MAXKEY
    for i in str_list:
        print(elf_hash(i))
        hash_table[elf_hash(i)] =i


use_hash()

