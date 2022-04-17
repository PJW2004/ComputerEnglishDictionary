import requests

def get_translate(text):
    client_id, client_secret = 'LnbkGpZ1FltpJ_Jytof0', '2odQqgaDim'
    url = 'https://openapi.naver.com/v1/papago/n2mt'
    data = {'text': text,
            'source': 'ko',
            'target': 'en'}


    header = {
        ''
    }