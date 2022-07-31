# Enter your code here. Read input from STDIN. Print output to STDOUT

n, m = input().split()
array = [int(x) for x in input().split()]
like = set([int(y) for y in input().split()])
dislike = set([int(z) for z in input().split()])
print(sum((i in like) - (i in dislike) for i in array))
