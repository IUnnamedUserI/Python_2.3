if __name__ == "__main__":
    sentence = input("Введите предложение: ")
    words = sentence.split()
    lst = []

    for i in range(len(words) - 1, -1, -1):
        lst.append(words[i])

    sentence = ' '.join(lst)

    print(sentence)
