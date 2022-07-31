if __name__ == '__main__':
    n = int(input())
    arr = map(int, input().split())
    sorted_set_arr = list(sorted(set(arr)))
    secondlarge = sorted_set_arr[-2]
    print(secondlarge)
        
