# import sys
# bmodule=sys.builtin_module_names
# print(bmodule)
#
# ('_abc', '_ast', '_bisect', '_blake2', '_codecs',
#  '_codecs_cn', '_codecs_hk', '_codecs_iso2022',
#  '_codecs_jp', '_codecs_kr', '_codecs_tw', '_collections',
#  '_contextvars', '_csv', '_datetime', '_functools', '_heapq',
#  '_imp', '_io', '_json', '_locale', '_lsprof', '_md5', '_multibytecodec',
#  '_opcode', '_operator', '_pickle', '_random', '_sha1', '_sha2', '_sha3',
#  '_signal', '_sre', '_stat', '_statistics', '_string', '_struct', '_symtable',
#  '_thread', '_tokenize', '_tracemalloc', '_typing', '_warnings', '_weakref',
#  '_winapi', '_xxinterpchannels', '_xxsubinterpreters', 'array', 'atexit',
#  'audioop', 'binascii', 'builtins', 'cmath', 'errno', 'faulthandler',
#  'gc', 'itertools', 'marshal', 'math', 'mmap', 'msvcrt', 'nt', 'sys',
#  'time', 'winreg', 'xxsubtype', 'zlib')

import myModule
import calculator
import show_info
import show_info as si

si.show_name()

myModule.func1()
myModule.func2()
myModule.func3()

print(calculator.add(2, 4.5))
show_info.show_name()

from show_info import show_phone as sp
sp()

