# user
print('[로그인을 먼저 해주셔야 프로그램이 시작됩니다.] : 계정이 없다면 "회원가입"을 입력해주세요')
user = input('user : ')
if user == '회원가입':
    user = input('[회원가입할 username을 입력해주세요] : ')
    passwd = input('[user의 비번은?] : ')

else:
    pass