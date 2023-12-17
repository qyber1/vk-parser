import datetime
import json
import os
from string import punctuation

class DataManage:


    @classmethod
    def remove_special_chars(cls) -> dict[int, None]:
        __chars = dict(zip(list(punctuation), [None for _ in range(len(punctuation))]))
        return __chars

    @staticmethod
    def save_data(data: dict, title_group: str) -> None:
        _chars = str.maketrans(DataManage.remove_special_chars())
        _folder = os.path.join(os.path.dirname(__file__), 'content')
        _file_path = os.path.join(_folder, f'{title_group.translate(_chars)}.json')

        if not os.path.exists(_folder):
            os.makedirs(_folder)

        if os.path.exists(_file_path):
            os.remove(_file_path)


        with open(_file_path, 'w', encoding='UTF-8') as file:
            file.write(json.dumps(data, ensure_ascii=False, indent=4))

    @staticmethod
    def convert_date(date: int) -> str:
        dt_object = datetime.datetime.fromtimestamp(date)
        return dt_object.strftime('%Y-%m-%d %H:%M:%S')