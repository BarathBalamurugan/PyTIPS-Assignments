def overlapping(len1, len2, list1, list2):
    for i in range(0, int(len1)):
        for j in range(0, int(len2)):
            if list1[i] == list2[j]:
                return True
    return False

if __name__ == "__main__":
    list1 = []
    list2 = []

    len1 = input("Length of List One : ")

    for i in range(0,int(len1)):
        element = input()
        list1.append(element)

    len2 = input("Length of List Two : ")

    for i in range(0,int(len2)):
        element = input()
        list2.append(element)

    print(overlapping(len1, len2, list1, list2))
