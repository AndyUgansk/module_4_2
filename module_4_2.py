# -*- coding: utf-8 -*-
"""
Created on Sun Aug 25 09:43:28 2024

@author: Zver
"""

def test_function():
    # Это функция test_function
    def inner_function():
        # Это подфункция inner_function
        print('Я в области видимости функции test_function')
        return
    inner_function()
    return

test_function() # При вызове функции в консоли выводится текст из подфункции
                # inner_function()  
inner_function() # При вызове функции в консоли выводится ошибка:
                 # имя 'inner_function' не было определено