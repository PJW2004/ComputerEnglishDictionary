import os

User_answers = {
    '용어 입력': 'python ./API/in_word.py',
    '용어 삭제': 'python ./API/delete_word.py',
    '단어 학습': 'python ./API/learning_word.py',
    '종료': 'python ./API/end.py'
}

try:
    os.system(User_answers[input('''
    [용어 입력, 용어 삭제, 단어 학습, 종료]
👉 위에 있는 데로 똑같이 작성을 해 주셔야 합니다. 👈
>> ''')])
except KeyError:
    print('입력이 잘못 되었습니다.')
finally:
    print('\n프로그램을 종료합니다.')

