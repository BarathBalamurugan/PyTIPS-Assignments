import List2

def is_palindrome(word):
    if word == List2.reverse(word):
        return True
    return False

if __name__ == "__main__":
    word = input("Enter the word to be checked : ")
    print(is_palindrome(word))