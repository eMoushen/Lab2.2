#!/usr/bin/env python3
# -*- coding: utf-8 -*-

if __name__ == '__main__':
    n = 64

    for k in range(n):
        for g in range(n):
            if k * 4 + g * 2 == n:
                print(k, 'Кроликов', 'и', g, 'Гусей')
