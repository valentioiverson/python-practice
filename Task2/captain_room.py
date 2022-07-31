# Enter your code here. Read input from STDIN. Print output to STDOUT

K = int(input())
arr = input().split(); 
unique_set = set();
multiple_set = set(); 
for i in arr:
    if i in unique_set:
        multiple_set.add(i); 
    else:
        unique_set.add(i); 

captain_num = unique_set.difference(multiple_set); 
print(captain_num.pop())
