import random

def make(data, idx, num, length):
    word = data[idx]
    random.shuffle(word)
    problems = []
    start = 0
    end = length
    if len(word) < num*length:
        key = num*length//len(word) + 1
        word = word*key
        random.shuffle(word)
    for i in range(num):
        problem = word[start:end]
        problems.append("".join(problem))
        start += length
        end += length
    
    return problems



