def reverse(sentence):
    reversedWord = ''
    for i in range(0, len(sentence)):
        reversedWord += sentence[(i+1)*(-1)]

    return reversedWord

if __name__ == "__main__":
    sentence = input("Enter the string to Reverse : ")
    print(reverse(sentence))