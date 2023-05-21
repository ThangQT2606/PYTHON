if __name__ == '__main__':
    # t = int(input())
    # cnt = 1
    # while cnt <= t:
        # cnt += 1
    n = input()
    for i in range(len(n)):
        if n[i] == '.':
            a = n[i+1::]
    # print(a)
    if a.lower() == 'py':
        print("yes")
    else:
        print("no")