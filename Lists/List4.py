x = input("Enter the character to be checked : ")
length = input("Length of the List : ")
list = []

def is_member():
    for i in range(0,int(length)):
        element = input()
        list.append(element)
        if x == list[i]:
            return True
    
    return False

if __name__ == "__main__":
    print(is_member())
