'''

@author: Administrator
'''


import paramiko
import os,sys,time
from pymysql.constants.ER import HOSTNAME

blip="192.168.110.128"
bluser="root"
blpassword="123456"

host="192.168.110.128"
username="root"
password="123456"

tmpdir="/tmp"
remotedir="/mnt/test"
localpath=r"C:\\Users\Administrator\Desktop\automation\pcre-8.34.tar.gz"

tmppath=tmpdir+"/pcre-8.34.tar.gz"
remotepath=remotedir+"/pcre-8.34.tar.gz"
port=22

passinfo='\'s password: '

paramiko.util.log_to_file('syslogin.log')

t= paramiko.Transport((blip,port))

t.connect(username=bluser, password=blpassword)

sftp = paramiko.SFTPClient.from_transport(t)
sftp.put(localpath,tmppath)
sftp.close()


ssh = paramiko.SSHClient()
ssh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh.connect(hostname=blip,username=bluser,password=blpassword)

channel= ssh.invoke_shell()
channel.settimeout(10)
channel.send('scp ' +tmppath+' '+username+'@'+host+':'+remotepath+'\n')
buff=''
# resp=''

while not buff.endswith('# '):
    resp = channel.recv(9999)
    if not resp.find(passinfo) == -1:
        print 'Error info : Authentication failed.'
        channel.close()
        ssh.close()
        sys.exit()
        
    buff += resp
    

print buff

channel.close()
ssh.close()
        
    





