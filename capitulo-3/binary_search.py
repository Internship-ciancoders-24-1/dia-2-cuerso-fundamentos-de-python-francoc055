import random


def binary_search(data, target, low, high):
    while low <= high:
        mid = (low + high) // 2

        if data[mid] == target:
            return True
        elif data[mid] > target:
            high = mid - 1
        else:
            low = mid + 1

    return False


    

if __name__ == "__main__":
    data = [random.randint(0, 100) for i in range(10)]

    data.sort()
    print(data)

    target = int(input("que numero desea buscar?: "))
    found = binary_search(data, target, 0, len(data)-1)

    print(found)