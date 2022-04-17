from translate import get_translate
user = input('[입력할 용어를 적어 주세요]\n[한 👉 영] : ')

data = {user: get_translate(user)}
YN = (f'[data가 최종적으로 이렇게 저장이 됩니다.]\n[변경하지 않겠습니까? (Y/N)] : ')

if YN == 'Y':
    data = {user: input('[변경될 영어 번역을 입력해 주세요] : ')}
    print(data)
else:
    print(data)
    