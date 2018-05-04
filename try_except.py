print ('start')

try:
    print ('try started')
    a = 10 / 0
    print ('try finished')

except:
    print ('error occured')

print ('end')

"""
[try_execpt無しの場合]

start
try started
Traceback (most recent call last):
  File "try_except.py", line 5, in <module>
    a = 10 / 0
ZeroDivisionError: division by zero


[try_execpt有りの場合]

start
try started
error occured
end
"""
