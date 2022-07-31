if __name__ == '__main__':
    list_of_names = []
    second_lowest = []
    scores = set()
    
    for _ in range(int(input())):
        name = input()
        score = float(input())    
        list_of_names.append([name,score])
        scores.add(score)
    
    for name, score in list_of_names: 
        if score == sorted(scores)[1]:
            second_lowest.append(name)
            
    for name in sorted(second_lowest):
        print(name, end = '\n')
