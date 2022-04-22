import os
import random

from API.db.database import engine

text = '''\033[92m
        [지금부터 단어 학습을 시작하겠습니다.]
[기본 학습 단어는 최대 10번의 랜덤 단어로 지정이 됩니다.]
  [학습이 최종적으로 되었을 때 맞춘 단어와 맞추지 못한 
 단어를 나열 할 수 있으며, 맞출 확률또한 계산이 됩니다.]
'''

print(text)


def requests_(select_=None):
    conn = engine.connect()

    requests = conn.execute(select_)

    li_1, li_2 = [], []

    for r in requests:
        li_1.append(r[0])
        li_2.append(r[1])
    return li_1, li_2


word_li, meaning_li = requests_(select_="select * from userdata")

correct = 0
failure = []

for ran in range(10):
    rl = random.randint(0, 1)
    word = random.choice(word_li)
    meaning = meaning_li[word_li.index(word)].lower()
    if meaning[-1] == '.':
        if word[-1] == '.':
            word = word[:-1]
        meaning = meaning[:-1]
    if rl == 0:
        user = input(f'\033[93m[현재 제시된 "{word}"의 영단어는?] : ')
        if user == meaning:
            print('\033[92m\n정답입니다!')
            correct += 1
        else:
            print('\033[94m\n땡! 틀렸습니다.'
                  f'정답은 : "{meaning}"입니다.')
            failure.append(meaning)

    elif rl == 1:
        user = input(f'\033[93m[현재 제시된 "{meaning}"의 정의는?] : ')
        if user == word:
            print('\033[92m\n정답입니다!')
            correct += 1
        else:
            print('\033[94m\n땡! 틀렸습니다.'
                  f'정답은 : "{word}"입니다.')
            failure.append(meaning)

print(f'''\33[92m
    최종적으로 사용자 님의
    정답률은 : {correct*10}%이며,
    10개의 문제중 {correct}만큼 맞추셨습니다.''')

os.system('python __init__.py')
