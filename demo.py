"""
__Title = '下划线变量与命名'
__Author = 'Jinlin'
__Time = '2019/4/20'
"""

# class Student:
#     def __init__(self,name,sex):
#         self._name = name
#         self.sex = sex
#
# stu = Student('Jinlin','Male')
# print(stu.sex)
# print(stu._name)
#
# class Person:
#     def __init__(self,name):
#         self.__name = name
#
#
#
# per = Person('Jinlin')
# print(per._Person__name)
#
# from tabulate import  tabulate
#
# def view(payload):
#     tb_header = payload.keys()
#
#     tb_data = []
#     tb_data.append(payload.keys())
#
#
#     print(tabulate(tb_data,headers=tb_header,tablefmt='psql'))
#
# payload = {1:'a',2:'b',3:'c',4:'d'}
#
# view(payload)

# msgs = {}
#
# class MSG:
#     def __init__(self,pkt):
#         self.id = pkt[0]
#         self.code  = pkt[1]
#
#         if self.id == 0:
#             self.payload = 'AP Message'
#         elif self.id == 1:
#             self.payload = 'AE Message'
#         else:
#             self.payload = None
#
#     def collect_msg(self):
#         if self.id == 0:
#             msgs['AP'] = 'ap-msg'
#         elif self.id == 1:
#             msgs['AE'] = 'ae-msg'
#
# if __name__ == '__main__':
#     pkt = [1,0]
#     msg = MSG(pkt)
#     print(msg)
#     msg.collect_msg()
#     print(msgs)

print('-' * 1000)

s = 'abc'


if not s.endswith('abc'):
    print('s')
else:
    print('a')

isinstance(s)
