if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    value = round(sum(student_marks[query_name])/float(len(student_marks[name])),2)
    print(format(value, ".2f"))
    
