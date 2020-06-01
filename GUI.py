from __future__ import print_function
import time
print()
print()
print()
print()
print()
print()
print()
print('---------------------GESTURE KEYBOARD----------------------')
f=open("test.txt", "r")
while(1):
	cont = f.read()
	print(cont, sep=' ', end='')
	time.sleep(0.5)