import pandas as pd

def get_data():
    nums = list(map(str, list(range(10)))) #숫자 리스트
    english = list("qwertyuiopasdfghjklzxcvbnm") #영어 리스트

    data = pd.read_csv("kor_language.csv")
    n = 1000 # 몇번째 순위까지 쓸지
    data = data["단어"]
    data = data[:n]
    kor_list = data.values.tolist()
    list_to_word = "".join(kor_list)
    word = "".join(list(set(list(list_to_word))))
    for num in nums:
        word = word.replace(num, "")
    k_list = list(word)
    wolast = []
    for i in range(399):
        wolast.append(44032+28*i)

    word_wo = []
    word_w = list(word)
    for i in list(word):
        a = ord(i)
        if a in wolast:
            word_w.remove(chr(a))
            word_wo.append(chr(a))

    return [k_list, word_w, word_wo, english, nums]
    #순서대로 한글, 한글받침, 한글받침x, 양어, 숫자


