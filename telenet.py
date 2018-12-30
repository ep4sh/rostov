#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import telnetlib

# настройки для телнет
telnet_host = "192.168.1.67"
user = "root"
password = "password2"
#################
tn = telnetlib.Telnet(telnet_host)

# вот тут важно - надо вписать то ПРИГЛАШЕНИЕ которые видно при входе на устройство
tn.read_until(b"login: ")
tn.write(user.encode('ascii') + b"\n")
if password:
    # АНАЛОГИЧНО, ПРИГЛАШЕНИЕ для ввода ПАРОЛЯ
    tn.read_until(b"password: ")
    tn.write(password.encode('ascii') + b"\n")
# перезагружаем устройство
tn.write(b"reboot\n")

print(tn.read_all().decode('ascii'))
