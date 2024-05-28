import paramiko

# SSH连接参数
hostname = '192.168.7.201'
port = 22
username = 'root'
password = 'moredian@1'

# Shell脚本路径
script_path = '/root/test/script.sh'

# 建立SSH连接
ssh_client = paramiko.SSHClient()
ssh_client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
ssh_client.connect(hostname, port, username, password)

# 执行Shell脚本
stdin, stdout, stderr = ssh_client.exec_command(f'bash {script_path}')
output = stdout.read().decode('utf-8')

# 打印输出
print(output)

# 关闭SSH连接
ssh_client.close()