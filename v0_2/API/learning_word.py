import random

from API.db.database import engine

text = '''
        [지금부터 단어 학습을 시작하겠습니다.]
[기본 학습 단어는 최대 10번의 랜덤 단어로 지정이 됩니다.]
[학습이 최종적으로 되었을 때 맞춘 단어와 맞추지 못한 단어를 나열 할 수 있으며,
 맞출 확률또한 계산이 됩니다.]
'''

print(text)

