class In_Terms:
    def __init__(self, terms=None, definitions=None):
        # data 를 입력할 수 있도록 해준다.
        with open('./APIv/data_list', 'a') as data:
            data.write(f"{terms}:{definitions},\n")
            data.close()
