#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import paramiko

# Настройки для SSH
hosts = ['192.168.88.252', '192.168.88.252', '192.168.88.252']
user = 'ep4sh'
secret = 'root'
port = 22
remote_ssh_server_dir = "test"
remote_ssh_server_telnet_file = "telnet.py"


for host in hosts:
    client = paramiko.SSHClient()
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    # Подключение
    client.connect(hostname=host, username=user, password=secret, port=port)

    # Выполнение команды
    stdin, stdout, stderr = client.exec_command("cd "+remote_ssh_server_dir+" && python "+remote_ssh_server_telnet_file+" ")

    # Читаем результат
    data = stdout.read() + stderr.read()
    print(data.decode("utf-8"))
    client.close()
