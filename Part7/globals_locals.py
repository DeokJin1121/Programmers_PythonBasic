# global scope variables <> local scope variables
def add(a, b):
    return a + b

a = 1
b = 2
c = 3
add(4, 5)

'''
global : 이것은 거실같은 느낌(거실)
local : 이것은 내방같은 느낌(내방)

내 방에 없는 것을 거실에서 찾아서 사용 O
거실에 없는 것을 방에서 찾아서 사용 X
'''