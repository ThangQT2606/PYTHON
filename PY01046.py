def tower_of_hanoi(n, source, auxiliary, target):
    if n == 1:
        print("{} -> {}".format(source, target))
        return
    
    tower_of_hanoi(n-1, source, target, auxiliary)
    print("{} -> {}".format(source, target))
    tower_of_hanoi(n-1, auxiliary, source, target)

n=int(input())
tower_of_hanoi(n, 'A', 'B', 'C')