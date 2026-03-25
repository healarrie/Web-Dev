if __name__ == '__main__':
    n = int(input())
    student_marks = {}
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    query_name = input()
    scores_to_average = student_marks[query_name]
    
    average = sum(scores_to_average) / len(scores_to_average)
    
    print(f"{average:.2f}")