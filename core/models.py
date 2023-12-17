from pydantic import BaseModel


class PostInfo(BaseModel):
    id_post: int
    published_date: str
    name_group: str
    count_like: int
    count_repost: int
    count_views: int
    comments: int | None


class Info(BaseModel):
    list_data: list[dict]

