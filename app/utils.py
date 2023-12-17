from vk_api import VkApi

from core import DataManage, Info, PostInfo
from .instance import VK


class APIWork(VK):

    @staticmethod
    def get_id_group(title_group: str, client: VkApi) -> dict:
        id_group = dict()
        result_id = client.groups.getById(group_id=title_group,
                                          fields=['id'])
        for result in result_id:
            id_group.setdefault(result['name'], result['id'] * -1)
        return id_group

    def start(self, group: str) -> None:
        id_group = self.get_id_group(group, self._client)

        for name_group, id_group in id_group.items():
            request = self._client.wall.get(owner_id=id_group, count=self.count)

            result = self.pars_posts(
                request=request,
                name_group=name_group,
            )

            DataManage.save_data(
                data=result.list_data,
                title_group=name_group
            )

    def pars_posts(self, request: dict, name_group: str) -> Info:
        list_data: list[dict] = []

        for post in request['items']:
            post_info = PostInfo(
                id_post=post['id'],
                count_like=post['likes']['count'],
                count_repost=post['reposts']['count'],
                name_group=name_group,
                count_views=post['views']['count'],
                comments=post['comments']['count'],
                published_date=DataManage.convert_date(post['date']))

            list_data.append(post_info.model_dump())

        return Info(list_data=list_data)
