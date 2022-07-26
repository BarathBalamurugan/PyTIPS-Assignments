length = input("Enter the length of the list :")

list = []

def myInput():
    for i in range(0,int(length)):
        element = input()
        list.append(element)
    return list

def sum():
    sum = 0
    for i in range(0,int(length)):
        sum += int(list[i])
    print("Sum of the elements of the list is ", sum)

def multiply():
    product = 1
    for i in range(0,int(length)):
        product *= int(list[i])
    print("Product of the elements of the list is ", product)

if __name__ == "__main__":
    myInput()
    sum()
    multiply()
