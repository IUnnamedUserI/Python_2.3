#!/usr/bin/python3
# -*- coding: utf-8 -*-

if __name__ == "__main__":
    sentence = input("Введите предложение: ")
    index = 0

    for i in sentence:
        if i == 'и' and index % 2 == 0:
            print(f"[{index}] {i}")
        
        index += 1
        