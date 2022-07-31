import string 

def print_rangoli(size):
    # your code goes here
    for i in list(range(size))[::-1] + list(range(1,size)):
        print('-'.join(string.ascii_lowercase[size-1:i:-1] + string.ascii_lowercase[i:size]).center(4 * size - 3,'-'))

