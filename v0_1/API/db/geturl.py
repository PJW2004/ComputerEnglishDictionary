import yaml


def yaml_loader(db_num):
    with open("../config.yaml", "r") as config:
        data = yaml.safe_load(config)
        data = data.get('db').get('postgres').get(f'{db_num}')
        usr, passwd, host, port, dbname = data.get('user'), data.get('host'), data.get('host'), data.get('port'), data.get('dbname')
        config.close()

    url = f"postgresql://{usr}:{passwd}@{host}:{port}/{dbname}"

    return url
