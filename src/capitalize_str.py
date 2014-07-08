#!/usr/bin/env python
# -*- coding: utf-8 -*-
'''
Created on Jul 8, 2014

@author: anroco

How to capitalize the first letter of string in python?

¿Como convertir el primer carácter en mayúscula y el resto en minuscula
(letra capital) de un str python?
'''

#enclosed in single quotes
s = 'many years later, as he faced the firing squad'
print(s)

#the capitalize() method generates copy of the string with its first character
#capitalized and the rest lowercased.
s_capitalize = s.capitalize()
print(s_capitalize)
print(s)
