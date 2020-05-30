import requests


def get_data(url):
    data = requests.get(url)
    print(data.content.decode("utf-8"))


if __name__ == '__main__':
    url = 'http://127.0.0.1:5000/getnews/'
    get_data(url)