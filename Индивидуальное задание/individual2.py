#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    a = int(input('Введите первое число: '))
    b = int(input('Введите второе число: '))
    c = int(input('Введите третье число: '))

    if a % 2 == 1 or b % 2 == 1 or c % 2 == 1:
        print('Есть нечётное число')
    else:
        print('Нет нечётных чисел')