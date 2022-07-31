# Enter your code here. Read input from STDIN. Print output to STDOUT

num_A = int(input())
set_A = set(map(int, input().split()))
N = int(input())

for i in range(N):
    command, num_B = input().split()
    set_B = set(map(int, input().split()))
    if(command == "intersection_update"):
        set_A.intersection_update(set_B)
    elif(command == "update"):
        set_A.update(set_B)
    elif(command == "symmetric_difference_update"):
        set_A.symmetric_difference_update(set_B)
    elif(command == "difference_update"):
        set_A.difference_update(set_B)

print(sum(set_A))
