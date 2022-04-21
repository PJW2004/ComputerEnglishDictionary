import random

from API.db.database import engine

text = '''\033[92m
        [지금부터 단어 학습을 시작하겠습니다.]
[기본 학습 단어는 최대 10번의 랜덤 단어로 지정이 됩니다.]
  [학습이 최종적으로 되었을 때 맞춘 단어와 맞추지 못한 
 단어를 나열 할 수 있으며, 맞출 확률또한 계산이 됩니다.]
'''

print(text)

conn = engine.connect()

select_ = "select * from userdata"

requests = conn.execute(select_)

word_li, meaning_li = [], []

for r in requests:
    word_li.append(r[0])
    meaning_li.append(r[1])



for ran in range(10):
    rl = random.randint(0, 1)
    word = random.choice(word_li)
    meaning = meaning_li[word_li.index(word)]
    if meaning[-1] == '.':
        if word[-1] == '.':
            word = word[:-1]
        meaning = meaning[:-1]
    if rl == 0:
        user = input(f'\033[93m[현재 제시된 "{word}"의 영단어는?] : ')
        if user == meaning.lower():
            print('\033[93m정답입니다!')
        else:
            print('\033[93m땡! 틀렸습니다.'
                  f'정답은 : "{meaning.lower()}"입니다.')
    elif rl == 1:
        user = input(f'\033[93m[현재 제시된 "{meaning.lower()}"의 정의는?] : ')
        if user == word:
            print('\033[93m정답입니다!')
        else:
            print('\033[93m땡! 틀렸습니다.'
                  f'정답은 : "{word}"입니다.')
