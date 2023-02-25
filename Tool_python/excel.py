import pandas as pd
import os
import accuracy as ac

def excel(problems, answers, ac_list):
    data = {"제시어": problems, "입력단어": answers, "일치율": ac_list}
    df = pd.DataFrame(data)
    if not os.path.exists('MagicNumber.csv'):
        df.to_csv('MagicNumber.csv', index=False, mode='w', encoding='utf-8-sig')
    else:
        df.to_csv('MagicNumber.csv', index=False, mode='a', encoding='utf-8-sig', header=False)