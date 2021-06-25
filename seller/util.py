import requests
import csv

def set_url(url: str):
    return url


def get_request():
    '''
    Função faz requisição e retorna o json com lista de produtos
    param: 
    return: int
    '''
    url_test = set_url() + "product/"
    r = requests.get(url_test)
    produtos_dict = r.json()

    return produtos_dict


def post_request():
    '''
    Função faz requisição post, enviando dados de produto, e retorna o json do produto
    param: 
    return: int
    '''
    url_test = set_url() + "product/"
    objeto = {
        "name": "test oi",
        "description": "test oi",
        "price": 11.0,
        "category": 1,
    }
    r = requests.post(url_test, data=objeto)

    produtos_dict = r.json()

    return produtos_dict


def put_request(id: int):
    '''
    Função faz requisição put, alterando dados do produto e retorna o json do produto deletado
    param: 
    return: int
    '''
    url_test = f"{set_url()}'product'/{id}/"
    objeto = {
        "name": "test put",
        "description": "test put",
        "price": 141.0,
        "category": 1,
    }
    r = requests.put(url_test, data=objeto)

    produtos_dict = r.json()

    return produtos_dict


def patch_request():
    '''
    Função faz requisição e retorna o json do produto deletado
    param: 
    return: int
    '''
    url_test = set_url() + "product/2/"
    objeto = {
        "name": "test patch",
    }
    r = requests.patch(url_test, data=objeto)

    produtos_dict = r.json()

    return produtos_dict


def delete_request() -> int:
    '''
        Função faz requisição e retorna o status code
        param: 
        return: int
    '''
    url_test = set_url() + "product/3/"

    r = requests.delete(url_test)

    produtos_dict = r.status_code

    return produtos_dict


# set_url("http://172.28.0.3:8000/")
# get_request()
# post_request()
# put_request()
# patch_request()
# delete_request()
# get_request()

