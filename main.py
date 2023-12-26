def BobleSort():
    pass


def Reverse(arr: list):
    rezArr = []
    for i in range(len(arr)-1, -1, -1):
        rezArr.append(arr[i])
    return rezArr


def Square(a):
    rezSqr = a * a
    return rezSqr


if __name__ == "__main__":
    BobleSort()
    Reverse([1, 2, 3])
    Square(5)
