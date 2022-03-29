import API.in_word as InWord
import API.delete_word as DeleteWord
import API.learning_word as LearningWord
import API.end as End

print('''
########################################
                환영 합니다!    
########################################''')

User_answers = {
    '용어 입력': InWord,
    '용어 삭제': DeleteWord,
    '단어 학습': LearningWord,
    '종료': End
}


