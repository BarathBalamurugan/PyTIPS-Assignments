def generate_n_chars(n, character):
    for i in range(0, int(n)):
        print(character, end="")

if __name__ == "__main__":
    n = input("Enter the length of the generated string : ")
    character = input("Enter the Character to be repeated : ")
    generate_n_chars(n, character)
