"""
Name: Zackery Vering
Project: Lab 3E
Date: 7 Sept 2018
"""

def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1)+fibonacci(n-2)

i = 0
x = 0
y = 1
current = 0
for i in xrange(100):
    current = x + y
    x = y
    y = current
    print(current)

i = 0
while(True):
    for i in xrange(100):
        print(fibonacci(i))
    break