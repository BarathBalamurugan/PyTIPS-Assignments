def char_freq(word):
    dict = {}
    for i in word:
        dict[i] = dict.get(i, 0) + 1
    return dict

if __name__ == '__main__':
    dict = {}
    print(char_freq(input("Enter a Word : ")))

# print(ord('3'))

# x = "Hello"

# assert x == 'Hello'

# assert x == 'Goodbye', "Not Equal"