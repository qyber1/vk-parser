import threading

from core import get_token
from app import APIWork


if __name__ == '__main__':
    groups = input('Введите @username групп через пробел: ').split(' ')

    parser = APIWork(token=get_token(), count=int(input('Введите количество постов для парсинга: ')))

    threads = [threading.Thread(target=parser.start, args=(group,)) for group in groups]
    for thread in threads:
        thread.start()
    for thread in threads:
        thread.join()


