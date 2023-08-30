import iuliia

source = "Харитон"
trans = iuliia.translate(source, schema=iuliia.WIKIPEDIA)
print(trans)

import paramiko

def connect_to_cisco(hostname, username, password):
  ssh = paramiko.SSHClient()
  ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
  ssh.connect(hostname, username=username, password=password)
  return ssh

hostname = '10.28.52.254'
username = 'simakov'
password = '28fev1980M07'

ssh = connect_to_cisco(hostname, username, password)
print("Connected to Cisco device")

def execute_command_on_cisco(ssh, command):
 stdin, stdout, stderr = ssh.exec_command(command)
 result = stdout.read().decode('utf-8')
 return result

command = 'show interfaces'
result = execute_command_on_cisco(ssh, command)
print(result)