import os
import random


# 시작 구성
class Start_Program:
    data_list = {

    }

    def __init__(self):
        if not os.path.exists('API/data_list'):
            with open('./API/data_list', 'w') as data:
                data.write("term:difinition,\n")
                data.close()

    # 현재 데이터 체크
    def Check_the_word(self, check=0):
        with open('./API/data_list', 'r') as data:
            for i in data:
                try:
                    term = i.split(':')[0]
                    difinition = i.split(':')[1][:-2]
                    print(f"{term} : {difinition}")
                    self.data_list.update({f'{term}': f'{difinition}'})

                except IndexError:
                    pass
            data.close()

    # 데이터 삭제
    def delete_data(self, Ddata):
        self.text = """"""
        with open('./API/data_list', 'r') as data:
            for i in data:
                if i.split(':')[0] != Ddata:
                    term = i.split(':')[0]
                    difinition = i.split(':')[1][:-2]
                    self.text += f"{term}:{difinition},\n"
            data.close()
        with open('./API/data_list', 'w') as data:
            data.write(self.text)
            data.close()


# 용어 학습
class Word_test:
    def __init__(self):
        if len(list(Start_Program.data_list)) > 0:
            keys = list(Start_Program.data_list)
            random.shuffle(keys)

            for english in keys:
                korean = Start_Program.data_list[english]

                guess = input(f'{english} 영어 단어를 번역하세요: ')

                if guess == korean:
                    print('영어 단어의 번역이 맞습니다.\n')
                else:
                    Word_test()
        else:
            print('데이터가 부족합니다.')
