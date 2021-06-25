import requests

url_base = "http://172.28.0.3:8000/"


def get_produtc():
    url_test = url_base + "product/"
    r = requests.get(url_test)
    produtos_dict = r.json()

    print(produtos_dict)


def post_produtc():
    url_test = url_base + "product/"
    objeto = {
        "name": "test oi",
        "description": "test oi",
        "price": 11.0,
        "category": 1,
    }
    r = requests.post(url_test, data=objeto)

    produtos_dict = r.json()

    print(produtos_dict)


def put_produtc():
    url_test = url_base + "product/1/"
    objeto = {
        "name": "test put",
        "description": "test put",
        "price": 141.0,
        "category": 1,
    }
    r = requests.put(url_test, data=objeto)

    produtos_dict = r.json()

    print(produtos_dict)


def patch_produtc():
    url_test = url_base + "product/2/"
    objeto = {
        "name": "test patch",
    }
    r = requests.patch(url_test, data=objeto)

    produtos_dict = r.json()

    print(produtos_dict)


def delete_produtc():
    url_test = url_base + "product/3/"

    r = requests.delete(url_test)

    produtos_dict = r.status_code

    print(produtos_dict)


get_produtc()
post_produtc()
put_produtc()
patch_produtc()
delete_produtc()
get_produtc()
