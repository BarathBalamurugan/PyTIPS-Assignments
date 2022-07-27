def translate(word):
    global dict
    return dict[word]

if __name__ == "__main__":
    dict = {"merry":"god", "christmas":"jul", 
            "and":"och", 
            "happy":"gott", 
            "new":"nytt",
            "year":"år"}
    engSen = input("Enter a Sentence : ")
    engList = engSen.split(' ')
    translated = list((map(translate, engList)))
    string = ' '
    print(string.join(translated))