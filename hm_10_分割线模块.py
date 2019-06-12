# def print_line2(char,times):
#     print(char * times)
# # print_line2("$",23)
#
# def print_line3(char,times):
#     col = 1
#     while col <= 2:
#         print_line2(char,times)
#         col += 1
# name = "黑马程序员"
#
# print("&" * 56)
# a = 7
# b = 2
# c = a**b
# print(c)
# import keyword
# print(keyword.kwlist)
# import random
# row = 1
#
# while row <= 5:
#
#     print("*" * row)
#
#     row += 1
# row = 1
#
# while row <= 5:
#
#     # 假设 python 没有提供字符串 * 操作
#     # 在循环内部，再增加一个循环，实现每一行的 星星 打印
#     col = 1
#
#     while col <= row:
#         print("*",end='')
#
#         col += 1
#
#     # 每一行星号输出完成后，再增加一个换行
#     print("")
#
#     row += 1
# s = 12.12
# w = int(s)
# w = 23

# def test(sum):
#     print("-" * 78)
#     print("%d 在函数中的地址是 %x" % (sum,id(sum)))
#     result = 100
#     print("#" * 20)
#     print("返回值%d 在内存中的的地址是 %x" % (result,id(result)))
#     return result
#
# a = 10
# print("函数调用之前 内存地址是 %x" % id(a))
#
# r = test(a)

# print("调用函数后。实参内存是 %x" % id(a))
# print("调用函数后。返回值内存地址是%x" % id(r))
# print(id(test()))
# print(id(10))
# a = 123
# b = 234
# name_list = ["a",1,"b",2,"c",3]
# name_list1 = [11,22,33,44,55,a,b]
# print(name_list[3])
# print(name_list1)
# name_list.insert(3,333)
# print(name_list)
# name_list.append("www.com")
# print(name_list)
# c = []
# c.extend(name_list1)
# print(c)
# name_list[3] = 23
# print(name_list)
# del name_list[3]
# print(name_list)
# name_list.remove(1)
# print(name_list)
# name_list.pop()
# print(name_list)
# name_list.pop(1)
# print(name_list)
# print(name_list)
# name_list.clear()
# print(name_list)
#
# print(len(name_list1))
#
# name_list1.sort()
# print(name_list1)
# name_list1.reverse()
# print(name_list1)
# name_list.reverse()
# print(name_list)
# name_list1.sort(reverse=True)
# print(name_list1)
# for name in name_list:
#    print(name)
# info_tuple = (50,)
# info = ("zhangsan", 18)
#
# print("%s 的年龄是 %d" % info)

# xiaoming = {"name":'xiaoming',
#             "age":78,
#             "gender":True,
#             "height":1.78,
#             "weight":80}
#
# for k in xiaoming:
#     print("%s: %s" % (k, xiaoming[k]))
# card_list = [{"name": "张三",
#               "qq": "12345",
#               "phone": "110"},
#              {"name": "李四",
#               "qq": "54321",
#               "phone": "10086"}
#              ]
# for j in card_list:
#     print(j)

# string = 'hello python nihao'
# string1 = 'strhello PYTHON'
# string2 = 'HELLO PYTHON'
# # for c in string:
# #     print(c)
# # print(string.isspace())
# # print(string.islower())
# # print(string2.isupper())
# string.find(str, start=0, end=len(string))
# print(string1.startswith(str))
# string.replace(old_st, new_str, num=string.count(old))

# print(num_str)num_str = "0123456789"
# print(num_str[2:6])
# print(num_str[2:])
# print(num_str[:6])
# print(num_str[:])
# print(num_str)
# print(num_str[::4])
# print(num_str[1::2])
# print(num_str[-1])
# print(num_str[2:-1])
# print(num_str[-3:])
# #print(num_str[::-1])
# print(num_str[-1:-7:-2])
# print(num_str[::])
# print(len(num_str))
# print(max(num_str))
# print(min(num_str))
# del(num_str)
# print(num_str)
# def nums():
#     d1 = 45
#     d2 = 46
#     d3 = 126
#     d4 = 23
#     return d1,d2,d3,d4
#
# a1,a2,a3,a4 = nums()
# # print(ad)
# print(a1)
# print(a3)




#  Redis 数据库操作


# from redis import *
#
# #
# if __name__ == '__main__':
#     try:
#         sr = StrictRedis()
#         # result = sr.set('name','ttttt')
#         # result1 = sr.get('name')
#         # result2 = sr.set('name','asdfasdsa')
#         # print(result)
#         # print(result1)
#         # print(result2)
#         # result3 = sr.get('name')
#         # print(result3)
#         # result4 = sr.delete('name')
#         # print(result4)
#         # result5 = sr.get('name')
#         # print(result5)
#         # result6 = sr.keys()
#         # print(result6)
#         # sr.delete('a2')
#         # print(sr.keys())
#         # sr.delete('a4','a1','a5','c1','a3','key')
#         # print(sr.keys())
#         # result7 = sr.hmset('a1','name')
#         # print(result7)
#         # result1 = sr.hkeys('name')
#         # print(result1)
#     except Exception as e:
#         print(e)

def demo(num,num_list):

    print("函数内部")
    print(num)
    print(id(num))
    print(num_list)
    print(id(num_list))

    num_list.pop()
    print(num_list)
    print(id(num_list))

    num = 12
    num_list = [1,2,3]
    print(num)
    print(id(num))
    print(num_list)
    print(id(num_list))
    num_list.pop()
    print("函数代码完成")


gl_num = 123
print(id(gl_num))
gl_num_list = [11,22,33]
print(id(gl_num_list))

demo(gl_num,gl_num_list)

print(gl_num)
print(id(gl_num))
print(gl_num_list)
print(id(gl_num_list))

# def demo(num, num_list):
#     print(num)
#     print(num_list)
#
#     print("函数内部")
#
#     # 赋值语句
#     num = 200
#     num_list = [1, 2, 3]
#
#     print(num)
#     print(num_list)
#
#     print("函数代码完成")
#
#
# gl_num = 999
# gl_list = [44, 55, 66]
# demo(gl_num, gl_list)
# print(gl_num)
# print(gl_list)

# def mutanle(num_list):
#     num_list.extend([111,222,333])
#     print(num_list)
#
# gl_list = [1,2,3]
# print(gl_list)
# mutanle(gl_list)
# print(gl_list)