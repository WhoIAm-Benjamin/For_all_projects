import subprocess as s
print(s.check_output(args = ['nslookup', 'myip.opendns.com.', 'resolver1.opendns.com']).decode('cp866').split()[3])
input()