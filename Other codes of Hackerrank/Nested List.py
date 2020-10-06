if __name__ == '__main__':
    list = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        list.append([name, score])


    def custom_key(list):
        return list[1]


    list.sort()
    list.sort(key=custom_key)

    min = list[0]

    for i in list:
        if i[1] > min[1]:
            print(i[0])
            runner_up = i
            list.remove(runner_up)
            break

    for i in list:
        if i[1] == runner_up[1]:
            print(i[0])
