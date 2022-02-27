# 실제 동작 program
from APIv.starting import Word_test
from APIv.starting import Start_Program
from APIv.Input_Program import In_Terms

print("// ######################################## // "
      "\n        환영 합니다!    \n// "
      "######################################## //")
SP = Start_Program()
User_answers = {
    '0': '용어 입력',
    '1': '용어 삭제',
    '2': '단어 학습',
    '3': '종료'
}
print(f'{User_answers} \n')
while True:
    User_answer = input('>> ')
    if User_answer == '0':
        print('현재 단어')
        SP.Check_the_word()

        Term = input('\n입력할 용어 : ')
        Definition = input('용어에 해당 하는 정의 정의 : ')

        In_Terms(terms=Term, definitions=Definition)
        print('완료\n\n')

    elif User_answer == '1':
        print('현재 단어')
        SP.Check_the_word()
        User_answer = input('어떤 용어를 삭제 하고 싶습 니까?')
        SP.delete_data(User_answer)

    elif User_answer == '2':
        Word_test()

    elif User_answer == '3':
        print('프로그램이 종료 됩니다.')
        break

    elif User_answer == '':
        pass

    else:
        print('잘못된 입력')
        print(f'{User_answers} \n')
