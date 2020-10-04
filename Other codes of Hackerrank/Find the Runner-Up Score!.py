if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())

    list = []
    for i in arr:
        list.append(i)

    list.sort(reverse=True)
    max = list[0]
    list.remove(max)
    for i in list:
        if i < max:
            print(i)
            break
