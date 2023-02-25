def ac(problems: list, answers: list):
    ac_list = []
    for i in range(len(problems)):
        problem = problems[i]
        answer = answers[i]
        cnt = 0
        for j in range(len(problem)):
            if problem[j] == answer[j]:
                cnt += 1
        ac = str(round(cnt/len(problem)*100, 3))+"%"
        ac_list.append(ac)
    
    return ac_list