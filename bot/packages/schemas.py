from pydantic import BaseModel


class UrlBase(BaseModel):
    image = str
    category = str
    description: str


class MainUrlList(UrlBase):
    id: int

    class Config:
        orm_mode = True
