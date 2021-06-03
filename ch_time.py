import os
while True:
	file = input('File: ')
	if file == '':
		break
	atime = os.stat(file).st_atime
	mtime = os.stat(file).st_mtime
	delta = eval(input('Delta: '))
	atime -= delta
	mtime -= delta
	os.utime(path = file, times = (atime, mtime))
