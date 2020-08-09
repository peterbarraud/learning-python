def addnumbers(i, j):
    if i.isnumeric() and j.isnumeric():
        print(int(i) + int(j))
    else:
        print("something isn't right")

def main():
    # take user input
    i = input('enter a number: ')
    j = input('enter another number: ')
    addnumbers(i, j)

if __name__ == "__main__":
    main()
