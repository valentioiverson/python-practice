import math 

scores = []
for i in range(5):
    scores.append(tuple(map(int, input().strip().split(' '))))
        
X = [n[0] for n in scores]
Y = [n[1] for n in scores]    
n = len(X)
new_X = [x*x for x in X]
new_Y = [y*y for y in Y]
newlist = []
for num1, num2 in zip(X, Y):
    newlist.append(num1 * num2)

d = n * sum(new_X) - sum(X) ** 2    
c = ((sum(Y) * sum(new_X)) - (sum(X) * sum(newlist)))/d
m = ((n * sum(newlist)) - sum(X) * sum(Y))/d
value = 80 * m + c
print(round(value, 3))