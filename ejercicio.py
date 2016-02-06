# -*- coding: utf-8 -*-

passwd = open('/etc/passwd', 'r')

lineas = passwd.readlines()
passwd.close()

diccionario = {}

for linea in lineas:
	elementos = linea.split(':')
	diccionario[elementos[0]] = elementos[-1]


try:
	print 'root:', diccionario['root'],
	print diccionario['imaginario'],
except KeyError:
	print 'El usuario "imaginario" no existe',
