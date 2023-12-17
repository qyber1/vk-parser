import vk_api

class VK:

    def __init__(self, token: str, count: int) -> None:
        """
        token - Токен необходимо получить в ВК после создания приложения
        count - Количество записей которые необходимо спарсить. Максимум 100
        """
        self._client = vk_api.VkApi(token=token).get_api()
        self.count = count
