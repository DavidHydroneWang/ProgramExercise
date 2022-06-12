#!/usr/bin/env python
# coding=utf-8
import paramiko


def ssh_command(ip, port, user, passwd, command):
    client = paramiko.SSHClient()
    # client can also support using key files
    # client.load_host_keys('~/.ssh/known_hosts')
    client.set_missing_host_key_policy(paramiko.AutoAddPolicy())
    client.connect(ip, port=port, username=user, password=passwd)
    ssh_session = client.get_transport().open_session()
    if ssh_session.active:
        ssh_session.exec_command(command)
        print(ssh_session.recv(1024))
    return


ssh_command('192.168.100.131', '22', 'justin', 'lovesthepython', 'ClientConnected')
