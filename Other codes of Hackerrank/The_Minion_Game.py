# Answer to the hackerrank question 'The Minion Game'
# URL: https://www.hackerrank.com/challenges/the-minion-game/problem

def minion_game(string):
    kevin = 0
    stuart = 0
    length = len(string)
    vowels = ['A', 'E', 'I', 'O', 'U']

    for i in range(length):
        if string[i] in vowels:
            kevin += length - i
        else:
            stuart += length - i

    if kevin > stuart:
        print("Kevin", kevin)
    elif kevin == stuart:
        print("Draw")
    else:
        print("Stuart", stuart)


if __name__ == '__main__':
    s = input()
    minion_game(s)
