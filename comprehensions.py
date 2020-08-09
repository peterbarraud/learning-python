def dicts():
    d = {x:x/2 for x in range(1,10)}
    print(d)

def lists():
    l = [x for x in range(1, 10)]
    print(l)
    l = [x for x in range(1, 10) if x%2==0 if x%3==0]
    print(l)

def compare2lists():
    l1 = [1, 2, 3, 4, 5]
    l2 = [2, 3]
    l = [x for x in l1 if x not in l2]
    print(l)

if __name__ == "__main__":
    compare2lists()