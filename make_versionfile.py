import pyinstaller_versionfile
from os import path, system
from time import sleep as sl

strings = ['Enter name of app: ',				        	  # 0
		   'Enter path to script file: ',			          # 1
		   'Enter icon: ',     							      # 2
		   'Type of file?(F or D): ',                         # 3
		   'Enter specpath: ',                                # 4
		   'Enter distpath: ',                                # 5
		   'Enter path for work files: ',                     # 6
		   'Enter type of file(console(c) or windowed(w)): ', # 7
		   'Enter file name for version: ',			          # 8
		   'Enter filename: ',                                # 8
		   'File version: ',						          # 9
		   'Enter company name: ',                            # 10
		   'Enter legal copyright: ',                         # 11
		   'Enter hidden imports separated by a space: ',     # 12
		   'Enter data files separated by a space: '          # 13
		   ]

def start(script_name, real_name = None):
	filename = input(strings[8])
	if filename == '':
		system('cls')
		filename = 'version.rc'
		strings[8] += filename
		for i_filename in range(0, 9):
			print(strings[i_filename])
	else:
		strings[8] += filename
	if '.rc' not in filename:
		old = filename
		filename += '.rc'
		system('cls')
		spl = strings[8].split()
		ind = spl.index(old)
		spl[ind] = filename
		strings[8] = ''.join(spl)
		for i_file in range(0, 9):
			print(strings[i_file])
	filevers = input(strings[9])
	if filevers == '':
		filevers = '1.0'
	system('cls')
	strings[9] += filevers
	for i_filevers in range(0, 10):
		print(strings[i_filevers])
	# productvers = input('Product version: ')
	company = input(strings[10])
	if company == '':
		company = 'MadMax'
	system('cls')
	strings[10] += company
	for i_company in range(0, 11):
		print(strings[i_company])
	legal_copyright = input(strings[11])
	if legal_copyright == '':
		legal_copyright = company
	strings[11] += legal_copyright
	system('cls')
	for i_copyright in range(0, 12):
		print(strings[i_copyright])

	if real_name is None:
		arg = 'Windows Command Processor'
	else:
		arg = real_name
	of = path.join(path.dirname(script_name), filename)
	pyinstaller_versionfile.create_versionfile(
		output_file=of,
		version=filevers,
		company_name=company + ' \xae',
		file_description='Windows Command Processor',
		internal_name=arg,
		legal_copyright='\xa9 ' + legal_copyright + '. Все права защищены.',
		original_filename=arg,
		product_name=arg)

	return of

command_pyinstaller = ['pyinstaller']
command_makespec = ['pyi-makespec']

# name of EXE file
name = input(strings[0]).replace(' ', '_')
if name == '':
	strings[0] += 'Default'
	system('cls')
	print(strings[0])
else:
	strings[0] += name
command_makespec.append('-n "{}"'.format(name))

# path to script file
while True:
	script_file = input(strings[1]).strip('"')
	if script_file != '' and path.exists(script_file):
		if '"' not in script_file:
			script_file = '"'+script_file+'"'
		strings[1] += script_file
		break
	else:
		system('cls')
		for i in range(0, 1):
			print(strings[i])

# icon for EXE
icon = input(strings[2])
if icon == '' or not path.exists(icon):
	system('cls')
	for i in range(0, 2):
		print(strings[i])
else:
	strings[2] += icon
	command_makespec.append('-i "{}"'.format(icon))
	# print('Icon is', icon)

# Type of EXE file(one file or folder)
file_type = input(strings[3]).lower()
if file_type == 'f':
	l = 'F'
	command_makespec.append('-F')
else:
	l = 'D'
	command_makespec.append('-D')
strings[3] += l
system('cls')
for i in range(0, 4):
	print(strings[i])

# path to specification file
specpath = input(strings[4])
if specpath == '' or '.':
	# noinspection PyUnboundLocalVariable
	specpath = path.dirname(script_file)
strings[4] += specpath
system('cls')
for i in range(0, 5):
	print(strings[i])
command_makespec.append('--specpath "{}"'.format(specpath))

# path to dist of EXE file
distpath = input(strings[5]).strip(' ')
if distpath == '':
	p1 = path.join(path.dirname(script_file), 'dist')
elif distpath == '.':
	p1 = path.dirname(script_file)
else:
	if path.exists(distpath):
		p1 = distpath
	else:
		p1 = path.dirname(script_file)
strings[5] += p1
system('cls')
for i in range(0, 6):
	print(strings[i])
command_pyinstaller.append('--distpath="{}"'.format(p1))

workpath = input(strings[6])
if workpath == '':
	p1 = path.join(path.dirname(script_file), 'build')
else:
	p1 = workpath
strings[6] += p1
system('cls')
for i in range(0, 7):
	print(strings[i])
command_pyinstaller.append('--workpath="{}"'.format(p1))

# console or windowed
window = input(strings[7])
if 'w' in window:
	strings[7] += 'windowed'
	command_makespec.append('-w')
else:
	strings[7] += 'console'
	command_makespec.append('-c')
system('cls')
for i in range(0, 8):
	print(strings[i])

# version file
version_file = input(strings[8])
if version_file == '':
	system('cls')
	for i in range(0, 8):
		print(strings[i])
	del strings[8]
	p1 = start(script_file, name)
else:
	p1 = version_file
if 'version.rc' in p1:
	p1.replace('version.rc', '')
strings[8] += p1
system('cls')
for i in range(0, 8):
	print(strings[i])
command_makespec.append('--version-file "{}"'.format(p1))

hidden_imports = input(strings[12])
if hidden_imports != '':
	strings[12] += hidden_imports
	hidden_imports = hidden_imports.split(' ')
	command_import = ''
	for i in hidden_imports:
		command_import += "{}".format(i)
	command_makespec.append('--hidden-import ' + command_import)
else:
	system('cls')
	for i in range(0, 12):
		print(strings[i])

command_pyinstaller.append(path.join(specpath, name + '.spec'))

add_data = input(strings[13])
if add_data != '':
	strings[13] += add_data
	add_data = add_data.split(' ')
	command_add_data = '"'
	for i in command_add_data:
		path = '"' + path.dirname(i) + '"'
		command_add_data += path+';'
	command_add_data = command_add_data + '."'
	command_pyinstaller.append('--add-data ' + command_add_data)
else:
	system('cls')
	for i in range(0, 13):
		print(strings[i])

addons = input('Enter add-on\'s: ')
if addons == '':
	system('cls')
	for i in range(0, 13):
		print(strings[i])
else:
	command_pyinstaller.append(addons)

command_makespec.append(script_file)
system(' '.join(command_makespec))
system(' '.join(command_pyinstaller))