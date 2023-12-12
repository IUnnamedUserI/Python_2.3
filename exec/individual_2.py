#!/usr/bin/python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sentence = input("Введите предложение: ")
    n_count = 0
    k_count = 0


    for i in sentence:
        if i == 'н' or i == 'Н':
            n_count += 1
        elif i == 'к' or i == 'К':
            k_count += 1

    if n_count == 0 or k_count == 0:
        print("В строке нет букв 'н' и/или 'к'")
        exit(1)

    for i in sentence:
        if i == 'н' or i == 'Н':
            print("Буква 'н' встречается раньше")
            break
        elif i == 'к' or i == 'К':
            print("Буква 'к' встречается раньше")
            break
    